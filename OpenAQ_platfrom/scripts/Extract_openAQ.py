import requests
import json
import time
from pathlib import Path
from datetime import datetime


def extract_data(url, headers, raw_dir, max_pages=10, timeout=80, max_retries=3):
    """
    Pull paginated results from the OpenAQ API and save them as a single
    raw JSON file.

    Parameters
    ----------
    url : str
        Base API URL (page number gets appended).
    headers : dict
        Request headers (e.g. API key).
    raw_dir : str or Path
        Directory the raw JSON file should be saved into.
    max_pages : int
        Number of pages to fetch (default 50).
    timeout : int
        Seconds to wait for a response before giving up on a single request.
    max_retries : int
        Number of attempts per page before moving on.

    Returns
    -------
    raw_path : Path
        Full path to the saved JSON file.

    Raises
    ------
    requests.exceptions.RequestException
        If a request fails outright (connection error, timeout, etc).
    ValueError
        If no records were fetched at all — signals a failed run rather
        than silently succeeding with an empty file.
    """
    # Make sure raw_dir is a Path object, even if a plain string was passed in
    raw_dir = Path(raw_dir)

    # This will collect every record from every page before we save anything
    all_data = []

    # Loop through each page number, from 1 up to max_pages (inclusive)
    for page in range(1, max_pages + 1):

        # If the base url already has a "?" (existing query params), use "&"
        # to add another one; otherwise this is the first param, so use "?"
        separator = "&" if "?" in url else "?"

        # Build the full URL for this specific page
        paginated_url = f"{url}{separator}page={page}"

        # Try this page up to max_retries times before giving up on it
        for attempt in range(1, max_retries + 1):
            try:
                # Send the GET request; timeout applies to both connecting
                # and waiting for a response
                response = requests.get(paginated_url, timeout=timeout, headers=headers)

                # 200 means success — parse and store the results
                if response.status_code == 200:
                    data = response.json()
                    # .get("results", []) avoids a KeyError if "results" is missing
                    all_data.extend(data.get("results", []))
                    print(f"Fetched page {page} successfully!")
                    # Success — stop retrying this page and move to the next one
                    break
                else:
                    # A non-200 status (e.g. 404, 500) usually won't be fixed
                    # by retrying, so log it and move on without retrying
                    print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
                    break

            except requests.exceptions.RequestException as e:
                # This catches network-level failures: timeouts, connection
                # drops, DNS errors, etc. (not HTTP error status codes)
                print(f"Page {page}, attempt {attempt}/{max_retries} failed: {e}")

                if attempt == max_retries:
                    # We've used up all our attempts for this page — give up on it
                    print(f"Giving up on page {page} after {max_retries} attempts.")
                else:
                    # Wait a bit before retrying (2s, then 4s, then 6s...)
                    # This gives a temporary network issue time to resolve
                    time.sleep(2 * attempt)

    # If every single page failed, all_data will still be empty — treat
    # that as a failed run rather than silently saving an empty file
    if not all_data:
        raise ValueError("No records were fetched from any page — aborting.")

    # Create the raw data directory if it doesn't already exist
    raw_dir.mkdir(parents=True, exist_ok=True)

    # Build a filename that includes a timestamp, so each run gets its own file
    filename = f"Raw_OpenAQ_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    raw_path = raw_dir / filename

    # Write all collected records to disk as a single JSON file
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=4)

    print(f"Data fetched successfully! Total records: {len(all_data)}")
    print(f"Saved as {raw_path}")

    return raw_path


# Only runs when this file is executed directly (not when imported elsewhere)
if __name__ == "__main__":
    # Import the raw data output directory from your config module
    from config import Raw_dir

    # Base OpenAQ endpoint — page numbers get appended to this in extract_data()
    url = "https://api.openaq.org/v3/locations"

    # OpenAQ API key
    api_key = "2aa5f014dacd89de622df3de68d988b63da1464c682fbd8d2598b5b1ace91e95"

    # Headers sent with every request: the API key, and telling the server
    # we want a JSON response back
    headers = {
        "X-API-Key": api_key,
        "Accept": "application/json"
    }

    # Run the extraction and save the raw JSON file
    extract_data(url, headers, Raw_dir)


