#program to display the power of number using anonymous function

# take input from the user
n = int(input("Enter the number: "))
terms = int(input("Enter the terms: "))


# use anonymous function
result = list(map(lambda x: n ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])