count =0
n=int(input('Enter a Number:'))
for i in range(1,n+1):
    if n%i ==0:
        count+=1
if count==2:
    print(n,"is a Prime Number")
else:
    print(n,"is Not a prime Number")