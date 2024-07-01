def triangle(numRows):
      # Initialize a 2D array with zeros
    triangle = [[0] * (i + 1) for i in range(numRows)]
    

    for i in range(numRows):
        triangle[i][0] = 1  # First element of each row is 1
        triangle[i][i] = 1  # Last element of each row is 1
        
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    
    return triangle
    
        


print(triangle(5))