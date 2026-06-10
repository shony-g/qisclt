""" OPERATOR OVERLOADING QUESTIONS """

""" 81. Overload + operator for complex numbers. """

# class Complex_num:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#         self.result = a + b

#     def show_add(self):
#         print(self.result)

# a = Complex_num('d','g')
# b = Complex_num(6,3)
# a.show_add()
# b.show_add()

""" 82. Overload + operator for adding bank balances. """

# class Bank_account:
#     def __init__(self,name,balence):
#         self.name = name
#         self.balence = balence
    
#     def __add__(self, other):
#         return self.balence + other.balence

#     def show_balence(self):
#         print(f"{self.name} Balanece :{self.balence}")

# acc1 = Bank_account('shony',6000)
# acc2 = Bank_account ('Priya', 7000)

# total_bank = acc1 + acc2

# acc1.show_balence()
# acc2.show_balence()

# print(f'Total Balance :',total_bank)

""" 

85. Create a shopping cart object supporting +.

86. Create a vector class with operator overloading.

87. Create a salary object supporting arithmetic operations.


89. Create a distance calculator using operator overloading.

90. Build a cryptocurrency wallet supporting operations."""

""" 83. Overload * operator for matrix multiplication."""

# class Complex_num:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#         self.result = a * b

#     def show_add(self):
#         print(self.result)

#     def __mul__(self,other):
#         return self.b * other.b
    
# a = Complex_num(5,'g')
# b = Complex_num(6,3)
# c = a*b
# a.show_add()
# b.show_add()
# print(c)

""" 84. Overload comparison operators for students based on marks."""

# class Complex_num:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#         self.result = a > b

#     def show_add(self):
#         print(self.result)

# # a = Complex_num(5,'g')
# b = Complex_num(6,3)
# c = Complex_num('f','k')
# d = Complex_num([5,2,6],[6,1,1])
# # a.show_add()
# b.show_add()
# c.show_add()
# d.show_add()

""" 88. Create a custom string formatter using operator overloading. """

# class String_op:
#     def __init__(self,a,b, oprator):
#         self.a = a
#         self.b = b
#         self.oprator = oprator
        
#     def do_opra(self):
#         if self.oprator == '+':
#             return self.a + self.b
#         elif self.oprator == '*':
#             return self.a * self.b
#         elif self.oprator == '<':
#             return self.a < self.b
#         elif self.oprator == '>':
#             return self.a > self.b
#         elif self.oprator == '==':
#             return self.a == self.b
#         elif self.oprator == '/':
#             return self.a / self.b
#         else:
#             print('Not a valied operator')
    
#     def show_op(self):
#         print(self.do_opra())
            
# a = String_op('d','f','+')
# a.show_op()
        
""" METHOD OVERRIDING QUESTIONS

92. Create a payment system overriding process_payment().

93. Create a social media notification system.

95. Build a food delivery app overriding delivery charges.

96. Create a ride fare calculator using overriding.

97. Create a streaming app with different subscription plans.

98. Build an employee attendance system.

99. Create a cloud storage pricing system.

"""

""" 91. Override display() method in child class."""

# class Animal:
#     def display (self):
#         print('Animal can run')

# class Dog(Animal):
#     def display(self):
#         print('Dogs can bark')

# a1= Animal()
# a2 = Dog()

# a1.display()
# a2.display()

""" 94. Create:
   - Admin
   - User
   - Guest
   overriding permissions."""


# class Admin:
#     def access (self):
#         print('Animal can system settings')

# class User(Admin):
#     def access (self):
#         print('User can access applictions')

# class Guest (Admin):
#     def access (self):
#         print('Guest can read documents')

# a1= Admin()
# a2 = User()
# a3= Guest()

# a1.access()
# a2.access()
# a3.access()

""" 100. Create a fraud detection system using overriding."""

# class Transaction:
#     def __init__(self,amount,loction,balance):
#         self.amount= amount
#         self.location = loction
#         self.balance = balance
#     def disply(self):
#         print()
#         print('........Transaction details..............')
#         print(f'Amount :{self.amount} banalnce {self.balance}')

# class Fruadprevent (Transaction):
#     def disply(self):
#         print("Fraud Detection Report")
#         print('........Transaction details..............')
#         print(f'Amount :{self.amount} banalnce {self.balance}')

#         if self.amount > self.balance:
#             print('Fruad alert')
#         elif self.amount > 50000:
#             print('Fruad alert')
#         elif self.location != 'India':
#             print('Fruad alert')
#         else:
#             print('safe transaction')

# a1 = Fruadprevent(5000,'India', 3000000)
# a2 = Fruadprevent(75000,"India",3000000)

# a1.disply()
# a2.disply()
            
""" ENCAPSULATION QUESTIONS """

""" 101. Create private attributes using __."""

# class Bank:
#     def __init__(self,name,balance):
#         self.__name = name
#         self.__balance = balance
        
#     def show_account(self):
#         print(f'Ac name {self.__name}')
#         print(f'Balance {self.__balance}')

# a1 = Bank('shony',8000000)
# # a1.__balance, """ getting error Bank' object has no attribute '__balance """
# a1.show_account()

""" 
103. Create a secure banking system.

105. Create a login system protecting passwords."""

""" 102. Create getter and setter methods."""

# class Student:
#     def __init__(self, name, mark):
#         self.__name = name
#         self.__mark = mark
        
#     def get_mark(self):
#         return self.__mark
    
#     def get_name(self):
#         return self.__name
    
#     def set_mark(self,mark):
#         self.__mark = mark
    
#     def set_name(self,name):
#         self.__name = name


# a1=Student('shony',45)

# print(a1.get_mark())
# print(a1.get_name())
# # print(a1._name), """get error prive, if we put single _ restircted, it will work """
# # print(a1._mark), """get error prive, if we put single _ restircted, it will work """

# a1.set_mark(48)
# print(a1.get_mark())
# a1.set_name('Priya')
# print(a1.get_name())

""" 104. Hide salary details using encapsulation. """

# class Bank:
#     def __init__(self, name, account, balance):
#         self.__name = name
#         self.__account = account
#         self.__balance = balance
        
#     def get_balance(self):
#         return self.__balance, self.__account
    
#     def get_name(self):
#         return self.__name, self.__account
    
#     def deposit(self,amount):
#         self.amount = amount
#         if self.amount > 0:
#             self.__balance += self.amount
#             print(f'{self.amount} sucessfully deposited')
#         else:
#             print('Not valied deposit')
        
    
#     def withdraw(self,amount):
#         self.amount = amount
#         if self.amount < self.__balance:
#             self.__balance -= self.amount
#             print(f'{self.amount} sucessfully withdrwed')
#         else:
#             print('Not valied deposit')


# a1=Bank('shony',101,45000)

# print(a1.get_balance())
# print(a1.get_name())

# a1.deposit(48000)
# print(a1.get_balance())
# a1.withdraw(6000)
# print(a1.get_balance())

# # print(a1.__balance) """ Error"""

""" 106. Create an ATM system with PIN validation.

107. Create a student grading system.

108. Create a hospital patient record system.

109. Create an online wallet with balance protection.

110. Create a secure inventory management system."""

""" ABSTRACTION QUESTIONS

113. Create:
   - Abstract Vehicle
   - Bike
   - Car

114. Create:
   - Abstract Shape
   - Circle
   - Rectangle

116. Create a cloud service provider abstraction.

117. Create a machine learning model abstraction.

118. Create an online exam system using abstraction.

119. Create an e-commerce delivery abstraction.

"""

""" 111. Create an abstract class for payment systems."""

# from abc import ABC, abstractmethod

# class Payement(ABC):
    
#     @abstractmethod
#     def payment (self, amount):
#         self.amount = amount
#         print('payment completed.')

#     @abstractmethod
#     def show_payment(self):
#         print(f'{self.amount} paid')

# class CrediCard(Payement):
    
#     def payment(self, amount):
#         return super().payment(amount)
    
#     def show_payment(self):
#         return super().show_payment()

# class UPI (Payement):
    
#     def payment(self, amount):
#         return super().payment(amount)
    
#     def show_payment(self):
#         return super().show_payment()

# a10 = CrediCard()
# a20 = UPI()

# a10.payment(5000)
# a10.show_payment()
# a20.payment(4000)
# a20.show_payment()

""" 112. Create abstract methods:
   - login()
   - logout()"""

# from abc import ABC, abstractmethod

# class User (ABC):
    
#     @abstractmethod
#     def login (self,name):
#         self.name= name
#         print('User logged in')

#     @abstractmethod
#     def logout(self):
#         print('user logout')

# class Student(User):
    
#     def login(self,name):
#         self.name= name
#         super().login(self.name)
   
#     def logout(self):
#         super().logout()

# a10 = Student()
# a10.login('shony')
# a10.logout()

""" 115. Build an online food ordering abstraction system."""

# from abc import ABC, abstractmethod

# class FoodOrder(ABC):
    
#     def __init__(self, name, food,price):
#         self.cus_name = name
#         self.food = food
#         self.price = price
    
#     @abstractmethod
#     def placeorder (self):
#         print(f'Customer Name {self.cus_name}')
#         print (f'Food {self.food}')
#         print(f'Price {self.price}')
        
    
#     @abstractmethod
#     def cancelorder(self):
#         print(f'Delivery cancelled')
#         print(f'Customer Name {self.cus_name}')
#         print (f'Food {self.food}')
#         print(f'Price {self.price} returned')
        
    

# class Delorder (FoodOrder):
    
#     def placeorder(self):
#         print(f'Delivery order placed')
#         return super().placeorder()
    
#     def cancelorder(self):
#         return super().cancelorder()
    
# class PickupOrder(FoodOrder):
    
#     def placeorder(self):
#         print(f'Order picked up')
#         return super().placeorder()
    
#     def cancelorder(self):
#         return super().cancelorder()
    
# a10 = Delorder('shony', 'puttu', 150)
# a20 = PickupOrder( 'shony','puttu',150)
# a10.placeorder()
# a10.cancelorder()

# a20.placeorder()
# a20.cancelorder()

""" 120. Build a hospital appointment abstraction system."""

# from abc import ABC, abstractmethod

# class Hospital(ABC):
    
#     def __init__(self, name,doct):
#         self.cus_name = name
#         self.doct = doct

#     @abstractmethod
#     def appontment(self):
#         print(f'Customer Name {self.cus_name}')
#         print (f'apponment registered for {self.doct}')
        
#     @abstractmethod
#     def cancelorder(self):
#         print(f'appontment cancelled')
        

# class User(Hospital):
    
#     def appontment(self):
#         print(f'getting appoinment')
#         return super().appontment()
    
#     def cancelorder(self):
#         return super().cancelorder()

# a10 = User('shony', 'OP')
# a10.appontment()
# a10.cancelorder()
