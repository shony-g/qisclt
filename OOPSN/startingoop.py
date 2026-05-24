"""" Basic Level"""

""" 1. Student Class
Create a class named Student.
Add a class attribute school_name = "ABC School"
Create two objects.
Display the school name using both objects."""

# class Student:
#     school_name = "THS School"

# shony = Student()
# priya = Student()

# print(shony.school_name)
# print(priya.school_name)

# priya.school_name = "GVHS Thiruvallur"

# print(shony.school_name)
# print(priya.school_name)

""" 2. Mobile Class

Create a class named Mobile.

Add class attributes:
brand = "Samsung"
country = "Korea"
Create an object and print both attributes."""

# class Mobile:
#     brand = 'Sansung'
#     Country = 'Korea'

# Galaxy = Mobile()
# Note = Mobile()

# Note.Country = 'India'
# print(Galaxy.brand)
# print(Galaxy.Country)

# print(Note.brand)
# print(Note.Country)

""" 3. Employee Class

Create a class named Employee.

Add a method show_company() that prints:
"Company Name: TechSoft"
Create an object and call the method."""

# class Employee:
#     def show_company(self):
#         print("Company Name: TechSoft")

# shony = Employee()

# shony.show_company()

""" 4. Car Class

Create a class named Car.

Add class attribute wheels = 4
Create two objects.
Print the number of wheels using both objects."""

# class Car:
#     number_of_wheels = 4

# Alto = Car()
# City = Car()

# print(Alto.number_of_wheels)
# print(City.number_of_wheels)

""" 5. College Class

Create a class named College.

Add a class attribute college_name = "Green Valley College"
Add a method display() to print the college name.
Create an object and call the method.
Intermediate Level"""

# class College:
#     college_name = "Green Vally College"
#     def display(self):
#         print(College.college_name)

# richu = College()

# richu.display()

""" 6. Laptop Class Attribute Updation

Create a class named Laptop.

Add class attribute brand = "Dell"
Print the brand.
Update the class attribute to "HP"
Print the updated value."""

# class Laptop:
#     brand = "Dell"

# ausus = Laptop()
# print(ausus.brand)

# Laptop.brand = 'HP'

# print(ausus.brand)

""" 7. Hospital Class

Create a class named Hospital.

Add class attribute hospital_name = "City Hospital"
Add method show() to display the hospital name.
Create two objects and call the method using both objects."""

# class Hospital:
#     hospital_name = 'City Hopital'
#     def show(self):
#         print(Hospital.hospital_name)

    
# meitra = Hospital()
# mims = Hospital()

# meitra.show()
# mims.show()

""" 8. Bus Class

Create a class named Bus.

Add class attribute seats = 40
Update the number of seats to 50
Print the updated value."""

# class Bus:
#     seats = 40

# city_bus = Bus()
# print(city_bus.seats)

# Bus.seats = 50

# print(city_bus.seats)

""" 
9. Bank Class

Create a class named Bank.

Add class attribute bank_name = "Federal Bank"
Add method display_bank() to print the bank name.
Create an object and call the method."""

# class Bank:
#     bank_name = 'Federal Bank'
#     def display_bank(self):
#         print(Bank.bank_name)

# account1= Bank()

# account1.display_bank()

""" 10. Movie Class

Create a class named Movie.

Add class attribute industry = "Mollywood"
Delete the class attribute.
Try printing the attribute after deletion.
Advanced Level"""

# class Movie:
#     industry = "Mollywood"

# ada = Movie()
# bda = Movie()
# print(ada.industry)

# del ada.industry

# print(ada.industry)
# print(bda.industry)

""" 11. Book Class

Create a class named Book.

Add class attribute library = "Central Library"
Add methods:
show_library()
update_library()
Update the library name using the method and display the updated value."""

# class Book:
#     library = "Central Library"
#     def show_library(self):
#         print(Book.library)
    
#     def update_library(self):
#         Book.library = "College Library"
#         print(Book.library)

# sun = Book()

# sun.show_library()
# sun.update_library()

""" 12. School Class Attribute Deletion

Create a class named School.

Add class attribute principal = "Ramesh"
Print the attribute.
Delete the attribute.
Handle the error if the attribute is accessed after deletion."""

# class School:
#     pricipal = 'Ramesh'

# shony = School()
# print(shony.pricipal)

# del School.pricipal

# try:
#     print(shony.pricipal)
# except AttributeError:
#     print('Error')

""" 13. TV Class

Create a class named TV.

Add class attribute company = "Sony"
Create three objects.
Update the class attribute to "LG"
Show that the updated value is reflected in all objects."""

# class TV:
#     company = 'shony'

# tv1= TV()
# tv2= TV()
# tv3= TV()

# print(tv1.company)
# print(tv2.company)
# print(tv3.company)

# TV.company = 'LG'

# print(tv1.company)
# print(tv2.company)
# print(tv3.company)

""" 14. University Class

Create a class named University.

Add class attribute country = "India"
Add method show_country()
Create multiple objects and call the method."""

# class University:
#     country = 'India'
#     def show_country (self):
#         print(University.country)

# tv1= University()
# tv2= University()
# tv3= University()

# tv1.show_country()
# tv2.show_country()
# tv2.show_country()

""" Challenge Questions """

""" 15. Restaurant Class

Create a class named Restaurant.

Add class attribute type = "Veg"
Update the attribute to "Multi Cuisine"
Delete the attribute.
Print suitable messages after each operation."""

# class Restaurant:
#     type = "Veg"

# user1 = Restaurant()

# print(user1.type)

# Restaurant.type = "Multi Cuisine"

# print(user1.type)

# del Restaurant.type

# print(user1.type)

""" 16. Company Management

Create a class named Company.

Add class attribute company_name = "Infosys"
Add methods to:
Display company name
Update company name
Delete company name"""

# class Company:
#     company_name = "Infosys"

#     def name(self):
#         print(Company.company_name)

#     def update_name(self):
#         Company.company_name = "ECI"
#         print(Company.company_name)

#     def del_name(self):
#         del Company.company_name
#         print(Company.company_name)

# plot1 = Company()

# plot1.update_name()
# plot1.name()
# plot1.del_name()
    
""" 17. Cricket Team

Create a class named CricketTeam.

Add class attribute team_name = "India"
Create multiple objects.
Change the team name to "Kerala"
Display the updated value using all objects.
18. ATM Machine

Create a class named ATM.

Add class attribute bank = "SBI"
Add method show_bank()
Delete the class attribute and check the output.
19. Airline Class

Create a class named Airline.

Add class attribute airline_name = "Air India"
Add methods to display and update the airline name.
Create two objects and test the methods.
20. Shopping Mall

Create a class named Mall.

Add class attribute mall_name = "Lulu Mall"
Create objects.
Update and delete the class attribute.
Display outputs before and after each operation."""