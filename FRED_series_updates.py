import os
import requests
import json
import pandas as pd
from pandas.errors import EmptyDataError

# Retrieve FRED API key from the appropriate User variable
API_KEY = os.environ['FRED_API_KEY']

# Explicity state file type
FILE_TYPE = 'json'

# Define the URL and the headers
url = f'https://api.stlouisfed.org/fred/series/updates?api_key={API_KEY}&file_type={FILE_TYPE}'

# Send the GET request
response = requests.get(url=url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Write the JSON data to a file
    with open(file='data.json', mode='w') as f:
        json.dump(obj=data, fp=f, indent=4)

    # Create a DataFrame from the 'seriess' array
    df_new = pd.DataFrame(data=data['seriess'])

    # Load the existing data
    try:
        df_existing = pd.read_csv(filepath_or_buffer='seriess_data.csv')
    except EmptyDataError:
        df_existing = pd.DataFrame()

    # Append new data to the existing DataFrame
    df_combined = pd.concat(objs=[df_existing, df_new]).drop_duplicates(subset=['id'])

    # Write the combined DataFrame back to the CSV file
    df_combined.to_csv(path_or_buf='seriess_data.csv', index=False)