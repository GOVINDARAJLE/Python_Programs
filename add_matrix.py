# program to add tow matrix using nested loop

# take the two matrix input from the user
first_matrix = []
second_matrix = []

# fou the size of the matrix
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

for i in range(rows):
    first_matrix.append([])
    for j in range(columns):
        first_matrix[i].append(int(input("Enter the element: ")))

for i in range(rows):
    second_matrix.append([])
    for j in range(columns):
        second_matrix[i].append(int(input("Enter the element: ")))

# add the two matrix
result = []
for i in range(rows):
    result.append([])
    for j in range(columns):
        result[i].append(first_matrix[i][j] + second_matrix[i][j])
    
# print the result
print("The result is: ")
for i in range(rows):
    for j in range(columns):
        print(result[i][j], end = " ")
    print()
    