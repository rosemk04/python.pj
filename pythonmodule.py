'''
Author: Rose Mary
Date:18-10-24
Discription:program that uses functions from the math module to perform the
following operations on a number provided by the user:
    Find the square root.
    Calculate the factorial.
    Raise the number to the power of 2.
'''
import math
num1=int(input("Enter a number "))
math_sqrt=math.sqrt(num1)
print("square root of",num1,":",math_sqrt)
num_factorial=math.factorial(num1)
print("Factorial of",num1,":",num_factorial)
num_power=math.pow(num1,2)
print(num1,"raised to power 2: ",num_power)
