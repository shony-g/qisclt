""" Write a program to input two numbers from the user and print their sum.
    Compare two numbers and print the larger one.
    Implement a simple calculator (+, -, *, /) using if-elif-else."""

# class Kanakk:
#     def __init__(self, a,b=1):
#         self.a = a
#         self.b = b
        
#     def sankalanam (self):
#         print('The sum is :',self.a + self.b )
    
#     def vyathyasam (self):
#         print('The difference is :',self.a - self.b )
    
#     def gunam (self):
#         print('The product is :',self.a * self.b )
    
#     def haranam (self):
#         try:
#             print('The division is :',self.a / self.b )
#         except ZeroDivisionError as e:
#             print('Not divisible by zero', e)
    
#     def utharam (self):
#         try:
#             print('The modular is :',self.a // self.b )
#         except Exception as e:
#             print('Not divisible by zero', e)
    
#     def sishttam (self):
#         try:
#             print('The modular is :',self.a % self.b )
#         except Exception as e:
#             print('Not divisible by zero', e)

#     def vargam2 (self):
#         print(f'Square of {self.a} is {self.a**2}' )
#         print(f'Square of {self.b} is {self.b**2}' )
    
#     def vargam3 (self):
#         print(f'Cube of  {self.a} is {self.a**3}' )
#         print(f'Cube of {self.b} is {self.b**3}' )
    
#     def vargamoolam(self):
#         print(f'Square root of {self.a} is {self.a**0.5}' )
    
#     def sarasari (self):
#         print('The avarage of these numbers :', (self.a + self.b)/2)

#     def tharathammyam (self):
#         if self.a == self.b:
#             print ('Both numbers are same')
#         elif self.a > self.b:
#             print(f'{self.a} is greater than {self.b}')
#         else:
#             print(f'{self.b} is greater than {self.a}')
    
# class Calculator(Kanakk):
#     def __init__(self, a, sign, b=1):
#         super().__init__(a, b)
#         if sign == "+":
#             self.sankalanam()
#         elif sign =="-":
#             self.vyathyasam()
#         elif sign =="*":
#             self.gunam()
#         elif sign =="/":
#             self.haranam()
#         else:
#             print("Invaled input")

# a1 = Kanakk(12,0)
# # a1.tharathammyam()
# a2 = Calculator(20,"/",10)


""" 2 Write a program to input a number of days and convert it into:
    a) Weeks
    b) Remaining days
    Check if a given year is a leap year.
    Write a program that takes a month number (1-12) and prints the number of days in that month.
    Check if a given date (day, month, year) is logically valid (e.g., no Feb 30).
"""
# from datetime import date, timedelta

# class Datetime_sho:

#     def __init__(self,dd,mm,yy):
#         self.day = dd
#         self.month = mm
#         self.year = yy
#         self.cal_mon = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
#         try:
#             self.start_dd = date(self.year, self.month, self.day)
#         except:
#             self.start_dd = None
#             print(f"The date you provided is {dd}-{mm}-{yy}")
#             print("Please check the date and month properly for the year")
    
#     def nthday(self,nth):
#         if self.start_dd is None:
#             print("Cannot calculate because the starting date is invalid")
#             return
        
#         self.count_day = self.start_dd + timedelta(days=nth)
#         print(f"Start date : {self.start_dd}")
#         print(f"Start day : {self.start_dd.strftime('%A')}")
#         print(f"Date after {nth} day :{self.count_day}")
#         print(f"And the Day is :{self.count_day.strftime('%A')}")
#         num_week = nth//7
#         days_rem = nth%7
#         print(f"{nth} day have {num_week} weeks and {days_rem} days")
    
#     def leap_year(self):
#         if (self.year % 400 == 0) or (self.year%4 == 0 and self.year %100 != 0):
#             print (f"{self.year} is a leap year")
#             return True
#         else:
#             print(f"{self.year} is not a leap year")
#             return False
    
#     def month_days (self):
#         mm= self.month

#         if mm not in self.cal_mon:
#             print("Invalid month number")
#         elif mm in [1, 3, 5, 7, 8, 10, 12]:
#             print(f"{self.year} {self.cal_mon[mm]} has 31 Days")
#         elif mm in [4, 6, 9, 11]:
#             print(f"{self.year} {self.cal_mon[mm]} has 30 Days")
#         elif mm == 2:
#             if self.leap_year():
#                 print(f"{self.year} {self.cal_mon[mm]} has 29 Days")
#             else:
#                 print(f"{self.year} {self.cal_mon[mm]} has 28 Days")

# check1 = Datetime_sho(2,2,2026)
# check1.nthday(150)
# check1.month_days()

"""3.  Write a program to input total seconds and convert it into:
    a) Minutes
    b) Remaining seconds
    Time Conversion: Convert 24hr format to 12hr format using conditions."""

# class Timecircus:
#     def __init__(self):
#         self.time={'Years':0,'Months':0,'Weeks':0,'Days':0,'Hours':0,'Minutes':0,'Seconds':0}
        
#     def sec_in(self, sec):
#         self.time['Minutes'] = sec//60
#         self.time['Seconds'] = sec%60
#         if self.time['Minutes'] >=60:
#             self.min_in(self.time['Minutes'])
        
#     def min_in(self,mints):
#         self.time['Hours'] = mints//60
#         self.time['Minutes'] = mints%60
#         if self.time['Hours'] >=24:
#             self.hr_in(self.time['Hours'])
        
#     def hr_in(self,hr):
#         self.time['Days'] = hr//24
#         self.time['Hours'] = hr%24
#         if self.time['Days'] >=7:
#             self.days_in(self.time['Days'])
    
#     def days_in(self,days):
#         self.time['Years'] = days//365
#         days%=365
#         if days >=30:
#             self.time['Months']=days//30
#             days%=30
#         self.time['Weeks']=days//7
#         self.time['Days']=days%7

#     def display_time(self):
#         for x,y in self.time.items():
#             if y>0:
#                 print(x ,':', y)

# class TimeCon (Timecircus):
#     def __init__(self):
#         super().__init__()
    
#     def twlve224(self,tnow, tmin=0):
#         self.clock = f"{tnow}:{tmin}AM" if tnow <=12 else f"{tnow -12}:{tmin:02d }PM"
#         print(self.clock)
    
#     def twnty212(self,tnow, tmin,am):
#         self.clock = f"{tnow}:{tmin}" if am =='AM' else f"{tnow +12}:{tmin:02d }"
#         print(self.clock)


# t1=Timecircus()
# t1.sec_in(72001122222)
# t1.days_in(375)
# t1.min_in(4000)
# t1.display_time()
# t2 = TimeCon()
# t2.twlve224(1,12)
# t2.twnty212(0,0,'AM')


""" 5. Write a program to input two numbers and swap them using arithmetic operators (without using a third variable).
"""
# num_a = int(input("Please enter first number :"))
# num_b = int(input("Please enter second number :"))
# print(f"Number A :{num_a} and number B :{num_b}")
# num_a , num_b = num_b, num_a
# print(f"Number A :{num_a} and number B :{num_b}")

""" 6. Write a program to input salary and calculate:
    a) 10% HRA
    b) 5% DA
    c) Total salary"""

# class Salary:
#     def __init__(self,bsal):
#         self.salary = bsal
#         self.earn = self.earnings()
#         self.dedu = self.deduction()
#         self.netpay = self.earn - self.dedu
        
        
#     def earnings(self):
#         basic = self.salary
#         hra = basic *0.1
#         da = basic *0.05
#         return basic + hra + da
    
#     def deduction (self):
#         basic = self.salary
#         tax = 200
#         if basic > 125000:
#             tax = basic*0.3 + tax
#             basic = basic - 125000

#         if basic >100000:
#             tax = basic*0.2 + tax
#             basic = basic - 100000
        
#         if basic >75000:
#             tax = basic*0.1 + tax
#             basic = basic - 75000

#         tax = basic*0.05 + tax

#         if tax > 75000:
#             tax = tax - 75000
#         else:
#             tax = 200
        
#         epf =3600 + 500
#         return tax + epf

#     def payslip(self):
#         print(f"Basic salary :{self.salary}")
#         print(f"Total earning (HRA + DA): {self.earn}")
#         print(f"The total deduction (TAX + PF) : {self.dedu}")
#         print(f"The net pay is: {self.netpay}")

# emp1 = Salary(75000)
# emp1.payslip()

""" Rewrite an if-else block that finds the minimum of two numbers into a single-line ternary expression.
Write a condition that avoids a "DivisionByZero" error"""

# a_num= float(input("Please ennter first number :"))
# b_num= float(input("Please ennter second number :"))
# c_num = 'Not divisible by zero' if b_num == 0 else a_num/b_num
# print(c_num)

