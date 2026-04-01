""" 
Section 4: Logical / Problem Solving
46. Given a list of numbers, move all zeros to the end while maintaining order.
47. Find the first non-repeating element in a list.
48. Find the highest frequency element in a list.
49. Find all pairs whose sum equals a given target value.
50. Write a program to detect duplicates in a list.
51. Given two lists, determine whether they contain the same elements regardless of order.
52. Write a program to partition a list into even and odd numbers.
53. Implement bubble sort using lists.
54. Implement selection sort using lists.
55. Write a program to remove consecutive duplicate elements."""

""" ############ Section 1: Beginner Level ##########"""

""" 1. Create a list of five integers and print all elements using a for loop."""

# my_List = []

# print("Please enter 5 integers below")

# for i in range (5):
#     item = int(input("Please enter a integers:"))
#     my_List+= [item]

# print(my_List)

""" 2. Write a program to find the length of a list without using len()."""

# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]

# num1 = 0
# print(lst)

# for x in lst:
#     num1+=1

# print (f" The length of the string is {num1} ")

""" 3. Create a list of numbers and print the maximum and minimum values."""

# my_List = input("Enter integers seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]

# print (lst)

# print(f"The minimum value is  {min(lst)} and maximum value is {max(lst)}")

""" 4. Write a program to append a new element to a list entered by the user."""

# my_list = [2,10,"shony"]

# print(my_list)

# num1 = int(input("How many values are you going to input:"))

# for x in range(num1):
#     new = input("Please enthe the value :")
#     if new.isdigit():
#         my_list.append(int(new))
#     else:
#         my_list.append(new)

# print(my_list)

""" 5. Insert an element at a specific position in a list."""

# my_list = [2,10,"shony",1980, "Priya",101.2]

# print(my_list)

# num1 = int(input("Which position you want to add the value:"))
# new = input("Please enther the value :")

# if new.isdigit():
#     my_list.insert(num1,int(new))
# else:
#     my_list.insert(num1,new)

# print(my_list)

""" 6. Remove an element from a list using remove() and pop()."""

# my_list = [2,10,"shony",1980, "Priya",101.2]

# print(my_list)
# num1 = int(input("Remove using index press 1 or else any number:"))
# if num1==1:
#     num2 = int (input("Please enther the index:"))
#     my_list.pop(num2)
# else:
#     num3 = input("Please enter the value:")
#     my_list.remove(num3)

# print(my_list)

""" 7. Write a program to check whether a given element exists in a list."""

# my_list = [2,10,"shony",1980, "Priya",101.2]

# new_list = [str(x) for x in my_list]

# print(new_list)

# checkI = input("Which element you want to check?:")

# if checkI in new_list:
#     print(f"The elemet {checkI} is in the list")
# else:
#     print("The element not present")

""" 8. Reverse a list without using reverse()."""

# my_List = input("Enter integers seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]

# r_lst = []
# print(" The list you have entered")
# print(lst)

# # for i in range (len(lst),0,-1):
# #     r_lst.append(lst[i-1])

# for x in lst:
#     r_lst.insert(0,x)

# print(" The list in reverse")
# print(r_lst)

""" 9. Sort a list of numbers in ascending and descending order."""

# my_List = input("Enter integers seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]

# lst.sort()

# print(f"The list in ascending order {lst}")

# lst.sort(reverse=True)

# print(f"The list in descending order {lst}")

""" 10. Create a list of numbers and print only the even numbers."""

# my_List = input("Enter integers seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]

# even_lst = [x for x in lst if x%2==0]

# print (f"The list with even number is {even_lst}")

""" 11. Count how many times a specific element appears in a list."""

# my_List = input("Enter integers seerated by space:").split()

# print(my_List)

# checkI = input("Which element's count you want to check?:")

# lst = [x for x in my_List if checkI==x]

# print(f"There are {checkI} repeats {len(lst)} times.")

""" 12. Write a program to copy one list into another list."""

# my_list = [2,10,"shony",1980, "Priya",101.2]

# sec_list = my_list.copy()

# print(my_list)
# print(sec_list)

""" 13. Concatenate two lists using the + operator."""

# my_list = [2,10,"shony",1980, "Priya",101.2]
# sec_list = ["Deeraj",1,2,3,"Theja"]
# print(my_list)
# print(sec_list)

# my_list+=sec_list

# print(my_list)

""" 14. Repeat a list three times using the * operator."""

# my_list = [2,10,"shony",1980, "Priya",101.2]

# print(my_list)

# my_list*=3

# print(my_list)

""" 15. Demonstrate positive and negative indexing in a list."""

# my_list = [2,10,"shony",1980, "Priya",101.2]

# lst_len = len(my_list)

# print(my_list)

# print(f"Postive index using my_list [0] {my_list[0]} and my_list[-length] {my_list[-lst_len]}")

# print("Both are same")

""" ############## Section 2: Intermediate Level #####################"""

""" 16. Write a program to remove duplicates from a list."""

# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]

# for x in lst:
#     if lst.count(x) >1:
#         lst.remove(x)
# print(f"duplicate removed from {lst}")

# print(lst)

""" 17. Find the second largest element in a list."""

# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]

# a=0
# b=0

# for x in lst:
#     if x>a:
#         b=a
#         a=x
#     elif x>b and x!=a:
#         b=x

# print(lst)
# print(f"The second largest is {b}") 

# lst.sort()
# for i in range (-1,-1*len(lst),-1):
#     print(lst[i-1],lst[i])
#     if lst[i-1]<lst[i]:
#         a=lst[i-1]
#         break
   
# print(lst)
# print(f"The second largest is {a}")

""" 18. Write a program to rotate a list to the left by one position."""

# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]

# print(lst)

# # lst.append(lst[0])
# # lst.pop(0)
# # print(lst)

# lst = lst[1:] + [lst[0]]
# print(lst)

""" 19. Write a program to rotate a list to the right by one position."""

# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]
# print(lst)

# # lst = [lst[-1]] + lst[:-1]
# # print(lst)

# lst.insert(0,lst[-1])
# lst.pop()
# print(lst)

""" 20. Move a specific element (e.g., 50) to the first position of a list."""

# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]
# print(lst)
# num1 = input("Please enter which value you need to move:")
# if num1.isdigit():
#     num1=int(num1)
# lst.remove(num1)
# lst.insert(0,num1)
# print(lst)

""" 21. Create a list of squares of numbers from 1–10 using list comprehension."""

# lst = [x for x in range(1,11)]
# print(lst)

""" 22. Create a list containing only odd numbers from 1–50 using list comprehension."""

# lst = [x for x in range(1,50) if x%2!=0]
# print(lst)

""" 23. Write a program to merge two lists and remove duplicates."""

# my_List = input("Enter values seerated by space:").split()
# lst1 =[int(x) if x.isdigit() else x for x in my_List]

# sec_List = input("Enter values seerated by space:").split()
# lst2 =[int(x) if x.isdigit() else x for x in sec_List]

# print(lst1)
# print(lst2)

# lst3 = []

# for x in lst1:
#     if x not in lst3:
#         lst3.append(x)
# for x in lst2:
#     if x not in lst3:
#         lst3.append(x)

# print(lst3)

""" 24. Find the sum of all elements in a list without using sum()."""

# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]

# l_sum=0

# for x in lst:
#     l_sum+=x

# print(l_sum)

""" 25. Write a program to find common elements between two lists."""

# my_List1 = input("Enter values seerated by space:").split()
# lst1 =[int(x) if x.isdigit() else x for x in my_List1]

# my_List2 = input("Enter values seerated by space:").split()
# lst2 =[int(x) if x.isdigit() else x for x in my_List2]

# common = [x for x in lst1 if x in lst2]

# print(f"common elements are {common}")

""" 26. Write a program to split a list into two halves."""

# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]

# len = int(len(lst)/2)

# first_halve = lst[:len]
# second_halve = lst[len:]

# print(first_halve ,"\n", second_halve)

""" 27. Find the index of a given element without using index()."""

# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]

# print(lst)

# num = input("Please let us know which values index you want:")

# if num.isdigit():
#     num = int(num)

# for i in range (len(lst)):
#     if lst[i]==num:
#         break
# print(f"The index of value {num} is {i}")

""" 28. Write a program to flatten a nested list."""

# lst = [1,2,[4,5],7,2,[8,9,"shony"],"priya"]

# s=[]

# for i in lst:
#     if type(i)==list:
#         for x in i:
#             s.append(x)
#     else:
#         s.append(i)

# print(s)

""" 29. Create a program to find the frequency of each element in a list."""
# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]

# print(lst)

# for i in lst:
#     print(f"The count of {i} is {lst.count(i)} ")


""" 30. Reverse each element of a list of strings."""

# my_List = input("Enter strings seerated by space:").split()

# print(my_List)
# lst =[]

# for i in my_List:
#     i=i[::-1]
#     lst.append(i)

# print(lst)

""" Section 3: Advanced Level """

""" 31. Implement a matrix using nested lists and print it in matrix format.
32. Write a program to add two matrices using nested lists.
33. Write a program to transpose a matrix.
34. Flatten a 2D list into a single list using list comprehension.
35. Find the largest sublist length in a nested list.
36. Write a program to find the intersection of multiple lists.
37. Write a program to group list elements by their length (strings).
38. Implement a simple stack using a Python list.
39. Implement a queue using a Python list.
40. Write a program to shuffle elements in a list.
41. Write a program to find the kth largest element in a list.
42. Write a program to check whether a list is a palindrome.
43. Write a program to generate all possible pairs from a list.
44. Create a list of prime numbers within a given range using list comprehension.
45. Write a program to remove all negative numbers from a list."""

""" 44. Create a list of prime numbers within a given range using list comprehension."""



""" 45. Write a program to remove all negative numbers from a list."""

# lst = [1,2,3,-4,-6]

# print(lst)
# s=[x for x in lst if x>=0]

# print(s)