from time import time, ctime

conn = None


# Check for nulls
def runDataQualityCheck(**options):
    print("*" * 50)
    print(ctime(time()))
    start_time = time()
    test_name = options.pop("testname")
    test = options.pop("test")
    print(f"Starting test with {test_name}")
    status = test(**options)
    print(f"Finish test {test_name}")
    print(f"Test passed {status}")
    end_time = time()
    options.pop("conn")
    print("Test parameter")
    for key, value in options.items():
        print(f"{key} = {value}")
    print()
    print("Durations : ", str(end_time - start_time))
    print(ctime(time()))
    print("*" * 50)
    return test_name, options.get("table"), options.get("column"), status

def checkForNulls(column, table, conn = conn):
    sql = f"Select count(*) from {table} where {column} is null"
    cursor = conn.cursor()
    cursor.execute(sql)
    row_count = cursor.fetchone()
    cursor.close()
    return bool(row_count)

# check min max
def checkForMinMax(column, table, minimum, maximum, conn = conn):
    sql = f"select count(*) from {table} where {column} < {minimum} or {column} > {maximum}"
    cursor = conn.cursor()
    cursor.execute(sql)
    row_count = cursor.fetchone()
    cursor.close()
    return not bool(row_count)


# Check for valid values
def checkForValidValues(column, table, valid_values = None, conn = conn):
    sql = f"select distinct({column}) from {table}"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    #print(result)
    actual_values = {x[0] for x in result}
    print(actual_values)
    status = [value in valid_values for value in actual_values]
    # print(status)
    cursor.close()
    return all(status)


# check for duplicatees
def checkDuplicateRow(column, table, conn = conn):
    sql = f"select count({column}) from {table} group by {column} having count({column}) > 1"
    cursor = conn.cursor()
    cursor.execute(sql)
    row_count = cursor.fetchone()
    cursor.close()
    return not bool(row_count)


