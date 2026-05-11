""" 40. Write a program to shuffle elements in a list."""
# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]
# import random

# print(lst)

# random.shuffle(lst)

# print(lst)

""" 41. Write a program to find the kth largest element in a list."""

# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]
# print(lst)

# num = int(input(" K th largest, please input K:"))

# lst2 = list(set(lst))

# lst2.sort()

# print(f"the {num}th largest is :{lst2[-1*num]}")

""" 42. Write a program to check whether a list is a palindrome."""

# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]
# print(lst)

# num = len(lst)//2
# flag = True
# for i in range(num):
#     if lst[i]!=lst[len(lst)-i-1]:
#         flag=False
#         break
# if flag:
#     print("palindrome")
# else:
#     print("Not a palindrome")

# lst2 = lst[::-1]
# if lst==lst2:
#     print("palindrome")
# else:
#     print("Not a palindrome")

""" 43. Write a program to generate all possible pairs from a list."""

# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]
# print(lst)

# lst2 = [(lst[i],lst[j]) for i in range(len(lst)) for j in range(i+1, len(lst))]

# print(lst2)

""" 45. Write a program to remove all negative numbers from a list."""

# num = int(input(" Please enter the range:"))

# lst=[x for x in range(1,num) if x/num !=0 for num in range(2,int(x**0.5))]

# print(lst)

# lst = [1 ,2,5,8,-1,5,-3,9,-8]

# s=[]

# for x in lst:
#     if x >=0:
#         s.append(x)

# print(s)

""" 
Section 4: Logical / Problem Solving
44. Create a list of prime numbers within a given range using list comprehension.
46. Given a list of numbers, move all zeros to the end while maintaining order.

49. Find all pairs whose sum equals a given target value.
50. Write a program to detect duplicates in a list.
51. Given two lists, determine whether they contain the same elements regardless of order.
52. Write a program to partition a list into even and odd numbers.
53. Implement bubble sort using lists.
54. Implement selection sort using lists.
55. Write a program to remove consecutive duplicate elements."""

""" 47. Find the first non-repeating element in a list."""

# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]
# print(lst)


# for x in lst:
#     if lst.count(x) ==1:
#         print(f"{x} is the first non repeating element in a list")
#         break

""" 48. Find the highest frequency element in a list."""

# my_List = input("Enter values seerated by space:").split()
# lst =[int(x) if x.isdigit() else x for x in my_List]
# print(lst)

# a=0
# b=0

# for x in lst:
#     if lst.count(x)>a:
#         b=x
#         a=lst.count(x)

# print(f"highest frequency {a} element in a list is {b}")

"""pract"""
# data = [(1,5),(3,2),(4,8)]

# datadic = dict(data)

# print(datadic)

# keyDataSort = sorted(datadic,key=datadic.get)

# # print(keyDataSort)

# findic = {x:datadic[x] for x in keyDataSort}

# print(findic)

# finlst = list(findic.items())

# print(finlst)

# samMatri= [[1,2,3],[4,5,6],[7,8,9]]

# s1= 0
# print('Matrix:')
# for x in samMatri:
#     for y in x:
#         print(y, end=" ")
#         s1+=y
#     print()
# print()
# print()
# print(f"Sum:{s1}")

# tpl = (1,2,3,2,4,2)

# rtol = tpl[::-1]
# print(rtol)
# print(tpl.count(2))

# lst =[1,2,{3,4}]
# print(lst)
# tup1 = (1,2,{3,4})
# print(tup1)
# set1 = {1,2,{3,4}}
# print(set1)

# nameset = {'koni','moni','soni'}
# # nameset.add(('aani','sani'))
# nameset.update( {'quni', 'gani'})

# print(nameset)