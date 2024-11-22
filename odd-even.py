'''Author: Rose Mary
Description: Input two lists from user.Merge these lists into a third list such that in the merged list,
all even numbers occur first followed by odd numbers.Both the even numbers and odd numbers should be in order.
'''
list1=[38,67,44,33,28,68,48]
list2=[77,58,16,35,25,47,66]
combined_list=list1+list2
even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
print("Even numbers: ",even_list)
odd_list.sort()
print("Odd numbers: ",odd_list)
print("Final list")
merged_list=even_list+odd_list
print(merged_list)