'''
Author: Rose Mary
Date:19-10-24
Discription: Create, concatenate, and print a string and access a sub-string from a given string.
Program that performs the following tasks:
Create two separate strings:
The first string should contain your first name.
The second string should contain your last name.
Concatenate the two strings with a space in between and store the result in a new variable.
Print the concatenated string.
From the concatenated string:
Access and print a sub-string that consists of the last name only. Use string slicing to extract the sub-string.
'''
first_name=input("Enter your firstname: ")
last_name=input("Enter your lastname: ")
name=first_name+" "+last_name
print (name)
first_name_length=len(first_name)
extracted_last_name=name[first_name_length+1:]
print (first_name_length)
print(extracted_last_name)
