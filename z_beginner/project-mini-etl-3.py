import pandas as pd
import sqlite3

db_name = "departments.db"
table_name = "departments"
attribute_list = ["DEPT_ID", "DEP_NAME", "MANAGER_ID", "LOC_ID"]
file_path = "/dev/z_beginer/department.csv"

conn = sqlite3.connect(db_name)
df = pd.read_csv(file_path, names = attribute_list)
df.to_sql(table_name, conn, if_exists = 'replace', index = False)

query_statement = f"select * from {table_name}"
query_output = pd.read_sql(query_statement, conn)

print("output: ", query_output)

data_dict = {
    "DEPT_ID": [9],
    "DEP_NAME": ["vono"]
}

data_append = pd.DataFrame(data_dict)
data_append.to_sql(table_name, conn, if_exists = 'append', index = False)

query_output = pd.read_sql(query_statement, conn)
print("output after append: ", query_output)

