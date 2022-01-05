# program to transpose a matrix using a nested loop

# take inout from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# transpose the matrix
transpose = []
for i in range(cols):
    transpose.append([])
    for j in range(rows):
        transpose[i].append(0)
    
for i in range(rows):
    for j in range(cols):
        transpose[j][i] = input("Enter the element: ")

# print the transpose matrix
print("The transpose matrix is: ")
for i in range(cols):
    for j in range(rows):
        print(transpose[i][j], end = " ")
    print()

        