# reading data from CSV in Python

import piplite
await piplite.install(["seaborn", "lxml", "openpyxl"])

import pandas as pd

from pyodide.http import pyfetch

file_name = "www.google.com"

async def download(url, file_name):
    res = await pyfetch(url)
    if res.status == 200:
        with open(file_name, "wb") as f:
            f.write(await res.bytes())

await download(file_name, "example.csv");

df = pd.read_csv("example.csv", header=None)

# add columns name csv
df.columns = ['First Name', 'Last Name', 'Location ', 'City','State','Area Code']

# select one column
df["First Name"]

# select multiple column
df[["First Name", "Last Name"]]

# select row use iloc or loc
df.loc[0]

# dump json (create file (write))
person = {
    "name": "vono",
    "age": 23,
    "exp": {
        "d": 0,
        "a": 1
    }
}
with open("person.json", "w") as f:
    json.dump(person, f)