""" -- PART 1: BASICS & INITIALIZATION ---"""

""" 1. Create a tuple containing five different data types (int, float, string, list, boolean)."""

# tpl = (5,10.01,"shony",[1,5,3],True,(3,9))

# print(tpl)

""" 2. Write a script to check the type of a tuple with a single element. Show the difference
between (5) and (5,)."""

# tpl1 = (5)
# tpl2 = (5,)

# print(f"type of (5) is {type(tpl1)}and type of (5,) is {type(tpl2)}")

""" 3. Access the last element of a tuple without knowing its length."""

# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]
# tpl = tuple(lst)

# print(tpl)

# print(f"The last element is: {tpl[-1]}")

""" 4. Access the second to last element of a tuple using negative indexing."""

# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]
# tpl = tuple(lst)

# print(tpl)

# print(f"The second last element is: {tpl[-2]}")

""" 5. Given nested_tuple = ("Python", [10, 20, 30], (5, 15, 25)), print the number 20."""

# nested_tuple = ("Python", [10, 20, 30], (5, 15, 25))

# print(nested_tuple[1][1])

""" 6. Check if the element 'Sreeraj' exists in a tuple using a membership operator."""

# my_List = input("Enter names seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]
# tpl = tuple(lst)


# if "Sreeraj" in tpl:
#     print("Sreeraj included")
# else:
#     print("Not inculded")

""" 7. Find the memory size of a list vs. a tuple with the same elements using the sys module."""

# my_List = input("Enter names seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]
# tpl = tuple(lst)

# import sys

# print(f"memory size of list {lst} is {sys.getsizeof(lst)}")
# print(f"memory size of list {tpl} is {sys.getsizeof(tpl)}")

""" 8. Unpack a tuple of 3 elements into three variables: x, y, and z."""

# tpl = (5,6,7)
# print(tpl)
# x,y,z = tpl

# print(x,y,z)
""" 9. Demonstrate what happens if you try to unpack a tuple of 4 elements into 3 variables."""

# tpl = (5,6,7,8)
# print(tpl)
# x,y,z = tpl

# print(x,y,z)

""" 10. Use the 'extended iterable unpacking' (using *) to grab the first element and the rest into a
list."""

# tpl = (5,6,7,8)
# print(tpl)

# *x,y,z = tpl
# print (f"*x,y,z is:",x,y,z)

# x,*y,z = tpl
# print (f"x,*y,z is:",x,y,z)

# x,y,*z = tpl
# print (f"x,y,*z is:",x,y,z)

""" --- PART 2: IMMUTABILITY LOGIC ---"""

""" 11. Write code that attempts to change the first element of a tuple and handle the resulting
TypeError gracefully."""

# tpl = (5,6,7,8)
# print(tpl)

# tpl[0]=0

# print(tpl)

""" 12. Given a tuple: t = (1, 2, [3, 4]). Change the value 3 to 30. Explain why this works despite
tuples being immutable."""

# t = (1, 2, [3, 4])

# print(t)

# t[2][0]=30

# print(t, " changed because nested item is a list.")

""" 13. Create two tuples, concatenate them, and assign them to a new variable."""

# t = (1, 2, [3, 4])
# tpl = (5,6,7,8)
# print(t)
# print(tpl)

# s = t + tpl

# print(s)

""" 14. Use the repetition operator (*) to create a tuple of ten zeros."""

# t=(0,)
# tpl = t*10

# print(t)
# print(tpl)

""" 15. Swap two variables a and b using tuple unpacking logic in a single line."""

# tpl = (5,6,7)
# print(tpl)

# x,y,z = tpl
# print("x,y,z",x,y,z)
# x,y = y,x
# print("x,y,z",x,y,z)

""" 16. Write a program to "add" an item to a tuple by converting it to a list first."""
# tpl = (5,6,7)
# print(tpl)

# lst = list(tpl)
# lst.append(8)
# tpl =tuple(lst)

# print(tpl)

""" 17. Write a program to "remove" an item from a tuple."""

# tpl = (5,6,7,8,9,1,4,2,5,8)
# print(tpl)

# num = int (input("Which item need to remove:"))

# ind = tpl.index(num)

# t = tpl[:ind] + tpl[ind +1:]

# print(t)

""" 18. Delete an entire tuple variable from memory and verify its absence using a try-except block."""
# tpl = (5,6,7,8,9,1,4,2,5,8)
# print(tpl)

# del tpl
# try:
#     print(tpl)
# except NameError:
#     print(" Name NameError")

""" 19. Sort a tuple of integers and return the result as a new tuple."""

# tpl = (5,6,7,8,9,1,4,2,5,8)
# print(tpl)

# lst = list(tpl)
# lst.sort()
# tpl2 = tuple(lst)

# print(tpl2)

""" 20. Reverse a tuple using the slicing method [::-1]."""

# tpl = (5,6,7,8,9,1,4,2,5,8)
# print(tpl)

# tpl2 = tpl[::-1]

# print(tpl2)

""" --- PART 3: METHODS & AGGREGATION ---"""

""" 21. Find the index of the first occurrence of the number 10 in a tuple."""

# tpl = (5,6,7,8,9,10,4,2,10,5,8)
# print(tpl)

# print(f"The inex of he first occurrence of the number 10 is:{tpl.index(10)}")\

""" 22. Count how many times the string "Python" appears in a tuple of job roles."""

# jd = ("Develop, test, and maintain robust server-side components using Python.", "Optimize existing applications by refactoring legacy code into efficient Python models.", "Design Python-based APIs and services to support frontend and mobile applications.")

# num = sum(1 for x in jd if "Python" in x)

# print(num)

""" 23. Find the maximum and minimum values in a tuple of stock prices."""

# tpl = (59,64,75,866,98,10,42,2,102,556,83)
# print(tpl)

# a = max(tpl)
# b = min (tpl)

# print(f"max is:{a} and min is{b}")

""" 24. Calculate the sum of all numeric elements in a tuple."""

# tpl = (5,6,7,8,9,10,4,2,10,5,8)
# print(tpl)

# s= sum(tpl)

# print(s)

""" 25. Given a tuple of tuples: ((1, 2), (3, 4), (5, 6)), calculate the sum of the second element of each internal tuple."""

# tpl = ((1, 2), (3, 4), (5, 6))

# tpl2 = []

# for x in tpl:
#     print(x)
#     s=sum(x)
#     tpl2.append(s)
# tpl2=tuple(tpl2)
# print(tpl2)

""" 26. Use the index() method to find the position of 'Apple' starting from index 3 in a large fruit tuple."""

# fruits = ("mango","apple","Thenga","Orange","mango","Thenga","Thenga","Orange","mango","Orange","apple","mango","apple","Orange","Orange","Thenga")

# num= fruits.index("apple",3)

# print(num)

""" 27. Write a function that takes a tuple and returns a new tuple containing only the even numbers."""

# tpl = range(1,20)
# print(tpl)
# tpl2 =tuple (x for x in tpl if x%2==0)

# print(tpl2)

""" 28. Convert a list of tuples into a single flat list."""

# tpl = ([1,2],4,5,[7,8,9,0])

# print(tpl)
# s= []

# for x in tpl:
#     if type(x)==list:
#         for y in x:
#             s.append(y)
#     else:
#         s.append(x)

# print(s)

""" 29. Create a tuple from a user-input string where each character is an element."""

# tpl = tuple(input("Please enter the strings:"))

# print(tpl)

""" 30. Check if all elements in a tuple are truthy using the all() function."""

# my_List = input("Enter names seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]
# tpl = tuple(lst)
# print(tpl)

# if all(tpl):
#     print(" All elements are truthy")
# else:
#     print("Some elements are falsy")

""" --- PART 4: SLICING & LOOPING ---"""

""" 31. Extract a sub-tuple containing the elements from index 2 to 5 (inclusive)."""

# tpl = (5,6,7,8,9,10,4,2,10,5,8)
# print(tpl)

# tpl2 = tpl[2:6]

# print(tpl2)

""" 32. Use slicing to get every second element of a tuple."""

# tpl = (5,6,7,8,9,10,4,2,10,5,8)
# print(tpl)

# tpl2 = tpl[::2]

# print(tpl2)

""" 33. Write a 'for' loop to print each element of a tuple with its corresponding index number."""

# tpl = (5,6,7,8,9,10,4,2,10,5,8)
# print(tpl)

# for x,y in enumerate(tpl):
#     print(f"{x} is the index and value is {y}")

""" 34. Use a 'while' loop to iterate through a tuple backwards."""

# tpl = (5,6,7,8,9,10,4,2,10,5,8)
# print(tpl)

# num = len(tpl)

# while num > 0:
#     print(tpl[num-1])
#     num-=1

""" 35. Create a tuple of 10 numbers and slice it to get the last 3 elements."""


# tpl = (5,6,7,8,9,10,4,2,10,5,8)
# print(tpl)

# tpl2 = tpl[-3:]

# print(tpl2)

""" 36. Slice a tuple to remove the first and last elements."""

# tpl = (5,6,7,8,9,10,4,2,10,5,8)
# print(tpl)

# tpl2 = tpl[1:-1]
# print(tpl2)

""" 37. Use a for loop to concatenate all strings in a tuple into a single sentence."""

# tpl = ("I", "Love","You")

# for x in tpl:
#     print(x, end=" ")

""" 38. Compare two tuples (1, 2, 3) and (1, 2, 4). Explain the logic of how Python compares them."""
# tpl1 = (1, 2, 3)
# tpl2 = (1, 2, 4)

# print(tpl1<tpl2)

""" 39. Write a program to find duplicate elements in a tuple."""

# my_List = input("Enter value seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]
# tpl = tuple(lst)
# print(tpl)


# dupe = set ()

# for x in tpl:
#     if tpl.count(x)>1:
#         dupe.add(x)
        
# print(f"Duplicates{tuple(dupe)}")


""" 40. Zip two tuples together to create a list of coordinate pairs."""

# tpl1 = (1,2,3,5,7,8,8)
# tpl2 = (6,7,8,8,1,2,4)

# cordi = list(zip(tpl1, tpl2))

# print(cordi)
