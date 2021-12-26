# program to check if a number is an Armstrong number or not
# taking the input from the user

num = int(input("Enter a number: "))

#initializing sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# display the result
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")

# Output:
# Enter a number: 153
# 153 is an Armstrong number
# Enter a number: 12
# 12 is not an Armstrong number
# Enter a number: 0
# 0 is not an Armstrong number
