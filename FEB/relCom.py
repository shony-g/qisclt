"""16. Write a program to check if a user-input number is even or odd."""

# num1=int(input("Please enter a number:"))
# if num1%2==0:
#     print("The number is EVEN")
# else:
#     print("The number is ODD")

""" 17. Compare two strings entered by the user and print which one comes first alphabetically."""

# str1=input("Please enter first name:")
# str2=input("Please enter second name:")
# print(str1,str2)

"""18. Check if a given year is a leap year using comparison and logical operators."""

# year=int(input("Please enter a year:"))
# if year%4==0:
#     print("Leap year")
# else:
#     print("Not a leap year")

""" 19. Take two numbers and print True if the first is greater than the second, else False."""

# num1=int(input("Please enter the first number:"))
# num2=int(input("Please enter the Second number:"))

# if num1>num2:
#     print("True")
# else:
#     print("False")

""" 20. Determine if a student passed or failed based on a passing mark of 40."""

# num1=int(input("Please enter the mark:"))
# if num1>=40:
#     print("Pass")
# else:
#     print("Fail")

""" 21. Compare a float and an integer (e.g., 5.0 == 5). Explain the result."""

# num1=int(input("Please enter the int number:"))
# num2=float(input("Please enter the float number:"))
# print(num1==num2)
# print(type(num1), type(num2))
# print(num1 is num2)
# print(" False bebacuse both not sharing same memory location.")

""" 22. Check if a number is a perfect square."""
# num1=int(input("Please enter a number less than 100:"))

# if num1==1 or num1==4 or num1==9 or num1==16 or num1==25 or num1==36 or num1==49 or num1==64 or num1==81 or num1==100:
#     print("Perfect square")
# else:
#     print("Not a perfect square")


""" 23. Write a program to find the largest of three numbers using comparison operators."""

# a=int(input("Please enter the first number:"))
# b=int(input("Please enter the second number:"))
# c=int(input("Please enter the third number:"))

# if a>b and a>c:
#     print(f"{a} is the larger number")
# else:
#     if b>a and b>c:
#         print(f"{b} is the larger number")
#     else:
#         print(f"{c} is the larger number")

""" 24. Check if a character entered by the user is an uppercase letter."""

# char=input("Please enter a character:")
# if 64<ord(char)<91:
#     print(" Upper case letter")
# else:
#     if 96<ord(char)<122:
#         print("Smaller case letter")
#     else:
#         print("Not a valid input")

""" 25. Validate if a triangle is valid given three angles (Sum must be exactly $180$)."""

# a=float(input("Please enter the first angle:"))
# b=float(input("Please enter the second angle:"))
# c=float(input("Please enter the third angle:"))
# sum = a + b + c
# if sum==180:
#     print("it is a perfect raingle")
# else:
#     print("Not a traingle")

"""26. Check if a number is divisible by both 3 and 5. """

# a=int(input("Please enter a number:"))
# if a%15==0:
#     print("The number is divisible by both 3 and 5")
# else:
#     print("The number is not divisible by both 3 and 5")

""" 27. Write a program to check if a number is between 10 and 50 (inclusive)."""

# a=int(input("Please enter a number:"))
# if 10<a<50:
#     print("Inclusive")
# else:
#     print("Not inclusive")

""" 28. Create a login logic: Check if username == "admin" AND password == "1234"."""
# u_name = input("Please enter username:")
# u_pass = int(input("Please entaer the password:"))

# if u_name=="admin" and u_pass==1234:
#     print("Login sucessfull")
# else:
#     print("Please verify username and password")

""" 29. Use the not operator to reverse a boolean result of a comparison."""

# num1=int(input("Please enter the first number:"))
# num2=int(input("Please enter the second number:"))
# print(f"{num1} not equeal to {num2}",num1!=num2 )

""" 30. Determine if a person is eligible to vote (Age  18$ AND has a Voter ID)."""

# age=int(input("Please enter the your age:"))

# if age>18:
#     print(" you are eligible for voting")
# else:
#     print("Your are not eligible for voting")

""" 31. Check if a number is either positive OR even."""

# num1=int(input("Please enter a number:"))

# if num1>0:
#     print("The number is positive.")
#     if num1%2==0:
#         print(f"{num1} is a even number.")
#     else:
#         print(f"{num1} is a odd number.")
# else:
#     print("The number is negative.")
#     if num1%2==0:
#         print(f"{num1} is a even number.")
#     else:
#         print(f"{num1} is a odd number.")

""" 32. Demonstrate "Short-circuit evaluation" using and where the first condition is False."""
# x=2
# y=1

# if x>5 and x/y>1:
#     print(" This is never going to print as the first condtion fails")
# else:
#     print("this will print as Short-circuit evaluation")

""" 33. Write a program that checks if a character is a vowel using the or operator."""

# char = input("Please enter a character:")

# if char=="a" or char=="e" or char=="i" or char=="o" or char=="u" or char=="A" or char=="E" or char=="I" or char=="O" or char=="U":
#     print(" You have entered a vowel")
# else:
#     print("Not a vowel")

""" 34. Check if a number is NOT divisible by 7."""

# num1=int(input("Please enter a number:"))

# if num1%7==0:
#     print("Divisible by 7")
# else:
#     print("Not divisible by 7")
""" 35. Combine and, or, and not in a single expression to evaluate a complex condition."""

# num1=int(input("Please enter a number:"))

# if (num1%2==0 and num1!=0) or (num1-1)!=0:
#     print (" not one")
# else:
#     print("one")