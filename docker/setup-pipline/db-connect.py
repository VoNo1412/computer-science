import psycopg2

pgpassword = ""
conn = None

try:
    conn = psycopg2.connect(
        user = 'postgres',
        password = pgpassword,
        host = 'postgres',
        port = 5432,
        database = 'postgres'
    )
except Exception as e:
    print("Error connect to data warehouse")
    print(e)
else:
    print("Successfully connected to data warehouse")
finally:
    if conn:
        conn.close()
        print("Connected closed!!!")