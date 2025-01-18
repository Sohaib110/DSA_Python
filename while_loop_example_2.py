# Program to find the sum of digits in given Numbers using while loop

num = int(input("Enter the number: "))
sum = 0
while (num>0):
    d= num%10
    sum = sum + d
    num = num//10
print("Sum of Digits",sum)