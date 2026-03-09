""" 11. Write a program to input two numbers and find the remainder using the modulus operator."""

# num1=float(input("Please enter the first number:"))
# num2=float(input("Please enter the Second number:"))
# print("The remainder of the first to second number is:",num1%num2)

""" 12. Write a program to input two numbers and perform integer division using floor division."""

# num1=float(input("Please enter the first number:"))
# num2=float(input("Please enter the Second number:"))
# print("The floor division of the first to second number is:",num1//num2)

""" 13. Write a program to input a number of days and convert it into:
    a) Weeks
    b) Remaining days """

# num1=int(input("Please enter the number of days to convert into weeks:"))
# print( num1,"days are equeal to",num1//7,"weeks and",num1%7,"days")

""" 14. Write a program to input a total amount and number of people, then calculate how much each person should pay."""

# num1=float(input("Please enter the total amount to distribute:"))
# num2=int(input("Please enter the total number of workers:"))
# print("The pay per person is",num1/num2)

""" 15. Write a program to input a 3-digit number and calculate the sum of its digits."""

# num1=int(input("Please enter a 3-digit number:"))
# x1=num1%10
# num2=num1//10
# x2=num2%10
# num3= num2//10
# x3=x1+x2+num3
# print("The sum of the digit in the number is:",x3)

""" 16. Write a program to input a 3-digit number and reverse the number. """

# num1=int(input("Please enter a 3-digit number:"))
# x1=num1%10
# num2=num1//10
# x2=num2%10
# num3= num2//10
# x3=x1*100+x2*10+num3
# print("The reverse of the number is:",x3)

""" 17. Write a program to input total seconds and convert it into: a) Minutes b) Remaining seconds"""

# num1=int(input("Please enter the total seconds to convert:"))
# minu=num1//60
# seco=num1%60
# hr=minu//60
# mins=minu%60
# print( num1,"seconds equeal to",hr,"hours",mins,"minutes and",seco,"seconds")

""" 18. Write a program to input the total marks of 5 subjects and calculate: a) Total marks b) Average marks"""

# num1=float(input("Please enter the marks of Maths out of 100:"))
# num2=float(input("Please enter the marks of Malayalam out of 100:"))
# num3=float(input("Please enter the marks of English out of 100:"))
# num4=float(input("Please enter the marks of Science out of 100:"))
# num5=float(input("Please enter the marks of Social out of 100:"))
# total=num1+num2+num3+num4+num5
# print("Your total marks is:",total, "and the avarage is:",total/5)

""" 19. Write a program to input a number and check whether it is even or odd using the modulus operator."""

# num1=int(input("Please enter a number to check even or odd:"))
# x=num1%2
# if x==0:
#     print( num1,"is an even number")
# else:
#     print( num1,"is an odd number")

""" 20. Write a program to input a number and calculate:  a) Square using **  b) Cube using ** """

# num1=int(input("Please enter a intiger number to calculate Square and Cube:"))
# print("The Square of",num1,"is", num1**2, " and the Cube is",num1**3)


