# program to multiplay the two matrix using nested loop

# take the two matrix input from the user
first_matrix = []
second_matrix = []

# fou the size of the matrix
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the Number of columns: "))

# take the two matrix input from the user
for i in range(rows):
    first_matrix.append([])
    for j in range(cols):
        first_matrix[i].append(int(input("Enter the element: ")))
    
for i in range(rows):
    second_matrix.append([])
    for j in range(cols):
        second_matrix[i].append(int(input("Enter the element: ")))

# multiplay the two matrix
result = []
for i in range(rows):
    result.append([])
    for j in range(cols):
        result[i].append(0)
        for k in range(cols):
            result[i][j] += first_matrix[i][k] * second_matrix[k][j]

# print the result
print("The result is: ")
for i in range(rows):
    for j in range(cols):
        print(result[i][j], end = " ")
    print()
    