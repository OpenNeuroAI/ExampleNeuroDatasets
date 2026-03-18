## Some ideas for how to load and visualise the dataset

# Download the excel file if not present
import os
import pandas as pd

filename = "elife-88229-supp1-v1.xlsx"
url = "https://cdn.elifesciences.org/articles/88229/%s" % filename

if not os.path.exists(filename):
    print("Downloading %s from %s" % (filename, url))
    import requests

    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)
else:
    print("File %s already exists, skipping download" % filename)


df = pd.read_excel(filename, sheet_name="Key to conditions")

print(df.head())

df = pd.read_excel(filename, sheet_name="Fitness all conditions")

print(df.head())
