# Program for Armstrong number in Python
# print all Armstrong numbers between num1 and num2

# take the Num1 and Num2 from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# main logic
for num in range(num1,num2+1):
    #order of number 
    order = len(str(num))
    sum = 0

    temp = num
    while temp>0:
        digit = temp % 10
        sum += digit**order
        temp //=10
    if num == sum:
        print(num)
        