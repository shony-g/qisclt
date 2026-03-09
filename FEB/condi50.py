""" 1. Write a program to check if a number entered by the user is even or odd. """

# num1=int(input("Please enter a number:"))

# if num1%2==0:
#     print("Even number")
# else:
#     print("Odd number")

""" 2. Create a script that asks for a person's age and prints if they are eligible to vote (18+)."""

# num1=float(input("Please enter your age:"))

# if num1>17:
#     print(f"You are eligible for vote")
# else:
#     print(f"You are not eligible for vote")

""" 3. Write an if-statement to check if a number is positive, negative, or zero."""

# num1=int(input("Please enter the first number:"))

# if num1<0:
#     print("You have entered a negative number")
# else:
#     if num1==0:
#         print("You have entered zero")
#     else:
#         print("You have entered a positive number")

""" 4. Compare two numbers and print the larger one."""

# num1=int(input("Please enter the first number:"))
# num2=int(input("Please enter the second number:"))

# if num1<num2:
#     print(f"{num2} is larger")
# else:
#     print(f"{num1} is larger")

""" 5. Check if a given year is a leap year."""

# num1=int(input("Please enter the year:"))

# if num1%4==0:
#     print(f"{num1} is leap year")
# else:
#     print(f"{num1} is not a leap year")

"""" 6. Write a program to check if a character is a vowel or consonant."""

# char = input("Please enter a character:")

# if 64 < ord(char) < 91:
#     if char=="A" or char=="E" or char=="I" or char=="O" or char=="U":
#         print(" You have entered a vowel")
#     else:
#         print(" You have entered a consonant")
# elif 96 < ord(char) < 123:
#     if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
#         print(" You have entered a vowel")
#     else:
#         print(" You have entered a consonant")
# else:
#     print("Not a alphabet")

""" 7. Accept a number and check if it is a multiple of both 3 and 5."""

# num1=int(input("Please enter a number:"))

# if num1%15==0:
#     print(f"{num1} is divisible by both 3 and 5")
# else:
#     print(f"{num1} is not divisible by both 3 and 5")

""" 8. Check if a string entered by the user is empty or not."""

# str1=input("Please enter a string:")

# if str1=="":
#     print(f"{str1} is NULL")
# else:
#     print(f"{str1} is not NULL")

""" 9. Write a program to find the largest of three numbers using only if-else."""

# num1=int(input("Please enter the first number:"))
# num2=int(input("Please enter the second number:"))
# num3=int(input("Please enter the third number:"))

# if num1<num2 and num3<num2:
#     print(f"{num2} is larger")
# elif num2<num1 and num3<num1:
#     print(f"{num1} is larger")
# else:
#     print(f"{num3} is larger")

""" 10. Check if a given number lies within the range 10 to 50 (inclusive)."""

# num1=int(input("Please enter a number:"))

# if 10<num1<51:
#     print(f"within the range 10 to 50")
# else:
#     print("Not within the range 10 to 50")

""" 11. Grade Calculator: Input marks (0-100). A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60."""

# num1=float(input("Please enter your mark in 100:"))

# if num1>89:
#     print("A Grade")
# elif num1>79:
#     print("B Grade")
# elif num1>69:
#     print("C Grade")
# elif num1>59:
#     print("D Grade")
# else:
#     print("Fail")


""" 12. Check if a triangle is equilateral, isosceles, or scalene based on three side inputs."""

# a=float(input("Please first side of the triangle:"))
# b=float(input("Please Second side of the triangle:"))
# c=float(input("Please Third side of the triangle:"))

# if (a+b>c) and (a+c>b) and (b+c>a):
#     if a==b==c:
#         print(" The triangle is equilateral")
#     elif a==b or b==c or a==c:
#         print("The triangle is isosceles")
#     else:
#         print("The triangle is scalene")
# else:
#     print("Not a valid traingle")

""" 13. Write a program to check if a single character is uppercase, lowercase, or a digit."""

# char=input("Please enter a charactor:")

# if 64<ord(char)<91:
#     print("You have entered a upper case letter")
# elif 96<ord(char)<123:
#     print("You have entered a lower case letter")
# elif 47<ord(char)<58:
#     print("You have entered a digit")
# else:
#     print("You have entered not a  uppercase, lowercase, or a digit")

""" 14. Authenticate a user: Prompt for username and password. Print "Access Granted" only if both match."""
# u_name = input("Please enter username:")
# u_pass = int(input("Please enter the password:"))

# if u_name=="admin" and u_pass==1234:
#     print("Login sucessfull")
# else:
#     print("Please verify username and password")

""" 15. Calculate the Profit or Loss based on Cost Price and Selling Price."""
# a=int(input("Please enter the cost of the product:Rs"))
# b=int(input("Please enter the selleing price of the product:Rs"))
# profit=b-a
# if profit<0:
#     print("The product sell with loss and the loss is: Rs",profit*-1,"/-")
# else:
#     print("The profit is :Rs",profit,"/-")

""" 16. Determine the quadrant of a coordinate point (x, y)."""
# x=float(input("Please enter 'x' coordinate :"))
# y=float(input("Please enter 'y' coordinate :"))

# if x>0:
#     if y>0:
#         print("first quadrant point")
#     elif y<0:
#         print("fourth quadrant point")
#     else:
#         print("point on x axis")
# elif x<0:
#     if y>0:
#         print("second quadrant point")
#     elif y<0:
#         print("Third quadrant point")
#     else:
#         print("point on x axis")
# else:
#     if y!=0:
#         print("point on y axis")
#     else:
#         print("point on Orgin")

""" 17. Check if a number is a three-digit number."""
# num1=int(input("Please enter a number:"))

# x=len(str(num1))

# if x==0:
#     print(" You have enterd a three digit number")
# else:
#     print("Not a three digit number")

""" 18. Write a program that takes a month number (1-12) and prints the number of days in that month. """

# num1=int(input("Please enter a month number:"))

# if num1==2:
#     print("28 days in normal year and 29 days in leap year")
# elif num1 in (1,3,5,7,8,10,12):
#     print("31 days")
# elif num1 in (4,6,9,11):
#     print("30 days")
# else:
#     print("Not a valid number")

""" 19. Given three angles, determine if they can form a valid triangle (sum = 180)."""
# a=float(input("Please first angle of the triangle:"))
# b=float(input("Please Second angle of the triangle:"))
# c=float(input("Please Third angle of the triangle:"))

# x=a+b+c
# if x==180:
#     print("it is a valid triangle")
# else:
#     print("Not a triangle")

""" 20. Check if a number is divisible by 7 but not a multiple of 5."""

# num1=int(input("Please enter a number:"))

# if num1%7==0:
#     if num1%5==0:
#         print("Divisible by 7 and multiple of 5")
#     else:
#         print("divisible by 7 but not a multiple of 5")
# else:
#     print("Not divisible by 7 and 5")

""" 21. Implement a simple calculator (+, -, *, /) using if-elif-else."""

# a=float(input("Please enter first number:"))
# b=float(input("Please enter second number:"))
# c=input("Please enter the oprator:")

# if c=='+':
#     print(f"{a} + {b} = {a+b}")
# elif c=='-':
#     print(f"{a} - {b} = {a-b}")
# elif c=='*':
#     print(f"{a} * {b} = {a*b}")
# else:
#     if b==0:
#         print("Division is not applicable")
#     else:
#         print(f"{a} * {b} = {a/b}")

"""

22. Check if a given string starts with a capital letter and ends with a period.
23. Determine if a person is a Senior Citizen (60+), Adult (18-59), or Minor (<18).
24. Write logic to find the second largest number among three unique inputs.
25. Check if a list provided by a user has more than 5 elements. """

""" Check if a given string starts with a capital letter and ends with a period."""

# char = input("Please enter a string:")

# a = ord (char[0])
# print(a)

# for i in char:
#     b=i
# endflag = False
# startflag = False

# if ord(b)==46:
#     endflag= True
# else:
#     endflag=False

# if 64<a<91:
#     startflag=True
# else:
#     endflag=False

# if endflag and startflag:
#     print ("Condition satisfied")
# else:
#     print("not applicable")


""" 24. Write logic to find the second largest number among three unique inputs."""

# a=float(input("Please first :"))
# b=float(input("Please Second :"))
# c=float(input("Please Third :"))

# if (a>b and c>a) or (b>a and a>c):
#     print(f"{a}")
# elif (b>a and c>b) or (b<a and b>c):
#     print(f"{b}")
# else:
#     print(f"{c}")