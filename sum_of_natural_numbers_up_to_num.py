# program to find the sum of natural numbers up to a given number

# take the input from the user 
num = int(input("Enter the number: "))


if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
