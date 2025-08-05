import requests
import pandas as pd
import os

csv_file = "chicago_crime_data_incremental.csv"
api_url = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"

limit = 1000

def convert_complex_cols_to_str(df):
    for col in df.columns:
        if df[col].apply(lambda x: isinstance(x, dict) or isinstance(x, list)).any():
            df[col] = df[col].astype(str)
    return df

if os.path.exists(csv_file):
    df_existing = pd.read_csv(csv_file)
    if "date" in df_existing.columns and not df_existing.empty:
        last_date = df_existing["date"].max()
        last_date = pd.to_datetime(last_date)
        start_date = (last_date + pd.Timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S')
    else:
        start_date = "2023-01-01T00:00:00"
else:
    df_existing = pd.DataFrame()
    start_date = "2023-01-01T00:00:00"

offset = 0

while True:
    params = {
        "$limit": limit,
        "$offset": offset,
        "$order": "date ASC",
        "$where": f"date >= '{start_date}'"
    }
    response = requests.get(api_url, params=params)
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        break
    batch = response.json()
    if not batch:
        print("No more data to fetch.")
        break

    df_batch = pd.DataFrame(batch)

    df_batch = convert_complex_cols_to_str(df_batch)
    df_existing = convert_complex_cols_to_str(df_existing)

    df_existing = pd.concat([df_existing, df_batch], ignore_index=True).drop_duplicates()

    df_existing.to_csv(csv_file, index=False)
    print(f"Fetched {len(batch)} records... total saved: {len(df_existing)}")

    if len(batch) < limit:
        print("All data fetched.")
        break

    offset += limit
