# Python program to swap two variables
# @author: GOVINDA RAJLE
#!/usr/bin/env python3
# Path: swap_variables.py

# take input from the user of x and y

x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))

# print the values of x and y
print("The value of x is {0} and the value of y is {1}".format(x, y))

# creating a temporary variable to store the value of x
temp = x
x = y
y = temp

print("The value of x after swapping is:", x)
print("The value of y after swapping is:", y)
