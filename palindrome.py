str=input("Enter the string to check Palindrome:")
str =str.casefold()
if str==str[::-1]:
    print("This is a Palindrome")
else:
    print("This is a not palindrome")
    
