arr=[]
num=int(input('Enter Number Elements:'))
for n in range(num):
    number=int(input('Enter Number:'))
    arr.append(number)
print('Max element in the list is :',max(arr))
print('Min element in the list is :',min(arr))
