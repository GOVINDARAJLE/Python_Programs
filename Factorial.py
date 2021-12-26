# program to find the factorial of a number

# take the input from the user

num = int(input("Enter a number: "))
factorial = 1

# calculate the factorial
for i in range(1, num + 1):
    factorial = factorial * i

# print the factorial of the number
print("The factorial of", num, "is", factorial)
