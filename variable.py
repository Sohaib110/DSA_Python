
#Variable Declaration
a=10
print(a)
b=10.5
print(b)
c="Hello"
print(c)
d=True
print(d)

#Swapping of two numbers
a=10
b=25
print("Before Swapping: ")
print("a=",a, "b=",b)

#First Method
a,b=b,a
#Second Method
temp=a
a=b
b=temp

print("After Swapping: ")
print("a=",a, "b=",b)