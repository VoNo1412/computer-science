# Create matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

def createMatrix():
    row = int(input("Enter the number of rows: "));
    column = int(input("Enter the number of columns: "))

    #initialize matrix
    matrix = [];

    print("Enter the entries row wise: ");

    for row in range(row):
        a = [];
    
        for column in range(column):
            a.append(int(input()))
        
        matrix.append(a);
    
    return matrix;

print(createMatrix())


# List Slicing

Lst(initial : end : index jump)
ex: Lst[::]

    # Initialize list
    List = [20, 30, 40]

    # Show original list
    print("Original List:\n", List)

    print("\nSliced Lists: ")

    # Display sliced list
    print(List[3:9:2])

    # Display sliced list
    print(List[::2])

    # Display sliced list
    print(List[::])


# List comprehension
    Syntax: newList = [ expression(element) for element in oldList if condition ] 
    
    
    numbers = [12, 13, 14,] 
    doubled = [x *2  for x in numbers] 
    print(double)

    matrix = [[j for j in range(4)] for i in range(3)] 
    
    print(matrix)