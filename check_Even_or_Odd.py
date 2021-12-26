# Program to check the number is Even or Odd

# take the input from the user

num = int(input("Enter the Number: "))

# check the given number is a Even or odd number

if num % 2 == 0:
    print("The Number {0} is a Even Number".format(num))
else:
    print("The Number {0} is a Odd Number".format(num))

# output:
# Enter the Number: 5
# The Number 5 is a Odd Number
