# program to find the factor of a number 

# define the function for the factor of a number

def print_factors(x):
    print("The factors of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

# take the input from the user
num = int(input("Enter a number: "))

# print the result
print_factors(num)
