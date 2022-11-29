# example of pulling csv data from a public gsheet with pandas
# output would have to be pasted into the sheet manually
# alternatively, use google's python api, but that requires authentication and gcloud setup

import pandas as pd

SHEET_ID = '1HPVsZ2BZ8rZIKK7biWq1johSrvlDN4nioLXX0stiNFY'
SHEET_NAME = '2022Q4'

url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)

# print player list
print(df)

# randomize player list
print(df.sample(frac=1).reset_index(drop=True))