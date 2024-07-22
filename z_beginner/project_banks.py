import pandas as pd
import sqlite3
from bs4 import BeautifulSoup
import requests
import datetime
import numpy as np

url = "https://en.wikipedia.org/wiki/List_of_largest_banks"
csv_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv"
attribute_column = ["Name", "MC_USD_Billion"]
name_csv = "./Largest_banks_data.csv"
db_name = "Banks.db"
table_name = "Largest_banks"
log_file = "code_log.txt"
response = requests.get(url)

def extract():
    df = pd.DataFrame(columns = attribute_column)
    if response.status_code == 200:
        res = BeautifulSoup(response.text, 'html.parser')
        table = res.find_all("table")
        rows = table[2].find_all("tr")
        # img = table[2].find_all("img")

        for row in rows:
            col = row.find_all("td")

            if len(col) != 0:
                data_dict = {
                    "Name": col[1].text.strip(),
                    "MC_USD_Billion": col[2].text.strip(),
                }

                df1 = pd.DataFrame(data_dict, index = [0])
                df = pd.concat([df, df1], ignore_index = True)
        return df;
    else:
        log_process("url is failure")
        print("Check url again!")
        
        
def transform(df, csv_path):
    data = pd.read_csv(csv_path)
    exchange_rate = pd.Series(data.Rate.values, index = data.Currency).to_dict()
    df['MC_USD_Billion'] = pd.to_numeric(df['MC_USD_Billion'], errors = "coerce")
    df['MC_GBP_Billion'] = np.round(df['MC_USD_Billion'] * exchange_rate['GBP'], 2)
    df['MC_EUR_Billion'] = np.round(df['MC_USD_Billion'] * exchange_rate['EUR'], 2)
    df['MC_INR_Billion'] = np.round(df['MC_USD_Billion'] * exchange_rate['INR'], 2)


    return df

    
def load_to_csv(df):
    df.to_csv(name_csv)

def load_to_db(df, sql_connect, table_name):
    df.to_sql(table_name, sql_connect, if_exists = 'replace', index = False)

def run_query(query, conn):
    query_output = pd.read_sql(query, conn)
    print(query_output)


def log_process(message):
    now = datetime.datetime.now()
    time = now.strftime('%Y-%m-%dT%H:%M:%S')
    with open(log_file, 'a') as f:
        f.write(time + ',' + message + "\n")

conn = sqlite3.connect(db_name)

try:
    log_process("RUN ETL")
    log_process("Extract started")
    raw_data = extract()    
    log_process("Extracted end")

    log_process("Transform started")
    transformed = transform(raw_data, csv_path)
    log_process("Transform end")

    log_process("Loaded csv started")
    load_to_csv(transformed)
    log_process("Loaded csv end")

    log_process("Loaded to database started")
    load_to_db(transformed, conn, table_name)
    log_process("Loaded to database end")

    log_process("Query started")
    run_query(f"SELECT * FROM {table_name}", conn)
    run_query(f"SELECT AVG(MC_GBP_Billion) FROM {table_name}", conn)
    run_query(f"SELECT Name from {table_name} LIMIT 5", conn)
    log_process("Query end")

except Exception as e:
    print('Check error: ', e)
finally:
    conn.close()

