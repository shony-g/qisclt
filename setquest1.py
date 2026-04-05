""" Section 1 – Basic Set Programs"""

""" 1. Create a set containing 5 numbers and print the set."""

# set1=set(range(1,6))
# print(set1)

# set2 = {3,4,5,6,7,3,4,5}

# print(set2)

""" 2. Create a set with mixed data types and print each element."""

# set1 = {3,10.5,"shony",(1980,True), False}

# for x in set1:
#     print(type(x), x)

""" 3. Write a program to create a set from a list."""
# lst = [1,2,3,4,5,2,3,2,8]
# print (lst)
# set1 = set(lst)

# print(set1)

""" 4. Write a program to remove duplicate elements from a list using a set."""

# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]

# print(lst)

# lst= list(set(lst))

# print(lst)

""" 5. Create an empty set and add three elements to it."""

# set1 = set()

# for i in range(3):
#     a = input("Please enter a value:")
#     set1.add(a)

# print(set1)

""" 6. Write a program to check if an element exists in a set."""

# set1 = set(range(1,20))

# num = int(input("Which number you wanto check:"))

# print(num in set1)

""" 7. Create a set and print all elements using a for loop."""

# set1 = set(range(1,20))

# for x in set1:
#     print(x)

""" 8. Write a program to find the length of a set without using len()."""

# set1 = set(range(1,20))

# print(set1)

# count =0

# for x in set1:
#     count+=1

# print(f"{count} is the length of the set")

""" 9. Write a program to convert a tuple into a set."""

# tpl = tuple(range(1,8))

# print(tpl)

# set1 = set(tpl)

# print(set1)

""" 10. Write a program to convert a set into a list."""

# set1 = set(range(1,20))

# print (set1)

# lst = list(set1)

# print(lst)

""" Section 2 – Adding and Removing Elements"""

""" 11. Create a set and add a new element using add(). """
# set1 = set()

# for i in range(3):
#     a = input("Please enter a value:")
#     set1.add(a)

# print(set1)

""" 12. Write a program to add multiple elements to a set using update()."""

# set1 = {3,4,5,89,12,45}

# print(set1)

# set1.update((1,2,"priya"),"shony")

# print(set1)

""" 13. Write a program to remove an element using remove()."""

# set1 = set(range(1,20))
# print(set1)

# num= int(input("Which value to remove:"))

# set1.remove(num)

# print(set1)

""" 14. Write a program to remove an element using discard()."""

# set1 = set(range(1,20))
# print(set1)

# num= int(input("Which value to remove:"))

# set1.discard(num)

# print(set1)

""" 15. Write a program to remove a random element using pop()."""
# set1 = set(range(1,20))
# print(set1)

# set1.pop()

# print(set1)

""" 16. Write a program to clear all elements from a set."""
# set1 = set(range(1,20))
# print(set1)

# set1.clear()

# print(set1)

""" 17. Write a program to copy a set into another set."""
# set1 = set(range(1,20))
# print(set1)

# set2 = set1.copy()

# print(set2)

""" 18. Write a program to add elements from a list into a set."""

# set1 = {3,4,5,89,12,45}
# lst= [1,2,3]
# print(set1)
# print(lst)
# set1.update(lst)

# print(set1)

""" 19. Write a program to add elements from a tuple into a set."""

# set1 = {3,4,5,89,12,45}
# tpl= (1,2,3)
# print(set1)
# print(tpl)
# set1.update(tpl)

# print(set1)

""" 20. Write a program to update a set with another set."""

# set1 = {3,4,5,89,12,45}
# set2 = {10,20,30}
# print(set1)
# print(set2)
# set1.update(set2)

# print(set1)

""" Section 3 – Set Operations"""

""" 21. Write a program to find the union of two sets."""

# set1 = {3,4,5,89,12,45}
# set2 = {10,20,30}
# print(set1)
# print(set2)

# print(set1 | set2)

""" 22. Write a program to find the intersection of two sets."""

# set1 = {3,10,5,89,20,45}
# set2 = {10,20,30,5}
# print(set1)
# print(set2)

# print(set1 & set2)

""" 23. Write a program to find the difference between two sets."""
# set1 = {3,10,5,89,20,45}
# set2 = {10,20,30,5}
# print(set1)
# print(set2)

# print(set1 - set2)

""" 24. Write a program to find the symmetric difference between two sets."""
# set1 = {3,10,5,89,20,45}
# set2 = {10,20,30,5}
# print(set1)
# print(set2)

# print(set1 ^ set2)

""" 25. Write a program to update a set using intersection_update()."""
# set1 = {3,10,5,89,20,45}
# set2 = {10,20,30,5}
# print(set1)
# print(set2)
# set1&=set2
# print(set1)

""" 26. Write a program to update a set using difference_update()."""
# set1 = {3,10,5,89,20,45}
# set2 = {10,20,30,5}
# print(set1)
# print(set2)
# set1-=set2
# print(set1)

""" 27. Write a program to update a set using symmetric_difference_update()."""

# set1 = {3,10,5,89,20,45}
# set2 = {10,20,30,5}
# print(set1)
# print(set2)
# set1^=set2
# print(set1)

""" 28. Write a program to check if one set is a subset of another set."""
# set1 = {3,10,5,89,20,45}
# set2 = {10,20,30,5}
# print(set1)
# print(set2)
# print(set1.issubset(set2))

""" 29. Write a program to check if one set is a superset of another set."""
# set1 = {3,10,5,89,20,45}
# set2 = {10,20,30,5}
# print(set1)
# print(set2)
# print(set1.issuperset(set2))

""" 30. Write a program to check if two sets are disjoint."""
# set1 = {3,5,89,45}
# set2 = {10,20,30,}
# print(set1)
# print(set2)
# print(set1.isdisjoint(set2))

""" 
Section 4 – Logical Set Problems
31. Write a program to find common elements between two lists using sets.
32. Write a program to find unique elements from two lists.
33. Write a program to find elements present in the first list but not in the second list.
34. Write a program to remove duplicates from a sentence using sets.
35. Write a program to find unique characters in a string using sets.
36. Write a program to count unique words in a sentence.
37. Write a program to find the difference between two strings using sets.
38. Write a program to find vowels present in a string using sets.
39. Write a program to check whether two strings contain the same characters.
40. Write a program to find common characters between two strings.
Section 5 – Set Comprehension
41. Write a program to create a set of squares from numbers 1–10 using set
comprehension.
42. Write a program to create a set of cubes using set comprehension.
43. Write a program to create a set of even numbers from 1–20 using set comprehension.
44. Write a program to create a set of odd numbers using set comprehension.
45. Write a program to create a set containing lengths of words in a sentence."""

""" Section 4 – Logical Set Problems"""