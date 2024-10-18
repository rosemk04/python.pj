'''
Author: Rose Mary
Date:18-10-24
Discription:program that demonstrates the usage of arithmetic,
comparison, and logical operators.
'''
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num_sum=num1+num2
num_division=num1/num2
print("Sum",num_sum,"Division",num_division)
print("Is number 1 greater than number 2?",num1>num2)
print("Are number 1 and number 2 equal?",num1==num2)
print("Logical AND: ",num1>0 and num2>0)
print("Logical OR :" ,num1<0 or num2>0)

