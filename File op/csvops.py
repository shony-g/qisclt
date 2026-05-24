""" Section 1: Basic File Operations """

""" Open the CSV file using open() in read mode and print its contents."""
# with open ("sample_data_50.csv",'r') as f:
#     print(f.read())

""" Count the total number of lines in the file."""
# with open ("sample_data_50.csv",'r') as f:
#     abb = f.readlines()

# print(len(abb))

""" Read only the first 5 rows from the file."""
# with open ("sample_data_50.csv",'r') as f:
#     for i in range(6):
#         print(f.readline())

""" Read the file line by line using readline()."""
# with open ("sample_data_50.csv",'r') as f:
#     line = f.readline()
#     while line:
#         print(line.strip())
#         line = f.readline()

""" Read all lines using readlines() and display them."""
# with open ("sample_data_50.csv",'r') as f:
#     abb = f.readlines()

# for x in abb:
#     print(x.strip())

""" Print only the header row of the CSV file."""
# with open ("sample_data_50.csv",'r') as f:
#     line = f.readline()

# print(line.strip())

""" Check whether the file exists before opening it."""
# import os

# if os.path.exists('sample_data_50.csv'):
#     with open ('sample_data_50.csv') as f:
#         abb= f.read()
#         print(abb)
# else:
#     print("File not exists")

""" Close the file manually after reading."""

# f = open ("sample_data_50.csv",'r')
# line = f.read()
# print(line.strip())
# f.close()

""" Use with statement to open and read the file."""

# with open('sample_data_50.csv','r') as f:
#     abb = f.read()

# print(abb)

""" Print file size in bytes."""
# import os

# print(os.path.getsize('sample_data_50.csv'))
# # print(len('sample_data_50.csv'))

""" 🔹 Section 2: Working with CSV Data"""

""" Read the CSV file using the csv module."""
# import csv

# with open ('sample_data_50.csv', 'r')as f:
#     abb = csv.reader(f)

#     for x in abb:
#         print(x)

""" Print all rows as lists."""
# import csv

# with open ('sample_data_50.csv', 'r')as f:
#     abb = csv.reader(f)

#     for x in abb:
#         print(x)

""" Print all rows as dictionaries using DictReader."""
# import csv

# with open ('sample_data_50.csv','r')as f:
#     abb = csv.DictReader(f)

#     for x in abb:
#         print(x)

"""Extract and print all names from the file."""

# import csv

# with open ('sample_data_50.csv', 'r')as f:
#     abb = csv.DictReader(f)

#     for x in abb:
#         print(x['Name'])

""" Extract and print all cities."""

# import csv

# with open ('sample_data_50.csv', 'r')as f:
#     abb = csv.DictReader(f)

#     for x in abb:
#         print(x['City'])

""" Count how many records are there in total."""

# import csv

# count = 0
# with open ('sample_data_50.csv', 'r')as f:
#     abb = csv.DictReader(f)
    
#     for x in abb:
#         count+=1

# print(f"Number of records : {count}")

""" Print records where Age > 30."""

# import csv

# with open ('sample_data_50.csv', 'r')as f:
#     abb = csv.DictReader(f)

#     for x in abb:
#         if int(x['Age']) > 30:
#             print(x)

""" Print records where City = "Kochi"."""
# import csv

# with open ('sample_data_50.csv', 'r')as f:
#     abb = csv.DictReader(f)

#     for x in abb:
#         if x['City'] == 'Kochi':
#             print(x)

""" Count how many people belong to each city."""
# import csv

# city_count = {}

# with open ('sample_data_50.csv', 'r')as f:
#     abb = csv.DictReader(f)

#     for x in abb:
#         city = x['City']

#         if city in city_count:
#             city_count[city] += 1
#         else:
#             city_count[city] = 1

# print(city_count)

""" Find the maximum age in the dataset."""
# import csv

# age = 0

# with open ('sample_data_50.csv', 'r')as f:
#     abb = csv.DictReader(f)

#     for x in abb:
#         if int(x['Age']) > age :
#             age = int(x['Age'])

# print(f"Max Age is: {age} ")

""" 🔹 Section 3: Writing to CSV """

""" Create a new CSV file and write 5 records manually."""

# import csv

# with open ("newcsv.csv",'w', newline="") as f:
#     abb = csv.writer(f)
#     abb.writerow(['Name', 'Age', 'City'])
#     abb.writerow(['shony',45,'kozhikode'])
#     abb.writerow(['priya',42,'ChaiyumK'])
#     abb.writerow(['Teju',12,'Iringath'])
#     abb.writerow(['Dheeraj',15,'Payyoli'])
#     abb.writerow(['Gangadharan',74,'iringath'])

""" Copy contents from original file to a new file."""

# import csv

# with open ("sample_data_50.csv",'r', newline="") as f:
#     abb = csv.reader(f)

#     with open('newcsv.csv','w', newline="")as f1:
#         bcc = csv.writer(f1)

#         for x in abb:
#             bcc.writerow(x)
    
""" Append a new record to the existing CSV file."""

# import csv

# with open ("newcsv.csv",'a', newline="") as f:
#     abb = csv.writer(f)
#     abb.writerow(['Name', 'Age', 'City'])
#     abb.writerow(['shony',45,'kozhikode'])
#     abb.writerow(['priya',42,'ChaiyumK'])
#     abb.writerow(['Teju',12,'Iringath'])
#     abb.writerow(['Dheeraj',15,'Payyoli'])
#     abb.writerow(['Gangadharan',74,'iringath'])

""" Write only names and ages to a new file."""

# import csv

# with open ('sample_data_50.csv', 'r')as f:
#     abb = csv.DictReader(f)

#     with open ('nameage.csv','w',newline="")as f1:
#         bcc = csv.writer(f1)

#         bcc.writerow(['Name','Age'])
#         for x in abb:
#             bcc.writerow([x['Name'],x['Age']])

""" Save filtered data (Age > 25) into a new CSV."""

# import csv

# with open ('sample_data_50.csv', 'r')as f:
#     abb = csv.DictReader(f)

#     with open ('nameage.csv','w',newline="")as f1:
#         bcc = csv.writer(f1)
#         bcc.writerow(['ID','Name','Age','City'])
#         for x in abb:
#             if int(x['Age']) >25:
#                 bcc.writerow([x['ID'],x['Name'],x['Age'],x['City']])

""" Write a CSV file with custom delimiter (e.g., ;)."""
# import csv

# with open ("newcsv2.csv",'w', newline="") as f:
#     abb = csv.writer(f, delimiter=';')
#     abb.writerow(['Name', 'Age', 'City'])
#     abb.writerow(['shony',45,'kozhikode'])
#     abb.writerow(['priya',42,'ChaiyumK'])
#     abb.writerow(['Teju',12,'Iringath'])
#     abb.writerow(['Dheeraj',15,'Payyoli'])
#     abb.writerow(['Gangadharan',74,'iringath'])

""" Write a file with uppercase names."""

# import csv

# with open ('sample_data_50.csv', 'r')as f:
#     abb = csv.DictReader(f)

#     with open ('newcsv2.csv','w',newline="")as f1:
#         bcc = csv.writer(f1)

#         bcc.writerow(['Name','Age'])
#         for x in abb:
#             bcc.writerow([x['Name'].upper(),x['Age']])

""" Remove duplicate rows (if any) and write to new file."""

# import csv
# new_data = set()
# with open ("sample_data_50.csv",'r') as f:
#     abb = csv.reader(f)

#     with open('newcsv2.csv','w', newline="")as f1:
#         bcc = csv.writer(f1)

#         for x in abb:
#             row_top = tuple(x)
#             if row_top not in new_data:
#                 new_data.add(row_top)
#                 bcc.writerow(x)

""" Write sorted data based on Age."""

# import csv
# new_data = []
# with open ("sample_data_50.csv",'r') as f:
#     abb = csv.DictReader(f)
#     for x in abb:
#         new_data.append(x)

# print(new_data)

# new_data.sort(key=lambda z: int(z["Age"]))

# with open('newcsv3.csv','w', newline="")as f1:
#         fieldnames = ["ID","Name","Age","City"]
#         bcc = csv.DictWriter(f1,fieldnames=fieldnames)
#         bcc.writeheader()
#         for y in new_data:
#             bcc.writerow(y)

"""Write data in reverse order."""

# import csv
# new_data = []
# with open ("sample_data_50.csv",'r') as f:
#     abb = csv.DictReader(f)
#     for x in abb:
#         new_data.append(x)

# acc = new_data[::-1]

# with open('newcsv4.csv','w', newline="")as f1:
#         fieldnames = ["ID","Name","Age","City"]
#         bcc = csv.DictWriter(f1,fieldnames=fieldnames)
#         bcc.writeheader()
#         for y in acc:
#             bcc.writerow(y)

""" 🔹 Section 4: Data Processing"""

""" Calculate average age of all records."""
# import csv
# tot =0
# count = 0

# with open ("sample_data_50.csv",'r') as f:
#     abb = csv.DictReader(f)
#     for x in abb:
#         tot += int(x['Age'])
#         count+=1

# avg = tot/count

# print(avg)

""" Find youngest person in the dataset."""

# import csv
# yPer =""
# yAge = 100

# with open ("sample_data_50.csv",'r') as f:
#     abb = csv.DictReader(f)
#     for x in abb:
#         if int(x['Age']) < yAge:
#             yPer = x
#             yAge = int(x['Age'])
      

# print(yPer)

""" Find oldest person in the dataset."""

# import csv
# yPer =""
# yAge = 0

# with open ("sample_data_50.csv",'r') as f:
#     abb = csv.DictReader(f)
#     for x in abb:
#         if int(x['Age']) > yAge:
#             yPer = x
#             yAge = int(x['Age'])
      

# print(yPer)

""" Count how many people are from each city."""

# import csv

# city_count = {}

# with open ('sample_data_50.csv', 'r')as f:
#     abb = csv.DictReader(f)

#     for x in abb:
#         city = x['City']

#         if city in city_count:
#             city_count[city] += 1
#         else:
#             city_count[city] = 1

# print(city_count)

""" Display names of people whose age is between 25–30."""

# import csv
# new_data = set()
# with open ("sample_data_50.csv",'r') as f:
#     abb = csv.DictReader(f)

#     with open('agename.txt', 'w') as f2:
#         for x in abb:
#             age = int(x['Age'])

#             if 25<age<30:
#                 f2.write(x['Name'] + "\n")

    # with open('newcsv4.csv','w', newline="")as f1:
    #     fname= ['ID', 'Name','Age','City']
    #     bcc = csv.DictWriter(f1, fieldnames=fname)

    #     bcc.writeheader()

    #     for x in abb:
    #         if 25 < int(x['Age']) <30:
    #             bcc.writerow(x)

    
""" Replace all city names "Delhi" with "New Delhi"."""

# import csv
# new_data = set()
# with open ("sample_data_50.csv",'r') as f:
#     abb = csv.DictReader(f)

#     with open('newcsv4.csv','w', newline="")as f1:
#         fname= ['ID', 'Name','Age','City']
#         bcc = csv.DictWriter(f1, fieldnames=fname)

#         bcc.writeheader()

#         for x in abb:
#             if x['City'] == "Delhi":
#                 x['City'] = 'New Delhi'
#                 bcc.writerow(x)
#             else:
#                 bcc.writerow(x)

""" Convert all names to lowercase."""

# import csv

# with open ("sample_data_50.csv",'r') as f:
#     abb = csv.DictReader(f)

#     with open('newcsv4.csv','w', newline="")as f1:
#         fname= ['ID', 'Name','Age','City']
#         bcc = csv.DictWriter(f1, fieldnames=fname)

#         bcc.writeheader()

#         for x in abb:
#             x['Name'] = x['Name'].lower()
#             bcc.writerow(x)

""" Add a new column "Status" (Adult/Young based on age)."""

# import csv

# with open ("sample_data_50.csv",'r') as f:
#     abb = csv.DictReader(f)

#     with open('newcsv4.csv','w', newline="")as f1:
#         fname= ['ID', 'Name','Age','City','Status']
#         bcc = csv.DictWriter(f1, fieldnames=fname)

#         bcc.writeheader()

#         for x in abb:
#             age = int(x['Age'])

#             if age > 30:
#                 x['Status'] = 'Adult'
#             else:
#                 x['Status'] = 'Young'
            
#             bcc.writerow(x)

""" Create a new CSV with only unique cities."""

# import csv

# city_count = set()

# with open ('sample_data_50.csv', 'r')as f:
#     abb = csv.DictReader(f)

#     for x in abb:
#         city = x['City']

#         if city not in city_count:
#             city_count.add(city)
        

# print(city_count)

""" Merge two CSV files (create another sample file)."""

# import csv

# with open("merge.csv",'w', newline="") as fk:
#     eaa = csv.writer(fk)

#     with open ('sample_data_50.csv', 'r')as f:
#         abb = csv.reader(f)

#         for x in abb:
#             eaa.writerow(x)

#     with open ('newcsv4.csv', 'r')as f1:
#         acc = csv.reader(f1)

#         next(acc)

#         for x in acc:
#             eaa.writerow(x)

""" 🔹 Section 5: Intermediate Tasks
Search for a record by name.
Update age of a specific person and rewrite file.
Delete a record based on ID.
Sort data by Name alphabetically.
Group data by City and display counts.
Find top 5 oldest people.
Find average age per city.
Validate data (check for missing values).
Handle exceptions while opening file.
Build a menu-driven program:
View records
Add record
Delete record
Search record"""
import csv
with open ("sdap.csv",'a+', newline="") as f:
        abb = csv.writer(f)
        acc = csv.DictReader(f)
        # sno = acc[S NO]
        print(acc)
        abb.writerow([])