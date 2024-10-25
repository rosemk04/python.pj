'''
Author: Rose Mary Mathew
Date:25/10/2024
Discription:program to find the largest of three numbers.
The program should take three numbers as input from the user and determine which one is the largest.
Use conditional statements to compare the numbers.
'''

num1=int(input("Enter first number "))
num2=int(input("Enter the second number "))
num3=int(input("Enter the third number"))
if(num1>num2 and num3<num1):
    print(num1,"is greater")
elif num2>num1 and num2>num3:
    print(num2,"is greater")
else:
    print(num3,"is greater")
