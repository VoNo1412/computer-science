import psycopg2

# Create the database
def connectDB():
    try:
        global conn
        conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=mysecretpassword")
        print("Connected successfully!!")
    except psycopg2.Error as e:
        print("Cannot connect to the db postgres: ", e)
        return

    try:
        cursor = conn.cursor()
        conn.set_session(autocommit=True)  # Set autocommit to create the database
        cursor.execute("CREATE DATABASE postgres_beginner")
        cursor.close()
        print("Database created successfully!")
    except psycopg2.Error as e:
        print(e)  # If the database already exists, it will print the error
    finally:
        conn.close()  # Ensure the connection is closed

# Execute a query on the new database
def queryDB(query, action):
    try:
        # Reconnect to the new database
        global conn
        conn = psycopg2.connect("host=127.0.0.1 dbname=postgres_beginner user=postgres password=mysecretpassword")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()  # Ensure changes are committed
        print(f"{action} is successful!")

        
    except psycopg2.Error as e:
        print("Query error: ", e)
    finally:
        cursor.close()
        conn.close()

# Call the functions in the correct order
connectDB()

queryDB("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INT PRIMARY KEY, 
            name VARCHAR(50), 
            age INT, 
            gender VARCHAR(10), 
            subject VARCHAR(50), 
            marks INT
        )
        """, "Create table")

# queryDB("INSERT INTO students (student_id, name, age, gender, subject, marks) VALUES (1, 'vono', 1412, 'male', 'python', 22222)", "Insert data")

def logData():
    try:
        # Reconnect to the new database
        global conn
        conn = psycopg2.connect("host=127.0.0.1 dbname=postgres_beginner user=postgres password=mysecretpassword")
        cursor = conn.cursor()

        cursor.execute("select * from students")
        rows = cursor.fetchall()

        c = 0
        while c <= len(rows):
            print(rows)
            c+=1

    except psycopg2.Error as e:
        print("log error: ", e)
    finally:
        cursor.close()
        conn.close()

logData()
        


        


