a=0
b=1
n=int(input('Enter number to generate fibonaci series:'))
print("fibi series:")
print("",a,"",b,end="")
for i in range(n):
    c=a+b
    a=b
    b=c
    print("",c);
    
