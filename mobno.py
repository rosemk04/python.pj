'''
Author:Rose Mary
Description:Program to check whether the given number is a valid mobile number or not using functions.
'''
def mobile_number(number):
    number_length=len(number)
    if number_length==10:
        if number[0] in ["7","8","9"]:
            print("Valid mobile number")
    else:
        print("Invalid mobile number")
number=input("Enter mobile number: ")
mobile_number(number)


