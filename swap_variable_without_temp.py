# swap the numbers without using a temporary variable

# take the input from the user of x and y

x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))

# print the values of x and y
print("The value of x is {0} and the value of y is {1}".format(x, y))

# swap the values of x and y
x = x+y
y = x-y
x = x-y

# print the values after swapping

print("The value of x after swapping is:", x)
print("The value of y after swapping is:", y)
