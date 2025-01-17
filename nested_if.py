#Find the Biggest of 2 numbers using nested if

a=int(input("Enter your marks: "))
b=int(input("Enter your marks: "))

if(a!=b):
    print("Both marks are not same")
    if(a>b):
        print("A is greater than B")
    else:
        print("B is greater than A")
else:
    print("Both marks are same")