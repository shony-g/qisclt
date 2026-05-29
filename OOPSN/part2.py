""" INHERITANCE QUESTIONS """

""" SINGLE INHERITANCE  """

""" 41. Create:
   - Parent → Person
   - Child → Student """

# class Person:
#    def __init__(self,name,age):
#       self.name = name
#       self.age = age

#    def dislplay_details(self):
#       print(f'name is {self.name} and age is {self.age}')

# class Child(Person):
#    def __init__(self, name, age,gender):
#       super().__init__(name, age)
#       self.gender = gender

#    def show_details(self):
#       self.dislplay_details()
#       print(f'The baby is {self.gender}')

   
# std1 = Child('Theju',11,'Boy')
# std1.show_details()

""" 42. Create:
   - Parent → Vehicle
   - Child → Bike"""

# class Vehicle:
#    def __init__(self,brand,model):
#       self.name = brand
#       self.model = model

#    def dislplay_details(self):
#       print(f'The brand is {self.name} and the model is {self.model}')

# class Bike(Vehicle):
#    def __init__(self, brand,model,yearm):
#       super().__init__(brand, model)
#       self.yearm = yearm

#    def show_details(self):
#       self.dislplay_details()
#       print(f'The Bike manufactured {self.yearm}')

   
# std1 = Bike('TVS','Avanies',2026)
# std1.show_details()

""" 43. Create an Employee class inherited by Developer."""

# class Employee:
#    Company_Name = 'QIS'
#    emp_id =1
#    def __init__(self):
#       self.ceo = 'Ravi'
#       self.cfo = 'sasi'

#    def dislplay_details(self):
#       print(f'company CEO {self.ceo} and CFO {self.cfo}')

# class Developer(Employee):
#    def __init__(self, name,depart):
#       super().__init__()
#       self.name = name
#       self.depart =depart
#       self.emp_no = Employee.emp_id
#       Employee.emp_id+=1

#    def show_details(self):
#       self.dislplay_details()
#       print(f'{self.emp_no} : {self.name} in {self.depart}')

   
# std1 = Developer('deepa','HR')
# std1.show_details()

""" 44. Create a hospital management system using inheritance. """

# class Hospital:
#     hopital_name = 'Fathiam Hospital'
#     h_address = 'Near Vet hospital, Kannur road, Kozhikode'
#     h_facility = ['Causuality', 'Emergency', 'in patianet service']
#     h_deparments =['genaral medicine','Pediatrician','gynocology','Orthology']
#     h_patianet_ID ='P'
#     h_docotrs_id = 'D'
#     h_nurse_id = 'N'

#     def __init__(self, h_id,name,age,depart = 'genaral medicine'):
#         self.hosp_id =h_id
#         self.name =name
#         self.age =age
#         self.depart = depart

#     def show_hosp (self):
#         print(f'............ {self.hopital_name}................')
#         print(f'............ {self.h_address}...................')
#         print(f'{self.hosp_id} : {self.name}  {self.age}  {self.depart}')

# class Doctor(Hospital):
#     doc_id = 1
#     def __init__(self,name,age,depart):
#         h_id = 'D'+ str(Doctor.doc_id)
#         Doctor.doc_id+=1 
#         super().__init__(h_id, name, age, depart)
    
# class Patiant(Hospital):
#     pat_id = 1
#     def __init__(self,name,age,depart):
#         h_id = 'P'+ str(Patiant.pat_id)
#         Patiant.pat_id+=1 
#         super().__init__(h_id, name, age, depart)


# omjit = Doctor('Omjith',51,'Pediac')
# omjit.show_hosp()
# print()
# shony = Patiant('shony',46,'Alergy')
# shony.show_hosp()

""" 45. Create a payment gateway system using inheritance."""

# class Payment:
#     def __init__(self,amount, custer_name):
#         self.amount = amount
#         self.customer = custer_name
   
#     def payment_details(self):
#         print("Customer name:", self.customer)
#         print("Amount ......:", self.amount)

#     def process_payment (self):
#         print('Processing payment')

# class CrediCard(Payment):
#     def __init__(self, amount, custer_name,car_number):
#         super().__init__(amount, custer_name)
#         self.card_number = car_number

#     def process_payment(self):
#         print("Creditcard payment")
#         self.payment_details()
#         print('Card number XXXX XXXX XXXX', str(self.card_number)[-4:])
#         print('Payment successfully completed')

# class UPIpayment(Payment):
#     def __init__(self, amount, custer_name,upi_id):
#         super().__init__(amount, custer_name)
#         self.upi_id = upi_id

#     def process_payment(self):
#         print("UPI Payment")
#         self.payment_details()
#         print('UPI ID', self.upi_id)
#         print('Payment successfully completed')

# payment1 = CrediCard(5000,'shony',1223343)
# payment2 = UPIpayment(4000,'priya','pkk@okicici')
# print ()
# payment1.process_payment()
# payment2.process_payment()
    
""" MULTILEVEL INHERITANCE """

""" 46. Create:
   - Animal → Mammal → Dog"""

# class Animal:
#     def __init__(self):
#         print('Animal reproduce')

#     def show_animal(self):
#         print('Animal with baby animal')
        
# class Mamal(Animal):
#     def __init__(self):
#         super().__init__()
#         self.baby = 'feeding'

#     def show_mamal(self):
#         self.show_animal()
#         print('Mamales feed babies', self.baby)

# class Dog(Mamal):
#     def __init__(self):
#         super().__init__()
#         self.sound = 'bow bow'

#     def show_dog(self):
#         self.show_mamal()
#         print('Bow Bow')

# tomy = Dog()
# tomy.show_dog()

""" 47. Create:
   - Company → Department → Employee"""

# class Company:
#     def show_company(self):
#         print('Company name is Shony Cll Blast')

        
# class Department(Company):
   
#     def show_department(self):
#         print('This is from telephone department', )

# class Employee(Department):
#     def __init__(self, name):
#         self.name = name

#     def show_employee(self):
#         self.show_company()
#         self.show_department()
#         print(f'Employye name {self.name}')

# tomy = Employee('Tomy')
# tomy.show_employee()

""" 48. Create:
   - User → Seller → PremiumSeller"""

# class PremiumSeller:
#     def __init__(self,product, company):
#         self.product = product
#         self.company = company

#     def show_company(self):
#         print(f'Product :{self.product} of {self.company}')
        
# class Seller(PremiumSeller):
#     def __init__(self, product, company,order = 100):
#         super().__init__(product, company)
#         self.order = order
   
#     def show_seller(self):
#         print(f'The seller stock {self.order}', )

# class User(Seller):
#     def __init__(self, product, company,order,price):
#         super().__init__(product, company,order)
#         self.price = price
#         self.tot = self.order * self.price

#     def show_order(self):
#         self.show_company()
#         self.show_seller()
#         print(f'Total Cost is : {self.tot}')

# tomy = User('pen','Cello',100,10)
# tomy.show_order()

""" 49. Create:
   - Account → SavingsAccount → SalaryAccount """

# class SalaryAccount:
#     def __init__(self,name, company):
#         self.name = name
#         self.company = company

#     def show_company(self):
#         print(f'company :{self.company} and Employee {self.name}')
        
# class SavingsAccount(SalaryAccount):
#     def __init__(self, name, company,salary):
#         super().__init__(name, company)
#         self.salary = salary
   
#     def show_savings(self):
#         print(f'The salaries {self.salary}', )

# class Account(SavingsAccount):
#     def __init__(self, name, company,salary,tax):
#         super().__init__(name, company,salary)
#         self.tax = tax
#         self.take_home = self.salary - (self.salary * self.tax / 100)

#     def show_salary(self):
#         self.show_company()
#         self.show_savings()
#         print(f'Total Take Home salary is  : {self.take_home}')

# tomy = Account('Jasil','IBM',40000,10)
# tomy.show_salary()

""" 50. Create:
   - Device → Laptop → GamingLaptop"""

# class Device:
#     def __init__(self,company):
#         self.company = company

#     def show_company(self):
#         print(f'company :{self.company}')
        
# class Laptop(Device):
#     def __init__(self,company,model):
#         super().__init__(company)
#         self.model = model
   
#     def show_savings(self):
#         print(f'The model {self.model}', )

# class GamingLaptop(Laptop):
#     def __init__(self, company,model,ram,cpu):
#         super().__init__(company,model)
#         self.ram = ram
#         self.cpu = cpu

#     def show_laptop(self):
#         self.show_company()
#         self.show_savings()
#         print(f'with CPU {self.cpu} and RAM {self.ram}')

# tomy = GamingLaptop('HP','Victus','64GB','i9')
# tomy.show_laptop()

""" MULTIPLE INHERITANCE """

""" 51. Create a class inheriting from:
   - Camera
   - Phone"""

# class Camara:
#     def __init__(self, photo):
#         self.photo = photo
    
#     def show_camara(self):
#         print(f'Camara can take {self.photo}')

# class Phone:
#     def __init__(self, call):
#         self.call = call
    
#     def show_phopne(self):
#         print(f'Phone can handle {self.call}.')

# class Mobile(Camara,Phone):
#     def  __init__(self, photo, call,games):
#         Camara.__init__(self,photo)
#         Phone.__init__(self,call)
#         self.game = games

#     def show_mobile(self):
#         print(f'mobiles can call {self.call}')
#         print(f'mobiles can do {self.photo} photo')
#         print(f'mobiles can play {self.game}')

# s20 = Mobile('selfie',911,'snakes')
# s20.show_mobile()

""" 52. Create:
   - Teacher
   - Researcher
   - Professor"""

# class Researcher:
#     def __init__(self, research):
#         self.research = research
    
#     def show_research(self):
#         print(f'Researcher working on {self.research}')

# class Teacher:
#     def __init__(self, subject):
#         self.subject = subject
    
#     def show_teacher(self):
#         print(f'Teacher teach {self.subject}.')

# class Professor(Researcher,Teacher):
#     def  __init__(self, name,reaserch, subject):
#         Researcher.__init__(self,reaserch)
#         Teacher.__init__(self,subject)
#         self.name = name

#     def show_mobile(self):
#         print(f'Professors work as teacher in {self.subject}')
#         print(f'Professor do reaserch on {self.research}')
#         print(f'Professor name {self.name}')

# s20 = Professor('shony','AI','python')
# s20.show_mobile()

""" 53. Create:
   - GPS
   - MusicPlayer
   - SmartCar"""

# class GPS:
#     def __init__(self, location):
#         self.gps = location
    
#     def show_gps(self):
#         print(f'GPS can found location {self.gps}')

# class MusicPlayer:
#     def __init__(self, track):
#         self.audio = track
    
#     def show_player(self):
#         print(f'Player can play {self.audio}.')

# class SmartCar(GPS,MusicPlayer):
#     def  __init__(self, location,track, drive):
#         GPS.__init__(self,location)
#         MusicPlayer.__init__(self,track)
#         self.drive = drive

#     def show_car(self):
#         print(f'SmartCar GPS location set on {self.gps}')
#         print(f'SmartCar playing {self.audio}')
#         print(f'SmartCar with speed {self.drive}')

# s20 = SmartCar('Kochi','MJ bille jean','120km/hr')
# s20.show_car()

""" 54. Build a food delivery app using multiple inheritance."""

# class Zomato:
#     def __init__(self, hotels):
#         self.hotels = hotels
    
#     def show_hotels(self):
#         print(f'available hotels {self.hotels}')

# class Hotel:
#     def __init__(self, foods):
#         self.foods = foods
    
#     def show_foods(self):
#         print(f'The hotel have {self.foods}.')

# class User(Zomato,Hotel):
#     def  __init__(self, hotel, foods,amount):
#         Zomato.__init__(self,hotel)
#         Hotel.__init__(self,foods)
#         self.amount = amount

#     def show_order(self):
#         self.show_hotels()
#         self.show_foods()
#         print(f'You have selcted Hotel {self.hotels}')
#         print(f'You have seleted Foods {self.foods}')
#         print(f'You have paid amount {self.amount}')

# s20 = User('Paragon','Biriyani','500/-')
# s20.show_order()

""" 55. Create a drone system combining:
   - Camera
   - FlightController"""

# class Camera:
#     def __init__(self, video):
#         self.video = video
    
#     def show_camara(self):
#         print(f'Camara showing {self.video}')

# class FlightController:
#     def __init__(self, joys):
#         self.joys = joys
    
#     def show_control(self):
#         print(f'The dron move {self.joys}.')

# class Drone(Camera,FlightController):
#     def  __init__(self, video,joys,shoot):
#         Camera.__init__(self,video)
#         FlightController.__init__(self,joys)
#         self.shoot = shoot

#     def show_drone(self):
#         self.show_camara()
#         self.show_control()
#         print(f'The drone shooting {self.shoot}')
        

# s20 = Drone('marrige','center','4k')
# s20.show_drone()

""" HIERARCHICAL INHERITANCE """

""" 56. Create:
   - Parent → Shape
   - Children → Circle, Rectangle, Triangle"""

# class Shape:
#     def __init__(self, color, roop):
#         self.color = color
#         self.roop = roop
    
#     def show_shape(self):
#         print(f'It is a {self.color} {self.roop}')

# class Circle (Shape):
#     shape = 'Circle'
#     def  __init__(self, color,rad):
#         super().__init__(color,self.shape)
#         self.rad = rad

#     def area(self):
#         result = 3.14 * self.rad * self.rad
#         self.show_shape()
#         print(f'Ares = {result}')

# class Rectangle (Shape):
#     shape = 'Rectangle'
#     def  __init__(self, color,len,bre):
#         super().__init__(color,self.shape)
#         self.len = len
#         self.bre = bre

#     def area(self):
#         result = self.len * self.bre
#         self.show_shape()
#         print(f'Ares = {result}')

# class Triangle (Shape):
#     shape = 'Triangle'
#     def  __init__(self, color,len,bre):
#         super().__init__(color,self.shape)
#         self.len = len
#         self.bre = bre

#     def area(self):
#         result = self.len * self.bre * 0.5
#         self.show_shape()
#         print(f'Ares = {result}') 

# s20 = Triangle('red',10,5)
# s20.area()

# s10 = Circle('green',6)
# s10.area()

# s30 = Rectangle('Yellow',10,5)
# s30.area()

""" 57. Create:
   - Employee
   - Manager
   - Developer
   - Tester"""
# class Employee:
#     company_name ='QIS'
#     domain = '@qis.com'
#     def __init__(self, emp_id, name,email,job ='Tarinee'):
#         self.emp_id = emp_id
#         self.name = name
#         self.email = email
#         self.job = job
    
#     def show_employe(self):
#         print(f'................{self.company_name}...............')
#         print(f'{self.emp_id}   :{self.name}  :{self.email}   :{self.job}')


# class Manager (Employee):
#     job = 'Manager'
#     man_id = 1
#     def  __init__(self, first,last):
#         self.emp_id = 'M' + str(Manager.man_id)
#         Manager.man_id +=1
#         self.first = first
#         self.last = last
#         self.name = self.first + " " + self.last
#         self.email = self.last[0] + self.first + self.domain
#         super().__init__(self.emp_id,self.name,self.email, self.job)
        

#     def show_manager(self):
#         self.show_employe()


# class Developer (Employee):
#     job = 'Developer'
#     dev_id = 1

#     def  __init__(self, first,last):
#         self.emp_id = 'D' + str(Developer.dev_id)
#         Developer.dev_id +=1
#         self.first = first
#         self.last = last
#         self.name = self.first + " " + self.last
#         self.email = self.last[0] + self.first + self.domain

#         super().__init__(self.emp_id,self.name,self.email, self.job)
        

#     def show_developer(self):
#         self.show_employe()


# class Tester (Employee):
#     job = 'Tester'
#     dev_id = 1

#     def  __init__(self, first,last):
#         self.emp_id = 'T' + str(Tester.dev_id)
#         Tester.dev_id +=1
#         self.first = first
#         self.last = last
#         self.name = self.first + " " + self.last
#         self.email = self.last[0] + self.first + self.domain

#         super().__init__(self.emp_id,self.name,self.email, self.job)
        

#     def show_tester(self):
#         self.show_employe()

# s20 = Manager('shony','gang')
# s20.show_manager()

# s10 = Developer('Priya','kk')
# s10.show_developer()

# s30 = Tester('Theju','shony')
# s30.show_tester()

""" 58. Create:
   - Payment
   - UPI
   - Card
   - Wallet"""
# class Payment:
#     company_name ='VISA'
    
#     def __init__(self, amount, name,via,tran_id):
#         self.amount = amount
#         self.name = name
#         self.via = via
#         self.tran = tran_id
          
#     def show_payment(self):
#         print(f'................{self.company_name}...............')
#         print(f'Payment of {self.amount} done by :{self.name} via :{self.via}')
#         print(f'Transaction ID :{self.tran}')


# class Wallet (Payment):
#     via = 'Wallet'
#     transac = 1
#     def  __init__(self, name,amount):
#         self.tran_id = 'W' + str(Wallet.transac)
#         Wallet.transac +=1
#         self.name = name
#         self.amount = amount
        
#         super().__init__(self.amount,self.name,self.via,self.tran_id)
        

#     def show_wallet(self):
#         print('Paying from Wallet')
#         self.show_payment()


# class UPI (Payment):
#     via = 'UPI'
#     transac = 1
#     def  __init__(self, name,amount):
#         self.tran_id = 'UPI' + str(UPI.transac)
#         UPI.transac +=1
#         self.name = name
#         self.amount = amount
        
#         super().__init__(self.amount,self.name,self.via,self.tran_id)
        

#     def show_upi(self):
#         print('Paying from UPI')
#         self.show_payment()


# class Card (Payment):
#     via = 'Card'
#     transac = 1
#     def  __init__(self, name,amount):
#         self.tran_id = 'UPI' + str(Card.transac)
#         Card.transac +=1
#         self.name = name
#         self.amount = amount
        
#         super().__init__(self.amount,self.name,self.via,self.tran_id)
        

#     def show_card(self):
#         print('Paying from Card')
#         self.show_payment()
        

# s20 = Wallet('shony',5000)
# s20.show_wallet()

# s10 = UPI('Priya',4000)
# s10.show_upi()

# s30 = Card('Theju',7000)
# s30.show_card()

""" 59. Build a school system using hierarchical inheritance.

60. Create an OTT subscription system."""

""" SUPER() AND MRO QUESTIONS

61. Demonstrate usage of super().

62. Create parent and child constructors using super().

63. Demonstrate Method Resolution Order (MRO).

65. Create an e-commerce order system using super().

70. Create a cloud storage system demonstrating MRO."""

""" 64. Create a diamond inheritance structure and explain MRO."""

# class Person:
#     def show(self):
#         print('Person class')

# class Teacher (Person):
#     def show (self):
#         print('Teacher Class')

# class Researcher (Person):
#     def show (self):
#         print('Researcher class')

# class Proffesor (Teacher,Researcher):
#     pass

# m20 = Proffesor()
# m20.show()

# print(Proffesor.mro())


""" 66. Create a notification system:
   - EmailNotification
   - SMSNotification
   - PushNotification"""

# class Notification:
       
#     def __init__(self, name, type):
#         self.type = type
#         self.name = name

#     def show_notification(self):
#         print(f'..........You have a new {self.type}.................')
#         print(f'notification sent to {self.name}')

# class Email (Notification):
#     type = 'Email'
    
#     def  __init__(self, name,message):
#         self.name = name
#         self.massage = message
        
#         super().__init__(self.name,self.type)

#     def show_email(self):
#         self.show_notification()
#         print(self.massage)

# class SMS (Notification):
#     type = 'SMS'
    
#     def  __init__(self, name,message):
#         self.name = name
#         self.massage = message
        
#         super().__init__(self.name,self.type)

#     def show_sms(self):
#         self.show_notification()
#         print(self.massage)


# class Call (Notification):
#     type = 'call'
    
#     def  __init__(self, name,message):
#         self.name = name
#         self.massage = message
        
#         super().__init__(self.name,self.type)

#     def show_call(self):
#         self.show_notification()
#         print('From',self.massage)

# s20 = Email('shony','I love you')
# s20.show_email()

# s10 = SMS('Priya','I love you')
# s10.show_sms()

# s30 = Call('Theju','9035076908')
# s30.show_call()

""" 
67. Create multiple inheritance and print MRO using: ClassName.mro()

68. Build a payroll system using parent constructor reuse.

69. Create a ride-booking system using inheritance and super().
"""

""" POLYMORPHISM QUESTIONS

73. Create payment methods:
   - UPI
   - Card
   - NetBanking

74. Create a shipping system using polymorphism.

76. Build an online meeting system:
   - Zoom
   - GoogleMeet
   - Teams

77. Create an AI assistant with multiple response styles.

78. Build a notification service using polymorphism.

79. Create a report generator supporting:
   - CSV
   - JSON
   - XML

80. Create a chatbot with different language responses."""

""" 71. Create different classes with same method: pay_bill()"""

# class Electric_Bill:
#     def pay_bill(self):
#         print('Electric bill paid successfully')

# class Internet_Bill:
#     def pay_bill(self):
#         print('Internet bill paid successfully')

# class Water_Bill:
#     def pay_bill(self):
#         print('Water bill paid successfully')

# bills = [Electric_Bill(), Internet_Bill(), Water_Bill()]

# for x in bills:
#     x.pay_bill()
""" 72. Create:
   - Dog
   - Cat
   with same sound() method."""

# class Dog:
#     def sound(self):
#         print('bow bow')

# class Cat:
#     def sound(self):
#         print('Meow, meow')

# class Cow:
#     def sound(self):
#         print('mugh mugh')

# bills = [Dog (),Cat(),Cow ()]

# for x in bills:
#     x.sound()

""" 75. Create different file handlers:
   - PDF
   - DOCX
   - TXT"""

# class PDF:
#     def open(self):
#         print('open PDF')

#     def read(self):
#         print('read PDF')

#     def close(self):
#         print('close PDF')

# class DOCX:
#     def open(self):
#         print('open DOCX')

#     def read(self):
#         print('read DOCX')

#     def close(self):
#         print('close DOCX')

# class TXT:
#     def open(self):
#         print('open TXT')

#     def read(self):
#         print('read TXT')

#     def close(self):
#         print('close TXT')

# bills = [PDF (),DOCX(),TXT ()]

# for x in bills:
#     x.open()
#     x.read()
#     x.close()
#     print ()