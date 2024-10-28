"""
Author: Rose Mary
Date:28-10-2024
Discription:program that allows users to convert temperatures
between Celsius and Fahrenheit
"""
while True:
    print("1.\tConvert Celsius to Fahrenheit")
    print("2.\tConvert Fahrenheit to Celsius")
    print("3.\tExit")
    choice=int(input("Enter you choice: "))
    if choice==1:
        temp = float(input("Enter temperature: "))
        c=(temp-32)* 5/9
        print("The temperature: ",c)
    elif choice==2:
        tem=float(input("Enter temperature: "))
        f=(tem+32)*9/5
        print("The Temperature: ",f)
    elif choice==3:
        break
    else:
        print("Invalid Entry")



