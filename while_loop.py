#Count the digits in Given Number

n = int(input("Enter the number: "))
count = 0
while(n>0):
    count = count + 1
    n = n//10
print("Count of digits in the given number is: ",count)
    