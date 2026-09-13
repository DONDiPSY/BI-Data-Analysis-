import pandas as pd
import json
with open("Raw_OpenAQ_20260803_170745.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.json_normalize(data["results"])

print(f"Total columns: {len(df.columns)}\n")

for col in sorted(df.columns):
    print(col)
