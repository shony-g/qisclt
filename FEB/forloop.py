""" 1.  Write a program to print numbers from 1 to 10 using a for loop."""

# for i in range(1,11,1):
#     print(i)

""" 2.  Write a program to print numbers from 1 to 20 using range()."""

# for i in range(1,21,1):
#     print(i)

""" 3.  Write a program to print even numbers from 1 to 50."""

# for i in range(2,51,2):
#     print(i)

""" 4.  Write a program to print odd numbers from 1 to 50."""

# for i in range(1,51,2):
#     print(i)

""" 5.  Write a program to print numbers from 10 to 1 in reverse order."""

# for i in range(10,0,-1):
#     print(i)

""" 6.  Write a program to print the multiplication table of a given number."""

# num1=int(input("Please enter the number for multiplication table:"))
# for i in range(1,11,1):
#     print(f"{i} X {num1} = {i*num1}")

""" 7.  Write a program to find the sum of numbers from 1 to N."""

# num1=int(input("Please enter the number upto do sum (N):"))
# s=0
# for i in range(1,num1+1,1):
#     s+=i
# print(f"{s}")

""" 8.  Write a program to find the factorial of a number."""

# num1=int(input("Please enter the number to find factorial:"))
# fact =1
# for i in range(1,num1+1,1):
#     fact*=i
# print(f"{fact}")

""" 9.  Write a program to print the square of numbers from 1 to 10."""

# for i in range(1,11,1):
#     print(i*i)

""" 10. Write a program to print the cube of numbers from 1 to 10."""

# for i in range(1,11,1):
#     print(i**3)

""" 11. Write a program to count numbers from 1 to 100."""

# for i in range(1,101,1):
#     print(i)

""" 12. Write a program to print all multiples of 3 between 1 and 50."""

# for i in range(3,51,3):
#     print(i)

""" 13. Write a program to print numbers divisible by both 2 and 5 between 1 and 100."""

# for i in range(10,101,10):
#     print(i)

""" 14. Write a program to print characters of a string using a for loop."""

# name1 = input("Please enter your name:")

# for val in name1:
#     print(val)

""" 15. Write a program to count the number of characters in a string."""

# name1 = input("Please enter a word or sentence:")
# i=0
# for val in name1:
#     i+=1
# print(i)

""" 16. Write a program to count vowels in a string."""

# name1 = input("Please enter a word or sentence:")
# incre=0
# for val in name1:
#     if val=="a" or val=="e" or val=="i"  or val=="o" or val=="u" or val=="A" or val=="E" or val=="I" or val=="O" or val=="U": 
#         incre+=1
# print(incre)

""" 17. Write a program to print numbers from N to 1."""

# num1=int(input("Please enter a number:"))

# for i in range(num1,0,-1):
#     print(f"{i}")

""" 18. Write a program to find the sum of even numbers from 1 to 100."""

# s=0
# for i in range(1,101,1):
#     s+=i
# print(f"{s}")

""" 19. Write a program to find the sum of odd numbers from 1 to 100."""

# s=0
# for i in range(1,101,2):
#     s+=i
# print(f"{s}")

""" 20. Write a program to print the first 10 natural numbers."""

# for i in range(1,11,1):
#     print(i)

""" 21. Write a program to print numbers from 1 to 100 with a step of 5."""

# for i in range(5,101,5):
#     print(i)

""" 22. Write a program to print the following pattern:-    ** """

# for i in range(1,101,1):
#     print("**")

""" 23. Write a program to print the following pattern: 1 12 123 1234 12345"""

# accu=0
# for i in range(1,6,1):
#     accu = 10*accu + i
#     print(accu, end=" ")

""" 24. Write a program to check whether a number is prime or not."""

# num1=int(input("Please enter a number:"))

# count = 0
# for i in range(1,num1+1,1):
#     if num1%i==0:
#         count+=1
# if count<3:
#     print(f"{num1} is a prime number!!! ")
# else:
#     print(f"{num1} not a prime number!!!")

"""  25. Write a program to print Fibonacci series up to N terms. """

# num1=int(input("How many Fibonacci series numbers needed? :"))
# x = 1
# y = 0
# print(y, end=" ")

# for i in range(1,num1,1):
#     z = x + y
#     x = y
#     y = z
#     print(z, end=" ")


# num1=int(input("How many Fibonacci series numbers needed? :"))
# x = 1
# y = 0
# print(y, end=" ")

# for i in range(1,num1,1):
#     z = x + y
#     x = y
#     y = z
#     print(z, end=" ")

""" print prime number up to"""

# num1=int(input("Please enter a number :"))

# a= num1

# for x in range(2,a+1):
#     for i in range (2,x):
#         if x%i==0:
#             break
#     else:
#         print(x)

"""" rivers name"""
# nam = input("Please enter your name:")

# a= nam
# ult = ""

# for i in a:
#     ult = i + ult

# print(ult)

""" perfect squre of a number"""

# x = int(input(" Please enter a number:"))
# a = x
# b = x**0.5
# c = int(b)
# if c*c == a:
#     print(" Perfect square")
# else:
#     print("Not a perfect square")





