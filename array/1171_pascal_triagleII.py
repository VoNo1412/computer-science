def getRow(rowIndex):
    row = [1]
    for i in range(1, rowIndex + 1):
        row.append(row[-1] * (rowIndex - i + 1) // i)

    return row

print(getRow(3))