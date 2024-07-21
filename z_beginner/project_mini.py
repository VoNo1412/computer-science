# extract all countries their GDP's in billion USDs(round 2 decimal places)
# add data into sources: json, database
# query database >= 100 economy
# log entries process excution in a file "etl_project_log.txt"

# pandas, sqlite3, beautifulSoup, reqeuest, json, datetime

import pandas as pd
import sqlite3
import requests
import json
from bs4 import BeautifulSoup
import datetime

url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
response = requests.get(url)
db_name = "world_usd.db"
table_name = "money_table"
target_json = "/dev/z_beginner/money_json.json"
logger_txt = "/dev/z_beginner/logger_money.txt"
conn = sqlite3.connect(db_name)

# Step 1: Extract data from url web
def extract_data():
    if response.status == 200:
        data = BeautifulSoup(response.text, "html.parser")
        attribute_list = ["Country", "GDP_USD_billion"]
        df = pd.DataFrame(columns = attribute_list)
        table = data.find("table", {"class": "wikitable"})
        rows = table.find_all("tr")
        for row in rows:
            col = row.find_all("td")
            if len(col) != 0:
                data_dict = {
                    "Country": col[0].text.strip(),
                    "GDP_USD_billion": col[2].text.strip() ## IMF dollar
                }
                df1 = pd.DataFrame(data_dict, index = [0])
                df = pd.concat([df, df1],  ignore_index = True)

        return df;
    else:
        logger_money("Failed to retrieve data from the URL")
        return;

# Step 2: Transform Data
def transform_data(df):
    df = df.drop(index = 0)
    df["GDP_USD_billion"] = round(df["GDP_USD_billion"].replace(',', '', regex=True).apply(pd.to_numeric, errors='coerce').fillna(0), 2)
    return df;

# Step 3: Loaded data into json, database, logger data
def loaded_data(df):
    df.to_json(target_json, orient="records")
    df.to_sql(table_name, conn, if_exists = 'replace', index = False)

def logger_money(message):
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%dT%H:%M:%S')

    with open(logger_txt, 'a') as f:
        f.write(date + "," + message + "\n")

# Step 4: Query Data
def query_database():
    query_statement = f"select * from {table_name} where GDP_USD_billion > 100"
    query_output = pd.read_sql(query_statement, conn)

    print("result_query: ", query_output)


try:
    logger_money("RUN ETL")
    logger_money("Extracted start")
    raw_data = extract_data()
    raw_data = None
    logger_money("Extracted end")
    logger_money("Transformed start")
    transformed_data = transform_data(raw_data)
    # print("transformed: ", transformed_data)
    logger_money("Transformed end")
    logger_money("Loaded start")
    loaded_data(transformed_data)
    logger_money("Loaded end")
    logger_money("DONE ETL")

    logger_money("Query started")
    query_database()
    logger_money("Query end")
except Exception as e:
    logger_money(f"ETL process failed: {e}")
    print('Raw data not exists')
finally:
    conn.close()

