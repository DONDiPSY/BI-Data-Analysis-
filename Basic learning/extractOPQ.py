import json
import requests
from datetime import datetime

# HTTP
url = ""
api_key = "2aa5f014dacd89de622df3de68d988b63da1464c682fbd8d2598b5b1ace91e95"
Header = {
    "X-Api-Key" : api_key,
    "Accept" : "application/json",
    "Content-Type" : "application/json"
}

# A Function that Extract from the API and write new json file
# check if extract  is successful convert text to json file
def ExtractAQ(f_url, f_header):
    try:
        response = requests.get(f_url, timeout= 5, headers = f_header)
        if response.status_code == 200:
            data = response.json()
            filename = f"RawOPQ{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
            with open (filename, "w") as f:
                json.dump(data, f , indent=4)
                print(f"{f_url} saved to \n{filename}")

        else:
            print(f"Failed to retrieve {response.status_code} from {f_url}")


    except requests.exceptions.RequestsException as e:
        print(f"An error has occurred: {e}")


ExtractAQ(url,Header)



