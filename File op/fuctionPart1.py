""" 
============================================================
SECTION A - BASIC FUNCTION BUILDING
============================================================

"""

""" 1. Write a function `company_welcome()` that prints:   "Welcome to Python Full Stack Lab"""

# def company_welcome():
#     print("Welcome to Python Full Stack Lab")


# company_welcome()

""" 2. Write a function `display_course_name()` and call it 3 times."""

# def display_course_name():
#     print("Python")

# display_course_name()
# display_course_name()
# display_course_name()

""" 3. Create a function `show_lab_rules()` that prints at least 5 lab instructions."""

# def show_lab_rules():
#     print("Wlecome to QIS")
#     print("Please Keep Bag outside")
#     print("Keep sialence")
#     print("Work hard")
#     print("If you need any help, please rise your hand")


# show_lab_rules()

""" 4. Write a function `student_info(name)` that prints: "Hello <name>, welcome to the Python lab" """
# def student_info(name):
#     print(f"Hello {name}, welcome to the Python lab")

# student_info("Shony")

""" 5. Write a function `add_two_numbers(a, b)` that returns the sum."""

# def add_two_numbers(a, b):
#     eSum = a+b
#     return eSum

# one = int(input("Enter first number:"))
# sec = int(input("Enter second number:"))
# print(add_two_numbers(one,sec))

""" 6. Write a function `multiply_three_numbers(a, b, c)` that returns the result. """

# def multiply_three_numbers(a, b, c):
#     eMul = a*b*c
#     return eMul

# one = int(input("Enter first number:"))
# sec = int(input("Enter second number:"))
# thre = int(input("Enter third number:"))

# print(multiply_three_numbers(one,sec,thre))

""" 7. Write a function `is_even(num)` that returns True if the number is even, otherwise False."""

# def is_even(num):
#     if num%2==0:
#         return True
#     else:
#         return False

# one = int(input("Enter the number:"))

# print(f"This is a even number :{is_even(one)}")

""" 8. Write a function `find_square(n)` that returns the square of a number."""

# def find_square(n):
#     return n*n

# one = int(input("Enter the number:"))

# print(f"The square of the number :{find_square(one)}")

""" 9. Write a function `find_cube(n)` that returns the cube of a number."""

# def find_cube(n):
#     return n**3

# one = int(input("Enter the number:"))

# print(f"The cube of the number :{find_cube(one)}")

""" 10. Write a function `full_name(first_name, last_name)` that returns the full name."""

# def full_name(first_name, last_name):
#     fname = first_name + " " +last_name
#     return fname
# print(full_name("Shony","Gangadharan"))

""" 11. Write a function `calculate_discount(price, discount_percent)` that returns the final price."""

# def calculate_discount(price, discount_percent):
#     disc = price * discount_percent/100
#     price-=disc
#     return price

# one = int(input("Enter the price:"))
# two = int(input("discount percentage:"))

# final_price = calculate_discount(one, two)
# print(f"The final price:{final_price}")

""" 12. Write a function `fahrenheit_to_celsius(temp)` that returns the Celsius value."""

# def fahrenheit_to_celsius(temp):
#     cels = (temp - 32) / 1.8
#     return cels

# one = int(input("Enter the temprature:"))

# print(f"The temperature in C: {fahrenheit_to_celsius(one)}")

""" 13. Write a function `calculate_area_of_rectangle(length, width)`."""

# def calculate_area_of_rectangle(length, width):
#     area_r = length * width
#     return area_r

# one = int(input("Enter the length:"))
# two = int(input("Enter the width:"))

# print(f"The area of rectangle: {calculate_area_of_rectangle(one,two)}")

""" 14. Write a function `calculate_simple_interest(p, r, t)`."""

# def calculate_simple_interest(p, r, t):
#     si = p * r * t / 100
#     total = p + si
#     return si
# p = int(input("Enter the priciple amount:"))
# r = int(input("Enter the rate of interest:"))
# t = int(input("Enter the time in years:"))
# palisa = calculate_simple_interest(p,r,t)
# motham = p + palisa
# print(f"The simple intrest is: {palisa} and the total is:{motham}")

""" 15. Write a function `generate_email(username, domain)` that returns a professional email ID."""

# def generate_email(username, domain):
#     emadd = username+'@'+domain
#     return emadd
# p = input("Enter username:")
# r = input("Enter domain:")

# print(f"The email address: {generate_email(p,r)}")

""" 
============================================================
SECTION B - FUNCTION CALLING + RETURN VS PRINT
============================================================

"""

""" 16. Write one function using `print()` and another using `return()` for adding two numbers.
    Compare the outputs."""

# def add_two(a,b):
#     return a+b
# p = int(input("Enter the first number:"))
# r = int(input("Enter the second number:"))

# def add_one(a,b):
#     print (a+b)

# print(add_two(p,r))
# print(add_one(p,r))

""" 17. Create a function `product_price(price, tax)` using return. Store the returned value in a variable and print it."""

# def product_price(price, tax):
#     tax = price * tax/100
#     price +=tax
#     return price

# p = int(input("Enter the price of the product:"))
# r = int(input("Enter the tax rate:"))

# fin_price = product_price(p,r)

# print(fin_price)

""" 18. Write a function `greet_user(name)` using print.
    Try storing it in a variable and observe the output."""

# def greet_user(name):
#     print(name)

# uname = greet_user("Dheeraj")

# print(uname)

""" 19. Write a function `calculate_salary(basic, hra, bonus)` that returns gross salary."""

# def calculate_salary(basic, hra, bonus):
#     hra = basic * hra /100
#     bonus = basic * bonus/100

#     salary = basic + hra + bonus

#     return salary
# b = int(input("Enter the basic salary:"))
# h = int(input("Enter hra percentage:"))
# bon = int(input("Enter bonus percetange:"))

# gross_salary = calculate_salary(b,h,bon)

# print(gross_salary)

""" 20. Create a function `student_result(mark1, mark2, mark3)` that returns total and average."""

# def student_result(mark1, mark2, mark3):
#     total = mark1 + mark2 + mark3
#     avag = total/3
#     return total, avag

# mytot, myavg = student_result(76,85,91)

# print (myavg, mytot)

""" 21. Write a function `login_status(username)` using print.
    Then convert it to return-based logic."""

# def login_status(username):
#     print(f"{username} logged in sucessfully")

# login_status("shony")

# def login_status2(username):
#     return username +" " + "logged in successful"

# abc = login_status2 ("priyanka")
# print(abc)

""" 22. Create a function `order_summary(item, qty, price)` that prints order details."""

# def order_summary(item, qty, price):
#     tot = qty * price
#     print(f"{item} quntity {qty} nos, price {price} = grand total {tot}")

# order_summary("bolt",5,25)

""" 23. Rewrite the previous question using return so the output can be reused elsewhere."""

# def order_summary(item, qty, price):
#     tot = qty * price
#     return str(item) + " quntity" + str(qty) + "nos, price" + str(price) + " = grand total " + str(tot)

# order = order_summary("bolt",5,25)

# print(order)

""" ============================================================
SECTION C - FUNCTION ARGUMENTS
============================================================
"""

""" 24. Write a function `employee_details(name, age, department)` using positional arguments."""

# def employee_details(name, age, department):
#     print(f"Name: {name}")
#     print(f"Age {age}")
#     print(f"Department {department}")


# employee_details(46,"shony", "Voice")
# employee_details("shony",46,"Voice")

""" 25. Call the above function with incorrect order and observe the issue."""

# employee_details(46,"shony", "Voice")

"""26. Rewrite the previous question using keyword arguments. """

# def employee_details(name, age, department):
#     print(f"Name: {name}")
#     print(f"Age {age}")
#     print(f"Department {department}")


# employee_details(name="Shony",department="Python",age=46)

""" 27. Create a function `create_profile(name, city="Kochi")`.
    Call it with and without city."""

# def create_profile(name, city="Kochi"):
#     print(f"Name: {name}")
#     print(f"City: {city}")

# create_profile("shony")
# create_profile("Shony", "Kozhikode")

""" 28. Write a function `book_ticket(name, seat_type="General", meal="No")`."""

# def book_ticket(name, seat_type="General", meal="No"):
#     print(f"Name: {name}")
#     print(f"Seat type: {seat_type}")
#     print(f"Meal :{meal}")

# book_ticket(name="Shony", seat_type="Chair car")
# book_ticket('priyanka','ac','yes')

""" 29. Create a function `send_notification(user, message="Welcome!")`."""

# def send_notification(user, message="Welcome!"):
#     print(f"{message} {user}")

# send_notification('shony','How are you')
# send_notification('Priya')

""" 30. Write a function `register_student(name, course="Python", duration="3 Months")`."""

# def register_student(name, course="Python", duration="3 Months"):
#     print(f"Name :{name} course={course} duration={duration}")

# register_student('shony','java')
# register_student('priya','python','6 months')

""" 31. Write a function `calculate_bill(amount, gst=18)`."""

# def calculate_bill(amount, gst=18):
#     gst = amount * gst/100
#     print(f"Price {amount} and  Bill with GST  :{amount + gst}")

# calculate_bill(100,12)

# calculate_bill(200)

""" 32. Create a function `delivery_charge(location, charge=50)`."""

# def delivery_charge(location, charge=50):
#     print(f"{location} and delivery charge is {charge}")

# delivery_charge('Kozhikode')
# delivery_charge('Kannur', 100)

""" 33. Write a function `attendance_status(name, status="Present")`."""

# def attendance_status(name, status="Present"):

#     print(f"{name} {status}")

# attendance_status('shony')
# attendance_status('richu','absend')

"""
============================================================
SECTION D - *args AND **kwargs
============================================================

"""

""" 34. Write a function `sum_all(*numbers)` that returns the sum of all given numbers."""

# def sum_all(*numbers):
#     return sum(numbers)

# result= sum_all(2,4,5,6,7)
# print(result)

""" 35. Write a function `find_maximum(*numbers)`."""

# def find_maximum(*numbers):
#     return max(numbers)
   
# num = find_maximum(3,6,7,3,4)
# print(num)

""" 36. Write a function `display_subjects(*subjects)` that prints all subject names."""

# def display_subjects(*subjects):
#     for x in subjects:
#         print(x)

# display_subjects('maths','malayalam','physics','Chemistry')

""" 37. Write a function `average_marks(*marks)` that returns the average."""

# def average_marks(*marks):
#     num = sum(marks)
#     avg = num /len(marks)
#     return avg

# print(average_marks(48,43,41,49,36))

""" 38. Write a function `shopping_total(*prices)` that returns total amount."""
# def shopping_total(*prices):
#     return sum(prices)

# num = shopping_total(23,45,67,44,32,23)
# print(num)

""" 39. Write a function `student_profile(**details)` that prints all key-value pairs."""

# def student_profile(**details):
#     for key, Valu in details.items():
#         print(key, ":", Valu)

    
# student_profile(
#     name = "shony",
#     age = 46,
#     course = "Python",
#     city = "Kozhikode"
# )

""" 40. Write a function `employee_record(**data)` to print employee details."""

# def employee_record(**data):
#     for x,y in data.items():
#         print(x," : ",y)

# employee_record(
#     name = "Priya",
#     dep = " Voice"
# )

""" 41. Write a function `product_details(**info)` for an ecommerce product."""

# def product_details(**info):
#     for x,y in info.items():
#         print(x," : ",y)

# product_details(
#     product = "laptop",
#     Brand = "Lenovo",
#     Price= 50000
# )

""" 42. Write a function `user_settings(**settings)` to simulate app preferences."""
# def user_settings(**settings):
#     for x,y in settings.items():
#         print(x, ":", y)
    
# user_settings(
#     color = "Blue",
#     size ="12 x 10 x 2",
#     user = "authentication"
# )

""" 43. Write a function `create_resume(**details)` to print formatted resume data."""

# def create_resume(**details):
#     for x, y in details.items():
#         print(x, " : ",y)

# create_resume(
#     anme = "Shony",
#     age = 46,
#     stream = "python"
# )

""" 44. Write a function `report_card(name, *marks, **details)`."""
# def report_card(name, *marks, **details):
#     print("Student Name:", name)

#     print("Marks")
#     for mark in marks:
#         print(mark)

#     print("Details")
#     for x,y in details.items():
#         print(x," : ",y)

# report_card(
#     "Shony",
#     45,41,46,
#     Grade = "A",
#     Place = "Kozhikode"
# )

""" 45. Write a function `invoice(customer_name, *items, **meta)`."""

# def invoice(customer_name, *items, **meta):
#     print(f"Name : {customer_name}")
#     print("Items")
#     for n in items:
#         print(n)
#     print("Meta Data")
#     for x,y in meta.items():
#         print (x," : ",y)
    

# invoice(
#     "SHony Call blast",
#     "toll free","national","local",
#     india = 91,
#     US= 1
# )

""" ============================================================
SECTION E - REAL-WORLD LOGIC BUILDING FUNCTIONS
============================================================
"""

""" 46. Write a function `validate_login(username, password)` that checks:
    - username should not be empty
    - password length should be at least 8"""

# def validate_login(username, password):
#     if username == "":
#         print("Username cannot be empty")
#     elif len(password)<8:
#         print("Password must be grater than 8 letters")
#     else:
#         print("Thank you!!!")
    
# validate_login("Shony","12345678")
    
""" 47. Write a function `is_eligible_for_vote(age)`."""

# def is_eligible_for_vote(age):
#     if age >17:
#         print("You are aligble for voting")
#     else:
#         print("You are not eligible for voting")

# is_eligible_for_vote(74)

""" 48. Write a function `is_eligible_for_job(age, degree_completed)`."""

# def is_eligible_for_job(age, degree_completed):
#     if age >17 and degree_completed == True:
#         print(" Elelgible for Job")
#     else:
#         print("Not eligible")

# is_eligible_for_job(19, True)

""" 49. Write a function `calculate_overtime(hours_worked)`. """

# def calculate_overtime(hours_worked):
#     if hours_worked > 8:
#         print("Eligible for over time pay")
#     else:
#         print("Not eligible for OT")

# calculate_overtime(9)

""" 50. Write a function `check_free_shipping(cart_total)`."""

# def check_free_shipping(cart_total):
#     if cart_total >1000:
#         print("Eligible")
#     else:
#         print("Not Eligible")

# check_free_shipping (1560)

""" 51. Write a function `check_coupon_valid(amount)`: Apply coupon only if amount >= 1000."""

# def check_coupon_valid(amount):
#     if amount >1000:
#         print("Eligible")
#     else:
#         print("Not Eligible")

# check_coupon_valid (560)

""" 52. Write a function `calculate_mobile_bill(call_minutes, sms_count, data_used)`."""

# def calculate_mobile_bill(call_minutes, sms_count, data_used):
#     Total_Bill = call_minutes * 0.20 + sms_count /100 + data_used *0.25/1000000000
#     return Total_Bill

# bill = calculate_mobile_bill(2000, 456,1500000000)
# print(bill)

""" 53. Write a function `loan_eligibility(salary, cibil_score)`."""

# def loan_eligibility(salary, cibil_score):
#     loan = salary * cibil_score /1000
#     if loan * 10 > 150000:
#         print(f"Eligible for load, max loan amount {loan * 3}")
#     else:
#         print("Not elegible")

# loan_eligibility(30000,876)

""" 54. Write a function `password_strength(password)`: Check length, digits, uppercase, lowercase."""

# def password_strength(password):
#     if len(password) < 8:
#         print("Password too short")
#         return
#     hasDigit = False
#     hasUpcase = False
#     hasLocase = False

#     for char in password:

#         if char.isdigit():
#             hasDigit = True
#         if char.isupper():
#             hasUpcase = True
#         if char.islower():
#             hasLocase = True
    
#     if hasLocase and hasDigit and hasUpcase:
#         print("Strong Password")
#     else:
#         print("Week Password")

# password_strength("Dontvntry")


""" 55. Write a function `username_validator(username)`:
    Rules:
    - minimum 5 characters
    - no spaces
    - must start with alphabet"""

# def username_validator(username):
#     if len(username) < 6:
#         print("too short")
#     elif " " in username:
#         print("username do not have space")
#     elif not username[0].isalpha():
#         print("username must start with alphabet")
#     else:
#         print("valied username")

# username_validator("shony123")

""" 56. Write a function `email_validator(email)` using simple conditions."""

# def email_validator(email):
#     asd = email.split("@")
    
#     if "@" not in email:
#         print("email must contain @")
#     elif " " in email:
#         print("no space allowed")
#     elif "." not in asd[1]:
#         print("please enter valied domain name")
#     else:
#         print("email address is valied")

# email_validator("asd@kjj.kadi")

""" 57. Write a function `generate_username(first_name, last_name)`."""

# def generate_username(first_name, last_name):

#     if " " in first_name and " " in last_name:
#         print("Please enter name with out space")
#         return

#     email = last_name[0]+first_name
#     return email

# uemai= generate_username("shony", "gangs")
# print(uemai)

""" 59. Write a function `masked_phone(number)` that returns masked phone like:
    9876543210 -> 987****210"""

# def masked_phone(number):
#     num = str(number)

#     if len(num) == 10:
#         num1 = num[:3]+"****"+num[-3:]
#         return num1
#     else:
#         print("Not a valied phone number")
#         return
    

# print(masked_phone (9035076908))

""" 60. Write a function `masked_email(email)`."""

# def masked_email(email):
#     lst= email.split("@")
#     uname = lst[0]
#     doname = lst[1]

#     msk= uname[:2] + "*****@" + doname
#     return msk

# print(masked_email("shony@gmail.com"))
    

"""
============================================================
SECTION F - TYPE HINTING PRACTICALS
============================================================





67. Write a function `get_topper(students: dict) -> str`

68. Write a function `filter_even(numbers: list[int]) -> list[int]`

69. Write a function `product_stock(name: str, quantity: int) -> str`

70. Write a function `calculate_total(prices: list[float]) -> float`

============================================================
SECTION G - BUILT-IN VS USER-DEFINED FUNCTIONS
============================================================

71. Write a program using built-in functions:
    len(), max(), min(), sum(), type()

72. Create a user-defined function that performs the same job as `max()` for 3 numbers.

73. Create a user-defined function that performs the same job as `sum()` for a list of numbers.

74. Write a custom function `my_len(text)` without using `len()`.

75. Write a custom function `my_upper(text)` without using `.upper()`.

76. Write a custom function `my_abs(num)` without using `abs()`."""

""" 61. Write a function with type hints:     `def add(a: int, b: int) -> int`"""

# def add(a: int, b: int) -> int:
#     return a + b

# print(add(10,20))

""" 62. Write a function `full_name(first: str, last: str) -> str`"""

# def full_name(first: str, last: str) -> str:
#     fname = first + " " + last
#     return fname

# print(full_name ("shony", "gangadharan"))

""" 63. Write a function `calculate_gst(amount: float, tax: float) -> float"""
# def calculate_gst(amount: float, tax: float) -> float:
#     gst = amount + amount * tax/100
#     return gst

# print(calculate_gst(123.23,12))

""" 
64. Write a function `is_adult(age: int) -> bool`

65. Write a function `student_grade(mark: int) -> str`

66. Write a function `average(numbers: list[float]) -> float`"""

def print_numbers(n):

    if n == 0:
        return

    print_numbers(n - 1)

    print(n)

print_numbers(5)