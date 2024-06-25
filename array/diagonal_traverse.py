def checkDiagonal(num):
    k = 0;
    m = n = len(num) - 1;
    arr = []

    for k in range(m):
        i = k;
        j = 0;

        while i >= 0:
            arr.append(num[i][j])
            i -= 1;
            j += 1;

    for k in range(n + 1):
        i = m;
        j = k;
    
        while j <= m :
            arr.append(num[i][j])
            i -= 1;
            j += 1;
    return arr;


print(checkDiagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

