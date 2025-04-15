import psycopg2
import pandas as pd

def create_database():
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=mysecretpassword")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    try:
        # Terminate all active connections to the 'accounts' database
        cur.execute("""
            SELECT pg_terminate_backend(pid)
            FROM pg_stat_activity
            WHERE datname = 'accounts' AND pid <> pg_backend_pid();
        """)

        # Drop and recreate the 'accounts' database
        cur.execute("DROP DATABASE IF EXISTS accounts")
        cur.execute("CREATE DATABASE accounts")
    except Exception as e:
        print(f"Error during database creation: {e}")
    finally:
        cur.close()
        conn.close()

    # Reconnect to the newly created 'accounts' database
    conn = psycopg2.connect("host=localhost dbname=accounts user=postgres password=mysecretpassword")
    cur = conn.cursor()
    return cur, conn


def create_tables(cur, conn):
    create_accounts_country_table = ("""
        CREATE TABLE IF NOT EXISTS accountsCountry(
            country_code VARCHAR PRIMARY KEY,
            short_name VARCHAR,
            table_name VARCHAR,
            long_name VARCHAR,
            currency_init VARCHAR
        )
    """)

    create_accounts_data_table = ("""
        CREATE TABLE IF NOT EXISTS accountsData(
            country_name VARCHAR,
            country_code VARCHAR,
            indicator_name VARCHAR,
            indicator_code VARCHAR,
            year_95 NUMERIC,
            year_2000 NUMERIC,
            year_05 NUMERIC,
            year_10 NUMERIC,
            year_14 NUMERIC
        )
    """)

    create_accounts_series_table = ("""
        CREATE TABLE IF NOT EXISTS accountsSeries(
            series_code VARCHAR PRIMARY KEY,
            topic VARCHAR,
            indicator_name VARCHAR,
            long_definition VARCHAR
        )
    """)

    try:
        cur.execute(create_accounts_country_table)
        cur.execute(create_accounts_data_table)
        cur.execute(create_accounts_series_table)
        conn.commit()
    except Exception as e:
        print(f"Error creating tables: {e}")


def insert_data(cur, conn):
    # Use ON CONFLICT to handle duplicate primary key insertion
    insert_accounts_country = ("""
        INSERT INTO accountsCountry (country_code, short_name, table_name, long_name, currency_init)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (country_code) DO NOTHING;
    """)

    insert_accounts_series = ("""
        INSERT INTO accountsSeries (series_code, topic, indicator_name, long_definition)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT DO NOTHING;
    """)

    # Insert into accountsCountry
    for _, row in accountsCountryClean.iterrows():
        try:
            cur.execute(insert_accounts_country, (row['Code'], row['Short Name'], row['Table Name'], row['Long Name'], row['Currency Unit']))
        except Exception as e:
            print(f"Error inserting data: {e}")

    # Insert into accountsSeries
    insert_accounts_series = ("""
        INSERT INTO accountsSeries (series_code, topic, indicator_name, long_definition)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT DO NOTHING;
    """)

    for _, row in accountsSeriesClean.iterrows():
        try:
            cur.execute(insert_accounts_series, list(row))
        except Exception as e:
            print(f"Error inserting data: {e}")
    conn.commit()


# Load and clean data
accountsCountry = pd.read_csv("./data/Wealth-AccountsCountry.csv")
accountsCountryClean = accountsCountry[['Code', 'Short Name', 'Table Name', 'Long Name', 'Currency Unit']]

accountsData = pd.read_csv("./data/Wealth-AccountData.csv")
accountsData = accountsData.drop(['2018 [YR2018]'], axis=1)

accountsSeries = pd.read_csv("./data/Wealth-AccountSeries.csv")
accountsSeriesClean = accountsSeries[['Code', 'Topic', 'Indicator Name', 'Long definition']]

# Create database and tables
cur, conn = create_database()
create_tables(cur, conn)
insert_data(cur, conn)

cur.close()
conn.close()
