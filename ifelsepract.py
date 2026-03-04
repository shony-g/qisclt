""" 1.  Check Even or Odd Write a program to check whether a given number is even or odd. """

# num1=int(input("Please enter the first number:"))

# if num1%2==0:
#     print("Even number")
# else:
#     print("Odd number")

"""  2. Positive, Negative or Zero Write a program to check if a number is positive, negative or zero."""

# num1=int(input("Please enter the first number:"))

# if num1<0:
#     print("You have entered a negative number")
# else:
#     if num1==0:
#         print("You have entered zero")
#     else:
#         print("You have entered a positive number")

""" 3.  Find the Largest of Two Numbers Take two numbers from the user and print the larger one."""

# num1=int(input("Please enter the first number:"))
# num2=int(input("Please enter the second number:"))

# if num1<num2:
#     print(f"{num2} is larger")
# else:
#     print(f"{num1} is larger")

""" 4.  Find the Largest of Three Numbers Take three numbers and print the largest among them."""

# num1=int(input("Please enter the first number:"))
# num2=int(input("Please enter the second number:"))
# num3=int(input("Please enter the third number:"))

# if num1<num2 and num3<num2:
#     print(f"{num2} is larger")
# elif num2<num1 and num3<num1:
#     print(f"{num1} is larger")
# else:
#     print(f"{num3} is larger")

""" 5.  Check Eligibility to Vote Ask the user for their age and check if they are eligible to vote (18 or above)."""

# num1=float(input("Please enter your age:"))

# if num1>17:
#     print(f"You are eligible for vote")
# else:
#     print(f"You are not eligible for vote")

""" 6.  Pass or Fail Ask the user for their mark and print Pass if mark is 40 or above, otherwise Fail."""

# num1=float(input("Please enter your mark:"))

# if num1>39:
#     print(f"You have passed the exam")
# else:
#     print(f"You have failed the exam")

""" 7.  Grade System Input marks and display grade: 90+ : A 80-89 : B 70-79 : C 60-69 : D Below 60 : Fail"""

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

""" 8.  Leap Year Checker Input a year and check whether it is a leap year or not."""

# num1=int(input("Please enter the year:"))

# if num1%4==0:
#     print(f"{num1} is leap year")
# else:
#     print(f"{num1} is not a leap year")

""" 9.  Divisible by 5 and 11 Check whether a number is divisible by both 5 and 11."""

# num1=int(input("Please enter a number:"))

# if num1%55==0:
#     print(f"{num1} is divisible by both 5 and 11")
# else:
#     print(f"{num1} is not divisible by both 5 and 11")

""" 10. Check Character Type Input a character and check if it is a vowel or consonant."""

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

""" 11. Simple Login System Ask for username and password. If both are correct, print Login Successful, else Login Failed."""

# u_name = input("Please enter username:")
# u_pass = int(input("Please enter the password:"))

# if u_name=="admin" and u_pass==1234:
#     print("Login sucessfull")
# else:
#     print("Please verify username and password")

""" 12. Number Comparison Game Take two numbers. If first is greater print “First is greater”, else print “Second is greater”. """
# num1=int(input("Please enter the first number:"))
# num2=int(input("Please enter the second number:"))

# if num1<num2:
#     print(f"Second is greater")
# else:
#     print(f"First is greater")

""" 13. Check Temperature If temperature > 30 print Hot, if between 20 and 30 print Warm, else Cold."""

# num1=int(input("Please enter the room temperature:"))

# if num1>30:
#     print(f"Hot")
# elif 20<num1<30:
#     print(f"Warm")
# else:
#     print("Cold")

""" 14. Check Salary Bonus If salary > 50000, give bonus 5000 else bonus 2000. Print total salary."""

# sal1=float(input("Please enter the salary:"))

# if sal1>50000:
#     sal1+=5000
# else:
#     sal1+=2000
# print(f"The salary is {sal1}")

""" 15. Check Shopping Discount If bill amount > 1000, give 10% discount else no discount."""

# a= float(input("Please enter total bill:"))
# if a>1000:
#     a-=0.1*a
#     print(f"Total bill:{a}")
# else:
#     print(f"Total bill:{a}")

""" 16. Age Category If age < 13 print Child If age between 13 and 19 print Teen Else print Adult"""

# num1=int(input("Please enter your age:"))

# if num1>19:
#     print(f"Adult")
# elif 13<num1<20:
#     print(f"Teen")
# else:
#     print("Child")

""" 17. Electricity Bill Calculator (Simple) If units <= 100 charge 2 per unit If 101-200 charge 3 per unit Above 200 charge 5 per unit"""

# num1=int(input("Please enter total unit consumed:"))

# if num1>200:
#     print(f"The Bill amount is:{num1*5}")
# elif 100<num1<201:
#     print(f"The Bill amount is:{num1*3}")
# else:
#     print(f"The Bill amount is:{num1*2}")

""" 18. Check Number is Multiple of 3 or 7 Input a number and check if it is multiple of 3 or 7."""

# num1=int(input("Please enter a number:"))

# if num1%21==0:
#     print(f"{num1} is divisible by both 3 and 7")
# else:
#     print(f"{num1} is not divisible by both 3 and 7")

""" 19. Check Password Strength If password length >= 8 print Strong Password else Weak Password."""

# u_pass = input("Please enter the password:")

# if len(u_pass)<8:
#     print("Week password")
# else:
#     print("Strong Password")


""" 20. Find Smallest of Two Numbers Take two numbers and print the smaller one. """

# num1=int(input("Please enter the first number:"))
# num2=int(input("Please enter the second number:"))

# if num1<num2:
#     print(num1)
# else:
#     print(num2)
