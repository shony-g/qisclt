""" 36. Create two lists with the same elements and use is to check their identity. Explain the result."""
# ls1 = "apple mango orange"
# ls2 = "apple mango orange"
# print (ls1 is ls2)

""" 37. Create two strings with the same value and check identity. Compare this to the list result."""
# str1 = "shonygangadharan"
# str2 = "shonygangadharan"
# print (str1 is str2)

""" 38. Use in to check if a specific fruit exists in a list of fruits."""
# ls1 = "apple mango orange"
# print ("mango" in ls1)
# print ("jackfruit" in ls1)
# print ("Mango" in ls1)

""" 39. Write a program to check if a specific substring exists within a sentence."""

# ls1 = "Hello!!! my name is Shony Gangadharan, i am from kozhikode Kerala"
# print ("i am" in ls1)

""" 40. Use is not to compare two different object types (e.g., a list and a tuple)."""

# ls1 = "apple mango orange"
# ls2 = "apple mango orange"
# ls3 = "apple mango jack fruit"
# ls4 = "apple mango Orange"
# print (ls1 is not ls2)
# print (ls1 is not ls3)
# print (ls1 is not ls4)

""" 41. Check if a key exists in a dictionary using the in operator."""
""" 42. Use not in to verify a username is NOT already in a list of banned users."""

# u_banned = "admin abc efg Admin user"
# new_uname = input("Please enter the username:")

# if new_uname not in u_banned:
#     print ("Login sucessfull")
# else:
#     print("Login failed")

""" 43. Demonstrate how is behaves when one variable is assigned to another (e.g., a = b)."""

# num1 = 10
# num2 = 10

# print(num1 is num2, " num1 is num2 If true means the both variable sharing the same memory location")
# num1 = num2
# print(num1, num2, " num1 = num2 means assiging the value of num1 to num2")
# print(num1== num2, " num1== num2 If true means the both the variable have the same value")

""" 44. Check if the digit '5' is present in the range of 1 to 10."""
# for i in range (1,11,1):
#     if i==5:
#         print(f"{i} is the rage of 1 to 10")
# print("Thank you")

""" 45. Compare the speed/result of == vs is for large integer values."""

# num1 = 8585858585885858858585
# num2 = 8585858585885858858585

# print(num1 is num2)
# print(num1== num2)
""" I feel is is fater than =="""

"""" 46. The Range Checker: Take a number and check if it’s outside the range 100-200."""
# num1 = int(input(" Please enter a number:"))

# for i in range (100,201,1):
#     if i==num1:
#         print(f"{i} is the rage of 100 to 200")
# print("Thank you")

""" 47. Quadratic Formula: Solve for $x$ in $ax^2 + bx + c = 0$ using arithmetic operators"""

# print(" Please enter valuses of x, a, b to find the value of c in expression $ax^2 + bx + c = 0$")
# x= int(input("Please enter value of x:"))
# a= int(input("Please enter value of a:"))
# b= int(input("Please enter value of b:"))
# c=-(a*x**2+b*x)
# print (c)

""" 48. Multiple Comparisons: Write a single expression to check if $a < b < c$ (Chained operators)."""

# a= int(input("Please enter value of a:"))
# b= int(input("Please enter value of b:"))
# c= int(input("Please enter value of c:"))

# if a<b<c:
#     print (f"{c} > {b} > {a}")
# elif b<c<a:
#     print (f"{a} > {c} > {b}")
# elif c<a<b:
#     print (f"{b} > {a} > {b}")
# elif a<c<b:
#     print (f"{b} > {c} > {a}")
# elif b<a<c:
#     print (f"{c} > {a} > {b}")
# elif c<b<a:
#     print (f"{a} > {b} > {c}")
# else:
#     print("some numbers are equel")

""" 49. Shopping Discount: Apply a 10% discount using *= only if the total is above $500."""

# a= float(input("Please enter total bill:"))
# if a>499:
#     a-=0.1*a
#     print(f"Total bill:{a}")
# else:
#     print(f"Total bill:{a}")

""" 50. Bit-like logic with Math: Determine the last digit of a number without using strings."""

# a= int(input("Please enter a number:"))
# b=a%10
# print(f"The last digit of the number is {b}")
