""" OOPs Lab Practical Questions (Python) """

""" BEGINNER LEVEL QUESTIONS"""
""" 1. Create a Student class with attributes:
   - name
   - age
   - course
   Create 3 objects and display their details."""

# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def get_details(self):
#         print('Name :', self.name)
#         print("Age :",self.age)
#         print('Course :', self.course)
#         print()


# std1 = Student('Shony',45,'Python')
# std2 = Student('Priya',40,'java')
# std3 = Student('Theju',40,'Boxing')

# std1.get_details()
# std2.get_details()
# std3.get_details()
 
""" 2. Create an Employee class and calculate yearly salary from monthly salary."""

# class Employee:
#     def __init__(self,name, salary):
#         self.salary = salary
#         self.name = name

#     def ctc (self):
#         sal = self.salary
#         bon = 0.05 * self.salary
#         year_sal = 12*sal + bon 
#         return year_sal
    
#     def get_details(self):
#         print(f"Monthaly Salary :{self.salary}")
#         print(f"Yearly Salary :{self.ctc()}")
        


# emp1 = Employee ('as',10000)
# emp2 = Employee ('ad',20000)
# emp3 = Employee ('hg',15000)

# emp1.get_details()
# emp2.get_details()

""" 3. Create a Car class with methods:
   - start()
   - stop()
   - display_details()"""

# class Car:

#     def __init__(self,brand,model,color):
#         self.model = model
#         self.brand = brand
#         self.color = color
        
#     def start (self):
#         print (f"{self.brand} with model {self.model} with {self.color} is starting")

#     def stop (self):
#         print (f"{self.brand} with model {self.model} with {self.color} is stopping")

#     def display_details (self):
#         print (f"Brand :{self.brand}")
#         print (f"Model {self.model}")
#         print (f"Color {self.color}")

# car1 = Car('VW','Ameo','Silk Blue')
# car1.display_details()
# car1.stop()
# car1.start()

""" 4. Create a Mobile class and store:
   - brand
   - model
   - price"""

# class Mobile:

#     def __init__(self,brand,model,price):
#         self.model = model
#         self.brand = brand
#         self.price = price
        

#     def display_details (self):
#         print (f"Brand :{self.brand}")
#         print (f"Model {self.model}")
#         print (f"Price {self.price}")

# mobile1 = Mobile('Apple',14,'110000')
# mobile1.display_details()

""" 5. Create a Book class and display book details using objects."""

# class Book:

#     def __init__(self,sub,size,pages):
#         self.sub = sub
#         self.size = size
#         self.pages = pages
        

#     def display_details (self):
#         print (f"Type :{self.sub}")
#         print (f"Model {self.size}")
#         print (f"Price {self.pages}")

# notebook = Book('notebook','A4',100)
# notebook.display_details()

""" 6. Create a BankAccount class with:
   - deposit()
   - withdraw()
   - check_balance()"""

# class Bank:

#     def __init__(self,name,acno,balance):
#         self.name = name
#         self.acno = acno
#         self.balance = balance
#         self.IFSC_Code = 'ICIC0000401'
    
#     def deposit (self, amount):
#         if amount < 0:
#             print("Not a valied amount")
#         else:
#             self.balance += amount
#             print(f"{amount} deposited successfully.")
#         return self.balance 

#     def withdraw(self,amount):
#         if amount <= self.balance:
#             self.balance-= amount
#             print(f"{amount} withdrawn successfully.")
#         else:
#             print("Insifficient balaence")
#         return self.balance 

#     def check_balance (self):
#         print (f"Name :{self.name}")
#         print (f"AC No :{self.acno}")
#         print (f"IFSC Code :{self.IFSC_Code}")
#         print (f"Balance {self.balance}")

# ac1= Bank('Shony',4011616,35000)
# ac1.check_balance()

# ac1.deposit(25000)
# ac1.withdraw(30000)

# ac1.check_balance()

# print(ac1.deposit(2000))

""" 7. Create a Laptop class and count how many objects are created. """

# class Laptop:

#     def __init__(self,brand,model,price):
#         self.model = model
#         self.brand = brand
#         self.price = price
        

#     def display_details (self):
#         print (f"Brand :{self.brand}")
#         print (f"Model {self.model}")
#         print (f"Price {self.price}")

# lap1 = Laptop('Lenovo','Think Pad',50000)
# lap1.display_details()

""" 8. Create a class for HospitalPatient with:
   - patient_id
   - disease
   - doctor_name"""

# class HospitalPatient:

#     def __init__(self,patient_id,disease,doctor_name):
#         self.patient_id = patient_id
#         self.disease = disease
#         self.price = doctor_name
        

#     def display_details (self):
#         print (f"Patient ID :{self.patient_id}")
#         print (f"Disease {self.disease}")
#         print (f"Doctor name {self.price}")

# pat1 = HospitalPatient(201,'Fever','Dr Shaji')
# pat1.display_details()

""" 9. Create a MovieTicket class to calculate total ticket price."""

# class MovieTicket:

#     def __init__(self,movie_name,ticket_price,num_ticket):
#         self.movie_name = movie_name
#         self.ticket_price = ticket_price
#         self.num_ticket = num_ticket
        
#     def total_price (self):
#         return  self.ticket_price * self.num_ticket

#     def display_details (self):
#         print (f"Movie Name :{self.movie_name}")
#         print (f"Number of ticket :{self.ticket_price}")
#         print (f"Total price :{self.total_price()}")

# pat1 = MovieTicket('Drishyam',250,4)
# pat1.display_details()

# print(pat1.total_price())

""" CONSTRUCTOR-BASED QUESTIONS"""
"""  10. Create a Rectangle class and calculate:
   - area
   - perimeter"""

# class Rectangle:

#     def __init__(self,len,bre):
#         self.len = len
#         self.bre = bre

#     def area (self):
#         return  self.len * self.bre
    
#     def perimeter (self):
#         return  (self.len  + self.bre) *2

#     def display_details (self):
#         print (f"Length :{self.len}")
#         print (f"Breadth :{self.bre}")
#         print (f"Area :{ self.area()}")
#         print (f"Perimeter :{self.perimeter()}")

# rect1 = Rectangle(12,10)
# print(rect1.area())
# print(rect1.perimeter())

# rect1.display_details()

""" 11. Create a class using a default constructor."""

# class Laptop:

#     def __init__(self):
#         self.model = 'Victus'
#         self.brand = 'HP'
#         self.price = 65000
        
#     def display_details (self):
#         print (f"Brand :{self.brand}")
#         print (f"Model {self.model}")
#         print (f"Price {self.price}")

# lap1 = Laptop()
# lap1.display_details()

""" 12. Create a class using a parameterized constructor."""

# class Bank:

#     def __init__(self,name,acno,balance):
#         self.name = name
#         self.acno = acno
#         self.balance = balance
#         self.IFSC_Code = 'ICIC0000401'
    
#     def deposit (self, amount):
#         if amount < 0:
#             print("Not a valied amount")
#         else:
#             self.balance += amount
#             print(f"{amount} deposited successfully.")
#         return self.balance 

#     def withdraw(self,amount):
#         if amount <= self.balance:
#             self.balance-= amount
#             print(f"{amount} withdrawn successfully.")
#         else:
#             print("Insifficient balaence")
#         return self.balance 

#     def check_balance (self):
#         print (f"Name :{self.name}")
#         print (f"AC No :{self.acno}")
#         print (f"IFSC Code :{self.IFSC_Code}")
#         print (f"Balance {self.balance}")

# ac1= Bank('Shony',4011616,35000)
# ac1.check_balance()

# ac1.deposit(25000)
# ac1.withdraw(30000)

# ac1.check_balance()

# print(ac1.deposit(2000))

""" 13. Create a User class where password should not be empty."""

# class User:
#     def __init__(self, username,password):
#         self.username = username
#         if password == "":
#             print("Pasword could not empty")
#             self.password = None
#         else:
#             self.password = password

#     def get_details(self):
#         print('Username :', self.username)
        
#         if self.password is not None:
#             print("Password is set")
#         else:
#             print("password not set")


# amit = User('amit', 12345)
# ant = User('ant',"")

# amit.get_details()
# ant.get_details()

""" 14. Create a constructor that validates email format."""

# class User:
#     def __init__(self, username,email):
#         self.username = username
#         if email == "":
#             print("Email could not empty")
#             self.email = None
#         elif '@' not in email:
#             print("Email must have @")
#             self.email = None
#         elif "." not in email:
#             print("Email must have .")
#             self.email = None
#         elif email.startswith("@") or email.endswith("@"):
#             print("Email must not start @")
#             self.email = None
#         elif email.startswith(".") or email.endswith("."):
#             print("Email must not start .")
#             self.email = None
#         else:
#             self.email = email 
        
#     def display_details(self):
#         print('Username :', self.username)
        
#         if self.email is not None:
#             print("Email is set")
#         else:
#             print("Email not set")


# amit = User('amit', 'abc@domain.com')
# ant = User('ant',"@domain.com")

# amit.display_details()
# ant.display_details()

""" 15. Create a constructor that automatically generates employee IDs."""

# class User:

#     emp_id = 1

#     def __init__(self, username):
#         self.username = username
#         self.emp_id = User.emp_id
#         User.emp_id += 1
        

#     def get_details(self):
#         print('Employe_ID :', self.emp_id)
#         print('Username :', self.username)
        

# amit = User("amit")
# ant = User("ant")

# amit.get_details()
# ant.get_details()

""" 16. Create a Product class that applies GST during object creation. """

# class Product:
#     def __init__(self,name, price):
#         self.pname = name
#         self.price = price
    
#     def after_gst(self):
#         gst = 0.18 * self.price
#         return self.price + gst

# salt = Product('tata',20)

# sugar = Product('parley',40)

# print(f"Salt is {salt.pname} price include Gst is {salt.after_gst()}")
# print(f"Salt is {sugar.pname} price include Gst is {sugar.after_gst()}")
        
""" 17. Create a Vehicle class that stores:
   - owner name
   - vehicle number
   - insurance expiry"""

# class Vehicle:
#     def __init__(self,owner, numb, insuEx):
#         self.oname = owner
#         self.rnum = numb
#         self.insurEx = insuEx
    
#     def display_details(self):
#         print(f"Owner Name :{self.oname}")
#         print(f"Registration Number is :{self.rnum}")
#         print(f"insurence Expaire date:{self.insurEx}")
#         print()

# car1 = Vehicle('shony','KL56 H 7933','26-10-2026')
# jepp1 = Vehicle('priya','KL56 E 5549','03-12-2026')

# car1.display_details()
# jepp1.display_details()

""" 18. Create a LibraryBook class with constructor-based initialization."""

# class LibraryBook:
#     def __init__(self,student, bname, date):
#         self.sname = student
#         self.book_name = bname
#         self.date = date
    
#     def display_details(self):
#         print(f"{self.sname} has taken a book with name {self.book_name} on {self.date}")
#         print()

# book1 = LibraryBook('shony','python study','10-05-2026')

# book1.display_details()

""" 19. Create a Course class and enroll students using constructors."""

# class Course:
#     def __init__(self,student, batch, subject):
#         self.sname = student
#         self.course = subject 
#         self.batch = batch
    
#     def display_details(self):
#         print(f"{self.sname} has joined {self.course} with {self.batch}")
#         print()
# anu = Course('Anu','11 AM','Python')
# manu = Course('Manu','2 PM','Java')

# anu.display_details()
# manu.display_details()

""" 20. Create a FoodOrder class that calculates total bill automatically."""

# class FoodOrder:
#     def __init__(self,item, price, onum):
#         self.iname = item
#         self.price = price 
#         self.count = onum
#         self.tot_bill = self.price * self.count
    
#     def display_details(self):
#         print(f"{self.iname} has ordered with price {self.price} with {self.count}")
#         print(f"Total bill is: {self.tot_bill}")
#         print()

# usr1 = FoodOrder('Biriyani',150,4)
# usr2 = FoodOrder('Chodu',80,2)

# usr1.display_details()
# usr2.display_details()

""" SELF AND ATTRIBUTE QUESTIONS """

""" 21. Demonstrate the use of self."""

# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def get_details(self):
#         print('Name :', self.name)
#         print("Age :",self.age)
#         print('Course :', self.course)
#         print()


# std1 = Student('Shony',45,'Python')
# std2 = Student('Priya',40,'java')
# std3 = Student('Theju',40,'Boxing')

# std1.get_details()
# std2.get_details()
# std3.get_details()

""" 22. Differentiate:
   - class attribute
   - instance attribute"""
# class Student:
#     school_name = 'QIS'
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def get_details(self):
#         print(f"School Name : {self.school_name}")
#         print('Name :', self.name)
#         print("Age :",self.age)
#         print('Course :', self.course)
#         print()
# """ School name is class attribute, instance attribute changed for each object"""

# std1 = Student('Shony',45,'Python')
# std2 = Student('Priya',40,'java')
# std3 = Student('Theju',40,'Boxing')

# std1.get_details()
# std2.get_details()
# std3.get_details()

""" 23. Create a company management system using class attributes."""

# class Employee:
#     company_name = 'QIS'
#     company_ltd = 'Private'
#     total_employees = 1

#     def __init__(self, name, department, salary):
#         self.name = name
#         self.depart = department
#         self.salary = salary
#         self.emp_id = Employee.total_employees
#         Employee.total_employees +=1

#     def get_details(self):
#         print(f"Company Name : {self.company_name, self.company_ltd}")
#         print('Employee Name :', self.name)
#         print("Department :",self.depart)
#         print('Salary :', self.salary)
#         print('Emp ID :', self.emp_id)
#         print()

# std1 = Employee('Shony',45,'400000')
# std2 = Employee('Priya',40,'400000')
# std3 = Employee('Theju',40,'400000')

# std1.get_details()
# std2.get_details()
# std3.get_details()

""" 24. Create instance-specific attributes for users."""

# class User:
#     def __init__(self, username,password):
#         self.username = username
#         if password == "":
#             print("Pasword could not empty")
#             self.password = None
#         else:
#             self.password = password

#     def get_details(self):
#         print('Username :', self.username)
        
#         if self.password is not None:
#             print("Password is set")
#         else:
#             print("password not set")


# amit = User('amit', 12345)
# ant = User('ant',"")

# amit.get_details()
# ant.get_details()

""" 25. Demonstrate local variables inside methods."""

# class User:
#     company_name = 'SCB'

#     def __init__(self, username,password):
#         self.username = username
#         if password == "":
#             print("Pasword could not empty")
#             self.password = None
#         else:
#             self.password = password

#     def get_details(self):
#         print('Company Name:', self.company_name)
#         print('Username :', self.username)
        
#         if self.password is not None:
#             print("Password is set")
#         else:
#             print("password not set")
    
#     def Salary (self, amount):
#         mon_sal = 0.4*amount + amount
#         dudect = 2000 + 0.01 * amount
#         self.take_home = mon_sal - dudect
#         ctc = mon_sal * 12
#         return f"Monthly Salay :{self.take_home} and CTC {ctc}"



# amit = User('amit', 12345)
# ant = User('ant',"")

# amit.get_details()
# ant.get_details()
# print()
# print("Amit",amit.Salary(20000))
# print("Ani", ant.Salary(40000))
# print()
# print(amit.take_home)

""" 26. Create a class attribute that tracks total online users."""

# class Online_users:
#     total_users = 0

#     def __init__(self, name, password):
#         self.name = name
#         self.pasword = password
#         Online_users.total_users +=1

#     def get_details(self):
#         print('Employee Name :', self.name)
#         print("Password :",self.pasword)
#         print()

# std1 = Online_users('Shony','12345')
# std2 = Online_users('Priya','12345')
# std3 = Online_users('Theju','12345')

# std1.get_details()
# std2.get_details()
# std3.get_details()

# print(std1.total_users)
# print(std2.total_users)
# print(std3.total_users)

""" 27. Build a login system where each object stores unique user data."""

# class User:
#     company_name = 'SCB'
#     lst_users = []
#     def __init__(self, username,password):
#         if username in self.lst_users:
#             self.username = None
#         else:
#             self.username = username
#             self.lst_users.append(username)
#         if password == "":
#            self.password = None
#         else:
#             self.password = password

#     def get_details(self):
        
#         if self.username is None:
#             print("Username already exsist")
#         else:
#             print('Company Name:', self.company_name)
#             print('Username :', self.username)
#             if self.password is not None:
#                 print("Password is set")
#             else:
#                 print("password not set")
#         print()

# amit = User('amit', 12345)
# ant = User('ant',"")

# amit.get_details()
# ant.get_details()

# ramu = User('amit', 12345)
# ramu.get_details()

""" 28. Create a shopping cart where products are instance attributes."""

# class Online_portal:
    
#     def __init__(self, name):
#         self.customer_name = name
#         self.product = []

#     def add_product (self,pro_name,price):
#         self.product.append([pro_name,price])
#         print(f"{pro_name} added to the card")

#     def display_cart (self):
#         print('Custopmer name :', self.customer_name)
#         print(f"Products selected")
#         for x in self.product:
#             print(f"{x[0]} - {x[1]}")
#         print()
    
#     def remove_product (self,name):
#         for x in self.product:
#             if x[0] == name:
#                 self.product.remove(x)
#                 print(f'{name} Removed from cart')
        
    
#     def total_price(self):
#         tot_v = 0
#         for x in self.product:
#             tot_v = x[1] + tot_v
#         return f"Total amoun : {tot_v}"

# std1 = Online_portal('Shony')
# std2 = Online_portal('Priya')
# std3 = Online_portal('Thejas')

# std1.add_product('TV',20000)
# std1.add_product('Mobile',30000)
# std1.add_product('AC',45000)
# print()
# std1.display_cart()
# print()
# std1.remove_product('AC')
# std1.display_cart()
# print()
# print(std1.total_price())
""" 29. Create a school system using:
   - class attribute for school name
   - instance attribute for student details"""

# class Student:
#     school_name = 'QIS'
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def get_details(self):
#         print(f"School Name : {self.school_name}")
#         print('Name :', self.name)
#         print("Age :",self.age)
#         print('Course :', self.course)
#         print()
# """ School name is class attribute, instance attribute changed for each object"""

# std1 = Student('Shony',45,'Python')
# std2 = Student('Priya',40,'java')
# std3 = Student('Theju',40,'Boxing')

# std1.get_details()
# std2.get_details()
# std3.get_details()

""" 30. Create a weather app object storing city-wise temperature data."""

# class Weather_app:
#     def __init__(self):
#         self.city_temp = {}
    
#     def add_temp(self, city, temp):
#         self.city_temp[city]= temp
#         print (f'{city} temperature addedd')
    
#     def dislay_weather (self):
#         print('Citywise temperature data')

#         for x, y in self.city_temp.items():
#             print(f'{x} : {y}°C')

#     def get_temp (self,city):
#         if city in self.city_temp:
#             print(f"{city} Temperature is {self.city_temp[city]}°C")
#         else:
#             print(f"{city} not found")

# kerala = Weather_app()
# tn = Weather_app()
# ka = Weather_app()
# kerala.add_temp('Kochi',32)
# kerala.add_temp('tvm',31)
# kerala.add_temp('clt',29)

# kerala.dislay_weather()

# kerala.get_temp('clt')

""" ATTRIBUTE HANDLING FUNCTIONS """

""" 31. Use getattr() to access object properties dynamically."""

# class Student:
#     school_name = 'QIS'
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def get_details(self):
#         print(f"School Name : {self.school_name}")
#         print('Name :', self.name)
#         print("Age :",self.age)
#         print('Course :', self.course)
#         print()
# """ School name is class attribute, instance attribute changed for each object"""

# std1 = Student('Shony',45,'Python')
# std2 = Student('Priya',40,'java')
# std3 = Student('Theju',40,'Boxing')

# std1.get_details()
# std2.get_details()
# std3.get_details()

# print(getattr(std1,'name', 'Novalied dats'))
# print(getattr(std1,'age', 'Novalied dats'))

""" 32. Use setattr() to update employee salary."""

# class Employee:
#     company_name = 'QIS'
#     company_ltd = 'Private'
#     total_employees = 1

#     def __init__(self, name, department, salary):
#         self.name = name
#         self.depart = department
#         self.salary = salary
#         self.emp_id = Employee.total_employees
#         Employee.total_employees +=1

#     def get_details(self):
#         print(f"Company Name : {self.company_name, self.company_ltd}")
#         print('Employee Name :', self.name)
#         print("Department :",self.depart)
#         print('Salary :', self.salary)
#         print('Emp ID :', self.emp_id)
#         print()

# std1 = Employee('Shony',45,'400000')
# std2 = Employee('Priya',40,'400000')
# std3 = Employee('Theju',40,'400000')

# std1.get_details()
# std2.get_details()
# std3.get_details()

# setattr(std2,'salary', '50000')
# setattr(std1,'depart','social')
# setattr(std3,'name','Dheeraj')
# setattr(std3,'time','Mon-Fri')

# std1.get_details()
# std2.get_details()
# std3.get_details()

""" 33. Use hasattr() to validate whether an object contains a field."""

# class Employee:
#     company_name = 'QIS'
#     company_ltd = 'Private'
#     total_employees = 1

#     def __init__(self, name, department, salary):
#         self.name = name
#         self.depart = department
#         self.salary = salary
#         self.emp_id = Employee.total_employees
#         Employee.total_employees +=1

#     def get_details(self):
#         print(f"Company Name : {self.company_name, self.company_ltd}")
#         print('Employee Name :', self.name)
#         print("Department :",self.depart)
#         print('Salary :', self.salary)
#         print('Emp ID :', self.emp_id)
#         print()

# std1 = Employee('Shony',45,'400000')
# std2 = Employee('Priya',40,'400000')
# std3 = Employee('Theju',40,'400000')

# std1.get_details()
# std2.get_details()
# std3.get_details()

# setattr(std2,'salary', '50000')
# setattr(std1,'depart','social')
# setattr(std3,'name','Dheeraj')
# setattr(std3,'time','Mon-Fri')

# std1.get_details()
# std2.get_details()
# std3.get_details()

# print(hasattr(std1,'time'))
# print(hasattr(std1,'name'))
# print(hasattr(std1,'depart'))
# print(hasattr(std1,'age'))

""" 34. Use delattr() to remove an object attribute."""

# class Employee:
#     company_name = 'QIS'
#     company_ltd = 'Private'
#     total_employees = 1

#     def __init__(self, name, department, salary):
#         self.name = name
#         self.depart = department
#         self.salary = salary
#         self.emp_id = Employee.total_employees
#         Employee.total_employees +=1

#     def get_details(self):
#         print(f"Company Name : {self.company_name, self.company_ltd}")
#         print('Employee Name :', self.name)
#         print("Department :",self.depart)
#         print('Salary :', getattr(self, 'Salary','Salary deleted'))
#         print('Emp ID :', self.emp_id)
#         print()

# std1 = Employee('Shony',45,'400000')
# std2 = Employee('Priya',40,'400000')
# std3 = Employee('Theju',40,'400000')

# std1.get_details()
# std2.get_details()
# std3.get_details()

# delattr(std1,'salary')

# std1.get_details()

""" 35. Build a dynamic student record manager using attribute functions."""

# class Student:
#    school_name = 'QIS'
#    tot_student = 1

#    def __init__(self, name, age, course):
#       self.name = name
#       self.age = age
#       self.course = course
#       self.std_id = Student.tot_student
        
#       Student.tot_student+=1

#    def display_details(self):
#       print(f"School Name : {self.school_name}")
#       print('Student ID :', getattr(self,'std_id','Student ID not available'))
#       print('Name :', getattr(self,'name','Name not available'))
#       print("Age :",getattr(self,'age', 'Age not availabe'))
#       print('Course :', getattr(self,'course','Course not available'))
#       print('Marks :',getattr(self,'marks','Marks not available'))
#       print()

# class Student_manager:
    
#    def __init__(self):
#       self.students = []

#    def add_student(self,name, age, course):
#       user = Student(name,age,course)
#       self.students.append(user)
#       print('Student add successfully')
   
#    def show_all_student (self):
#       if not self.students:
#          print("No Student found")
#          return
#       for user in self.students:
#          user.display_details()
   
#    def find_student(self,student_id):
#       for user in self.students:
#          if user.std_id == student_id:
#             return user
#       return None
   
#    def get_atribute(self,student_id, atribute):
#       user = self.find_student(student_id)
#       if user:
#          a = getattr(user,atribute,'atribute not found')
#          print(f"{atribute} :{a}")
#       else:
#          print('Student not found')

#    def update_atribute (self, student_id,atribute,value):
#       user =self.find_student(student_id)
#       if user:
#          setattr(user, atribute,value)
#          print(f"{atribute} update successfully")
#       else:
#          print('User not found')

#    def delete_atribute(self,student_id,atribute):
#       user = self.find_student(student_id)
#       if user:
#          if hasattr(user,atribute):
#             delattr(user,atribute)
#             print(f'{atribute} delete sucessfully')
#          else:
#             print(f'{atribute} not found')
#       else:
#          print('Student not found')

# manager = Student_manager()

# manager.add_student('Shony',44,'Python')
# manager.add_student('Priya',41,'Java')
# manager.add_student('Thejas',21,'Data science')
# manager.add_student('Koya',24,'Data science')

# manager.show_all_student()

# # print(manager.find_student(4))

# manager.get_atribute(4,'name')
# manager.get_atribute(2,'marks')
# manager.get_atribute(3,'age')

# manager.update_atribute(4,'name','pathu')
# manager.update_atribute(1,'age','46')

# manager.show_all_student()

# manager.delete_atribute(4,'age')
# manager.show_all_student()

""" 36. Create an API response object and dynamically add attributes.

37. Create a configuration class where attributes are added at runtime.

38. Build a chatbot profile manager using setattr().

39. Create a form builder using dynamic attributes.

40. Create a dynamic inventory management system."""


# class Student:
#    school_name = 'QIS'
#    tot_student = 1

#    def __init__(self, name, age, course):
#       self.name = name
#       self.age = age
#       self.course = course
#       self.std_id = Student.tot_student
        
#       Student.tot_student+=1

#    def display_details(self):
#       print(f"School Name : {self.school_name}")
#       print('Student ID :', getattr(self,'std_id','Student ID not available'))
#       print('Name :', getattr(self,'name','Name not available'))
#       print("Age :",getattr(self,'age', 'Age not availabe'))
#       print('Course :', getattr(self,'course','Course not available'))
#       print('Marks :',getattr(self,'marks','Marks not available'))
#       print()

# class Student_manager:
    
#    def __init__(self):
#       self.students = []

#    def add_student(self,name, age, course):
#       user = Student(name,age,course)
#       self.students.append(user)
#       print('Student add successfully')
   
#    def show_all_student (self):
#       if not self.students:
#          print("No Student found")
#          return
#       for user in self.students:
#          user.display_details()
   
#    def find_student(self,student_id):
#       for user in self.students:
#          if user.std_id == student_id:
#             return user
#       return None
   
#    def get_atribute(self,student_id, atribute):
#       user = self.find_student(student_id)
#       if user:
#          a = getattr(user,atribute,'atribute not found')
#          print(f"{atribute} :{a}")
#       else:
#          print('Student not found')

#    def update_atribute (self, student_id,atribute,value):
#       user =self.find_student(student_id)
#       if user:
#          setattr(user, atribute,value)
#          print(f"{atribute} update successfully")
#       else:
#          print('User not found')

#    def delete_atribute(self,student_id,atribute):
#       user = self.find_student(student_id)
#       if user:
#          if hasattr(user,atribute):
#             delattr(user,atribute)
#             print(f'{atribute} delete sucessfully')
#          else:
#             print(f'{atribute} not found')
#       else:
#          print('Student not found')

# manager = Student_manager()

# manager.add_student('Shony',44,'Python')
# manager.add_student('Priya',41,'Java')
# manager.add_student('Thejas',21,'Data science')
# manager.add_student('Koya',24,'Data science')

# manager.show_all_student()

# # print(manager.find_student(4))

# manager.get_atribute(4,'name')
# manager.get_atribute(2,'marks')
# manager.get_atribute(3,'age')

# manager.update_atribute(4,'name','pathu')
# manager.update_atribute(1,'age','46')

# manager.show_all_student()

# manager.delete_atribute(4,'age')
# manager.show_all_student()