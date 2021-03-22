s1=input("Enter a string to check palindrome:")
s2=""
for i in s1:
    s2=i+s2
if(s1==s2):
    print("this is a palindrome ")
else:
    print("This is Not a palindrome")
