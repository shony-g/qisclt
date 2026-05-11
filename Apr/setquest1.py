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

""" Section 4 – Logical Set Problems"""

""" 31. Write a program to find common elements between two lists using sets."""
# lst1= [1,2,3,4,5,6,7]
# lst2 = [4,5,6,7,8,9,10]

# lst3 = set(lst1).intersection(set(lst2))
# print(lst3)

""" 32. Write a program to find unique elements from two lists."""

# lst1= [1,2,3,4,5,6,7]
# lst2 = [4,5,6,7,8,9,10]
# print(lst1)
# print(lst2)

# lst3 = set(lst1).symmetric_difference(set(lst2))
# print(lst3)

""" 33. Write a program to find elements present in the first list but not in the second list."""

# lst1= [1,2,3,4,5,6,7]
# lst2 = [4,5,6,7,8,9,10]
# print(lst1)
# print(lst2)

# lst3 = set(lst1).difference(set(lst2))
# print(lst3)

""" 34. Write a program to remove duplicates from a sentence using sets."""

# str1 =" hare rama hare rama rama rama hare hare"
# str2= str1.split()
# print(str2)
# set1 = set(str2)
# print(set1)

""" 35. Write a program to find unique characters in a string using sets."""

# str1 =" I love you"
# print(str1)
# set1 = set(str1)
# print(set1)

""" 36. Write a program to count unique words in a sentence."""

# str1 =" hare rama hare rama rama rama hare hare"
# str2= str1.split()
# print(str2)
# set1 = set(str2)
# print(len(set1))

""" 37. Write a program to find the difference between two strings using sets."""

# str1 = "shony gangadharan"
# str2 = "Priyanka shony"

# set3= set(str1)-set(str2)

# print(set3)

""" 38. Write a program to find vowels present in a string using sets."""
# str1 = "shony gangadharan"
# set1= set("AEIOUaeiou")
# set2 = set1 & set(str1)
# print(set2)

""" 39. Write a program to check whether two strings contain the same characters."""

# str1 = "welcome"
# str2 = "melcowe"
# print(str1, str2)

# if set(str1)==set(str2):
#     print("Two strings contain the same characters")
# else:
#     print("Two strings contain NOT same characters")


""" 40. Write a program to find common characters between two strings."""

# str1 = "shony gangadharan"
# set1= "Priyanka shony"
# set2 = set(set1) & set(str1)
# print(set2)

""" Section 5 – Set Comprehension"""

""" 41. Write a program to create a set of squares from numbers 1–10 using set comprehension."""

# set1 = {x**2 for x in range(1,11)}
# print(set1)

""" 42. Write a program to create a set of cubes using set comprehension."""
# set1 = {x**3 for x in range(1,11)}
# print(set1)

""" 43. Write a program to create a set of even numbers from 1–20 using set comprehension."""

# set1 = {x for x in range(1,21) if x%2==0}
# print(set1)

""" 44. Write a program to create a set of odd numbers using set comprehension."""

# set1 = {x for x in range(1,21) if x%2!=0}
# print(set1)

""" 45. Write a program to create a set containing lengths of words in a sentence."""

# str1="aana alrodu alararal aana kuthi"
# lst= str1.split()
# print(lst)
# set1=set()
# for x in lst:
#     set1.add(len(x))

# print(set1)