def diagonal_traverse(mat):
    row = len(mat);
    col = len(mat[0]);

    result = [];
   
    for s in range(row + col - 1):
        if s % 2 == 0:
            print(min(s, row - 1), max(-1, s - col), row)
            for i in range(min(s, row - 1), max(-1, s - col), -1):  ## min(2), max(0), -1
                  result.append(mat[i][s - i])
        else:
            for i in range(max(0, s - col + 1), min(row, s + 1)): ## max(1), min(3)
                  result.append(mat[i][s - i])
    return result;


print(diagonal_traverse([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
