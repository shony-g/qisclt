""" 1. Write a program to calculate the area and perimeter of a rectangle. """

# num1=float(input("Please enter the length of a rectangle in cm:"))
# num2=float(input("Please enter the breadth of a rectangle in cm:"))
# print("The area of the rectangle is:",num1*num2,"cm2")
# print("The perimeter of the rectangle is:",(num1+num2)*2,"cm")

""" 2. Given a total number of days, convert it into years, weeks, and days."""

# num1=int(input("Please enter the number of days to convert:"))
# year=num1//365
# remDays=num1%365
# weeks=remDays//7
# days=remDays%7
# print( num1,"days are equeal to",year,"Years",weeks,"weeks and",days,"days")

""" 3. Calculate the compound interest for a given principal, rate, and time."""

# princi=float(input("Please enter the principal amount in Rs:"))
# inter=float(input("Please enter the interest rate in %:"))
# years=float(input("Please enter the time in years:"))
# r=inter/100
# a=(1+r)**years
# b=princi*a
# print("compound interest for a given principal for",years,"years is:",b)

""" 4. Write a program to swap two variables using only arithmetic operators ($+$ and $-$)."""

# num1=int(input("Please enter the first number:"))
# num2=int(input("Please enter the Second number:"))
# num1+=num2
# num2=num1-num2
# num1-=num2
# print("First number:",num1,"Second number:",num2)

""" 5. Demonstrate the difference between / (float division) and // (floor division) using positive and negative numbers."""

# num1=int(input("Please enter the first number:"))
# num2=int(input("Please enter the Second number:"))
# print("Float division of",num1,"and",num2,"is",num1/num2,)
# print("The input numbers are positive intigets but the result is number type is float.")
# print("Floor division of",num1,"and",num2,"is",num1//num2,)
# print("Floor divition only provide the integier number not the decimal parts.")
# num1=num1*(-1)
# print("Let make a first number to a negative number",num1)
# print("Float division of",num1,"and",num2,"is",num1/num2,)
# print("The input numbers are positive intiget number but the result is float ty number.")
# print("Floor division of",num1,"and",num2,"is",num1//num2,)
# print("Floor divition only provide the integier number not the decimal parts.")

""" 6. Find the remainder of $12345$ divided by $67$ using the modulo operator."""
# a=12345
# b=67
# c=a%b
# print("The remainder of",a,"divided by",b,"is:",c)

""" 7. Write a script to calculate $a^b$ without using the pow() function."""

# num1=int(input("Please enter the first number:"))
# num2=int(input("Please enter the Second number:"))
# print("First number power of Second number is:",num1**num2)

""" 8. Create a simple "Tip Calculator": Input bill amount and percentage, output the final total."""

# print("Tip Calculator")
# a=float(input("Please enter the bill amount in Rs:"))
# b=float(input("Please enter the tip percentage in %:"))
# r=b/100
# t=a*r
# print("The bill amount is",a,"tip is",t,"and the total bill is:",a+t)

"""9. Use the += operator to keep a running total of 5 user-input numbers."""
# num1=int(input("Please enter the first number:"))
# num2=int(input("Please enter the Second number:"))
# num3=int(input("Please enter the third number:"))
# num4=int(input("Please enter the fourth number:"))
# num5=int(input("Please enter the fifth number:"))

# sum=0
# sum+=num1
# sum+=num2
# sum+=num3
# sum+=num4
# sum+=num5
# print("The sum of five number is:",sum)

"""10. Given a 3-digit number, find the sum of its digits using / and %."""

# num1=int(input("Please enter a three digit  number:"))
# num2= num1//10
# sum = num2%10 + num1%10 + num1//100
# print("The sum of its digits is :",sum)

""" 11. Write a program to convert Celsius to Fahrenheit: $F = (C \times 9/5) + 32$."""

# C=int(input("Please enter temperature in Celsiu:"))
# F= (C*9/5)+32
# print("The temperature in Fahrenheit is :",F)

""" 12. Calculate the surface area of a sphere given its radius."""

# r=int(input("Please enter the radius of the sphere:"))
# pi=3.14
# a=4*pi*r**2
# print("The surface area of the sphere is :",a)

""" 13. Implement a program that calculates the BMI (Body Mass Index) based on weight (kg) and height (m)."""

# num1=float(input("Please enter the weight (kg):"))
# num2=float(input("Please enter the height (m):"))
# bmi=num1/(num2**2)
# print("BMI (Body Mass Index) is:",bmi)

""" 14. Show how the * operator behaves differently with integers vs. strings."""
# num1= 123
# x="shony"
# one=num1*2
# two=x*2
# print("With int",one,"with string",two)

"""15. Predict and verify the result of $10 + 5 * 2 ** 3 / 4 - 1$. Explain the precedence. """
# sum = 10 + 5 * 2 ** 3 / 4 - 1
# print(sum)