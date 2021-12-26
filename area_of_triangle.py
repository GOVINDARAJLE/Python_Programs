# program calculate the area of trangle
# taking the input  a b c from the user

a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))

# calculate the semi-perimeter
s=(a+b+c)/2

#calculate the area of triangle
area= (s*(s-a)*(s-b)*(s-c))**0.5

#print the area of triangle
print("the area of trangle of {0} {1} {2} is {3}".format(a,b,c,area))

# End of program
# @author: GOVINDA RAJLE

