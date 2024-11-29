'''Author: Rose Mary
Description:A program that accepts the lengths of three sides of a triangle as inputs.
'''
def is_right_triangle():
    a=int(input("Enter hypotenuse side: "))
    b=int(input("Enter second side: "))
    c=int(input("Enter third side: "))
    if a*a==b*b+c*c:
        print("It is right triangle")
    else:
        print("It is not right triangle")

is_right_triangle()
