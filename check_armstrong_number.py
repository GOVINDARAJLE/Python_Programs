# Program to check if a number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initalize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp>0:
    digit = temp % 10 
    sum +=digit**3
    temp //=10

# display the result 
if num == sum:
    print(num,"is an Armstrong Number")
else:
    print(num,"is not an Armstrong Number")

# End of program

# output
# Enter a number: 153
# 153 is an Armstrong Number
# Enter a number: 12
# 12 is not an Armstrong Number
