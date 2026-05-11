""" 🔹 Section A: Basic File Opening (r mode)

🔹 Section C: Read + Write Mode (r+)
Write a program to open a file in r+ mode and display content.
Write a program to read a file and then write additional data using r+.
Write a program to overwrite the beginning of a file using r+.
Write a program to modify the first line of a file using r+.
Write a program to read and append data using r+.
Write a program to move file pointer and write data.
Write a program to demonstrate pointer position in r+ mode.
Write a program to update specific content in a file using r+.
Write a program to replace a word in a file using r+.
Write a program to read and rewrite file content using r+.
🔹 Section D: Mixed Practice Questions
Write a program to copy content from one file to another using r and w.
Write a program to merge two files into a third file.
Write a program to read file and write only vowels into another file.
Write a program to read file and write only consonants into another file.
Write a program to read numbers from file and write their squares into another file.
Write a program to read file and remove blank lines.
Write a program to read file and write reversed lines into another file.
Write a program to read file and count frequency of a word.
Write a program to read file and write unique words into another file.
Write a program to read file and write lines starting with a vowel into another file.
🔹 Section E: Small Practical Tasks
Create a file student.txt, write student names, then read and display them.
Create a file marks.txt, write marks, then read and calculate total.
Create a file and update its first line using r+.
Read a file and duplicate its content into another file.
Write a program to demonstrate all three modes (r, w, r+) in one program."""

""" Write a Python program to open a file in read (r) mode and display its content."""
# with open ("sample.txt", "r") as f:
#     print(f.read())

""" Write a program to read the first 10 characters from a file."""
# with open ("sample.txt", "r") as f:
#     print(f.read(10))

""" Write a program to print all lines using a loop."""
# with open ("sample.txt", "r") as f:
#     for x in f:
#         print(x)

""" Write a program to count total characters in a file."""

# with open ("sample.txt", "r") as f:
#     tot_C = 0
#     for x in f:
#         tot_C += len(x)
#     print(f"Total char in file :{tot_C}")

""" Write a program to count total lines in a file."""

# with open ("sample.txt", "r") as f:
#     tot_C = 0
#     for x in f:
#         tot_C += 1
#     print(f"Total lines in file :{tot_C}")

""" Write a program to display only the first line of a file."""

# with open ("sample.txt", "r") as f:
#     print(f.readline())
    
""" Write a program to display the last line of a file."""

# with open ("sample.txt", "r") as f:
#     lines = f.readlines()

# print(lines[-1])

""" Write a program to read a file and print it in uppercase."""

# with open ("sample.txt", "r") as f:
#     lines = f.read()
#     abb = lines.upper()
    
# print(abb)

""" Write a program to read a file and count number of words."""

# with open ("sample.txt", "r") as f:
#     lines = f.read()
#     abb = lines.split()
    
# print(len(abb))

""" Write a program to check what happens if file does not exist in r mode."""

# with open ("sample1.txt", "r") as f:
#     print(f.read())

""" Write a program to read a file using with statement."""

# with open ("sample.txt", "r") as f:
#     print(f.read())

""" Write a program to check if file is closed after reading."""

# with open ("sample.txt", "r") as f:
#     print(f.read())

# print(f.closed)

""" Write a program to print alternate lines from a file."""

# with open ("sample.txt", "r") as f:
#     abb = f.readlines()

# for i in range(0, len(abb), 2):
#     print(abb[i])

""" Write a program to read file content and reverse it."""

# with open ("sample.txt", "r") as f:
#     abb = f.read()

# bba = abb[::-1]
# print(bba)

""" 🔹 Section B: Writing Files (w mode)"""

""" Write a program to create a file using write (w) mode."""
# with open ("test.txt",'w') as f:
#     f.write("Hello World")

""" Write a program to write a single line into a file."""

# with open ("test.txt",'w') as f:
#     f.write("Welcome to Ooty")

""" Write a program to write multiple lines into a file."""

# with open ("test.txt",'w') as f:
#     f.write("Welcome to Ooty \n Hello how are you")

""" Write a program to overwrite existing file content."""

# with open ("test.txt",'w') as f:
#     f.write("Hello World")

""" Write a program to write user input into a file."""

# uinp = input("Please enthe the strings:")

# with open ("test.txt",'w') as f:
#     f.write(uinp)

""" Write a program to create a file and write numbers from 1 to 10."""

# with open ("test.txt",'w') as f:
#     for i in range (1,11):
#         f.write(str(i) + "\n")

""" Write a program to write a list of names into a file."""
# lst = input("Please enter the names with space:").split()
# print(lst)

# with open ("test.txt",'w') as f:
#     for i in range (0,len(lst)):
#         f.write(lst[i] + "\n")

""" Write a program to write formatted text into a file."""

# name = 'shony'
# age = '45'
# place = 'Kozhikode'

# with open ("test.txt",'w') as f:
#     f.write(f"Name : {name}\n")
#     f.write (f"Age : {age}\n")
#     f.write(f"City : {place}\n")

""" Write a program to write content and close the file manually."""

# f = open("test.txt",'w')
# f.write("Hello World")
# f.close()

# print(f.closed)

""" Write a program using with statement to write into a file."""

# with open ('test.txt','w')as f:
#     f.write("Hello Kozhikode")

""" Write a program to demonstrate that w mode overwrites existing data."""

# with open ('test.txt','w')as f:
#     f.write("Hello World")

""" Write a program to write a paragraph into a file."""
# cont = "7, Kiran,26, Kochi 8,Hannah,36, Bangalore 9,Ibrahim,31, Hyderabad 10,Bob,37, Bangalore 11,Zane,20, Bangalore 12,Wendy,39, Kolkata "

# with open ('test.txt','w')as f:
#     f.write(cont)

""" Write a program to write data and check file size."""

cont = "7, Kiran,26, Kochi 8,Hannah,36, Bangalore 9,Ibrahim,31, Hyderabad 10,Bob,37, Bangalore 11,Zane,20, Bangalore 12,Wendy,39, Kolkata "

# with open ('test.txt','w')as f:
#     f.write(cont)

# import os

# fsiz = os.path.getsize('test.txt')

# print(fsiz)

""" Write a program to write lowercase letters into a file."""

# with open('test.txt', 'w')as f:
#     for x in range (ord('a'),ord('z')+1):
#         f.write(chr(x) + " ")

""" Write a program to write even numbers into a file."""

# with open('test.txt', 'w')as f:
#     for x in range (2,21,2):
#         f.write( str(x) + " ")