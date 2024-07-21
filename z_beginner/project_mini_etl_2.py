import pandas as pd
from bs4 import BeautifulSoup
import sqlite3
import requests as rq


url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = "/dev/z_beginner/movies.db"
table_name = "Movies_tb"
csv_path = "/dev/z_beginner/top_50.csv"
df = pd.DataFrame(columns = ["Film", "Year", "Rotten Tomatoes' Top 100"])
count = 0

html_page = rq.get(url).text
data = BeautifulSoup(html_page, "html.parser")

table = data.find_all("table")
rows = table[0].find_all("tr")

for row in rows:
    if count < 25:
        col = row.find_all("td")

        if len(col) != 0:
            data_dict = {
                "Film": col[1].contents[0],
                "Year": col[2].contents[0],
                "Rotten Tomatoes' Top 100": col[3].contents[0]
            }

            df1 = pd.DataFrame(data_dict, index = [0])
            df = df.concat([df, df1], ignore_index = True)
    else:
        break


print(df)

df.to_csv(csv_path)

conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists = 'replace', index = False)
conn.close()

