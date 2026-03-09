""" ************************************************************************"""
""" **********************    Beginner Level     ***************************"""
""" ************************************************************************"""

""" 1. Create a string and print it."""

# line_str = input("Please enter a string:")
# print(line_str)

""" 2. Print each character of a string using indexing."""

# line_str = input("Please enter a string:")
# len_str = len(line_str)
# for i in range(len_str):
#     print(line_str[i])

""" 3. Print the first and last character of a string."""

# line_str = input("Please enter a string:")
# print(line_str[0],line_str[-1])

""" 4. Demonstrate positive and negative indexing on a string."""

# line_str = input("Please enter a string:")
# print("Positive index starts from 0 is:",line_str[0])
# print("Positive index starts from -1 is:",line_str[-1])

""" 5. Extract the first five characters from a string using slicing."""

# line_str = input("Please enter a string:")
# print(line_str[:5])

""" 6. Reverse a string using slicing."""

# line_str = input("Please enter a string:")
# print(line_str[::-1])

""" 7. Count the length of a string without using len()."""

# line_str = input("Please enter a string:")
# num1=0
# for i in line_str:
#     num1+=1
# print(f"The lengath:{num1}")

""" 8. Convert a string to uppercase and lowercase. """

# line_str = input("Please enter a string:")
# lcase = line_str.lower()
# print(lcase)

""" 9. Capitalize the first letter of a string."""

# line_str = input("Please enter a string:")
# print(line_str.capitalize())

""" 10. Swap the case of each character in a string."""

# line_str = input("Please enter a string:")
# print(line_str.swapcase())

""" 11. Check whether a string starts with a specific substring."""

# line_str = input("Please enter a string:")
# print(f"Chcking the string starts with 'I am':{line_str.startswith('I am')}")

""" 12. Check whether a string ends with a specific substring."""

# line_str = input("Please enter a string:")
# print(f"Chcking the string ends 'you':{line_str.endswith('you')}")

""" 13. Count the number of occurrences of a character in a string."""

# line_str = input("Please enter a string:")
# print(f"Chcking 'e' in a string:{line_str.count('e')}")

""" 14. Replace a word in a string with another word."""

# line_str = input("Please enter a string:")
# print(f"replacing I with We:{line_str.replace('I','We')}")

""" 15. Remove leading and trailing spaces from a string."""

# line_str = input("Please enter a string:")
# print(f"Removing starting and trailing spaces:{line_str.strip()}")

""" ************************************************************************"""
""" ******************    Intermediate Level     ***************************"""
""" ************************************************************************"""

""" 1. Check whether a string contains only alphabets."""

# line_str = input("Please enter a string:")
# print(f"is the string contains only alphabets?:{line_str.isalpha()}")

""" 2. Check whether a string contains only digits."""

# line_str = input("Please enter a string:")
# print(f"is the string contains only digits?:{line_str.isnumeric()}")

""" 3. Check whether a string is alphanumeric."""

# line_str = input("Please enter a string:")
# print(f"is the string contains only alphanumerics?:{line_str.isalnum()}")

""" 4. Split a sentence into words using split()."""

# line_str = input("Please enter a string:")
# print(f"The sentence split into words:{line_str.split()}")

""" 5. Join a list of words into a single string."""

# line_str = input("Please enter a string:").split()
# print(f"The input is:{line_str}")
# print(f"By joining the words using white space:{" ".join(line_str)}")
# print(f"By joining the words using *:{"*".join(line_str)}")

""" 6. Find the first occurrence of a substring in a string."""

# line_str = input("Please enter a string:")
# print(f"The first occurrence of 'you' into words:{line_str.find('you')}")

""" 7. Find the last occurrence of a substring in a string."""

# line_str = input("Please enter a string:")
# print(f"The last occurrence of 'you' into words:{line_str.rfind('you')}")

""" 8. Remove a prefix from a string"""

# line_str = input("Please enter a string:")
# print(f"prefix 'I' removed:{line_str.removeprefix('I')}")

""" 9. Remove a suffix from a string."""

# line_str = input("Please enter a string:")
# print(f"Trailing 'you' removed:{line_str.removesuffix('you')}")

""" 10. Center align a string within a given width."""

# line_str = input("Please enter a string:")
# print(f"Center align with space:{line_str.center(20)}")
# print(f"Center align with '*'  :{line_str.center(20,'*')}")

""" 11. Left justify and right justify a string."""

# line_str = input("Please enter a string:")
# print(f"Left justify align with space:{line_str.ljust(20)}")
# print(f"Left justify align with '*'  :{line_str.ljust(20,'*')}")
# print(f"right justify align with space:{line_str.rjust(20)}")
# print(f"right justify align with '*'  :{line_str.rjust(20,'*')}")

""" 12. Pad a number string with zeros using zfill()."""

# line_str = input("Please enter a number:")
# print(f"Adjusted for 10 digit:{line_str.zfill(10)}")

""" 13. Use format() method in string formatting."""

# name = 'Shony'
# age = '45'
# place = 'Kozhikode'
# s3 ='Hello, I am {}, and I am {} years old. I am from {}'.format(name,age,place)
# s1 ='Hello, I am {1}, and I am {2} years old. I am from {0}'.format(name,age,place)
# s2 ='Hello, I am {0}, and I am {1} years old. I am from {2}'.format(name,age,place)
# print (f"S1 is with wrong indication :{s1}\n S2 is with proper indication :{s2}\nS3 is with blank indication :{s3}")

""" 14. Create a formatted string using f-strings."""

# name = 'Shony'
# age = '45'
# place = 'Kozhikode'
# s3 ='Hello, I am {}, and I am {} years old. I am from {}'.format(name,age,place)
# s1 ='Hello, I am {1}, and I am {2} years old. I am from {0}'.format(name,age,place)
# s2 ='Hello, I am {0}, and I am {1} years old. I am from {2}'.format(name,age,place)
# print (f"S1 is with wrong indication :{s1}\n S2 is with proper indication :{s2}\nS3 is with blank indication :{s3}")

""" 15. Use partition() to split a string into three parts."""

# line_str = input("Please enter a string:")
# print(f"Partitioned the string with white space:{line_str.partition(" ")}")
# print(f"Partitioned the string with word 'you':{line_str.partition("you")}")

""" ************************************************************************"""
""" ******************  Logical Problem Solving  ***************************"""
""" ************************************************************************"""

""" 1. Check whether a string is a palindrome."""

# line_str = input("Please enter a string:")
# case_line = line_str.lower()
# copy_line = case_line[::-1]
# print( case_line, copy_line)

# if case_line==copy_line:
#     print("palindrome")
# else:
#     print("Not a palindrome")

""" 2. Count the number of vowels and consonants in a string."""

# line_str = input("Please enter a string:")
# s=line_str.lower()

# vow= 0
# con = 0

# for i in s:
#     if i in 'aeiou':
#         vow+=1
#     else:
#         con+=1

# print(f"There are {vow} vowels and {con} consonants")

""" 3. Remove duplicate characters from a string."""

# line_str = input("Please enter a string:")
# s=line_str.lower()

# p = ""

# for i in s:
#     if i not in p:
#         p = p + i

# print(f"{p}")

""" 4. Find the most frequent character in a string."""

# line_str = input("Please enter a string:")
# s=line_str.lower()

# p = ""
# a = 0
# b = 0

# for i in s:
#     if i in s:
#         a= s.count(i)
#         if a > b:
#             b=a
#             p=i

# print(f"Most frequent character is :{p} repated {b} times")


""" 5. Check if two strings are anagrams."""

# line_str1 = input("Please enter first string:")
# line_str2 = input("Please enter second string:")
# line_str3 = line_str2[::-1]

# if line_str3 == line_str1:
#     print("Two strings are anagrams")
# else:
#     print("Not anagrams")

""" 6. Reverse each word in a sentence without reversing the sentence order."""

# line_str = input("Please enter a string:")

# s= line_str.split()

# s3=""

# for i in s:
    
#     s2 = i[::-1]
#     print(s2)
#     s3 = s3 + " " + s2

# print(s3.strip(" "))

""" 7. Find the longest word in a sentence."""

# line_str = input("Please enter a string:")

# s= line_str.split()

# p = ""
# a = 0
# b = 0

# for i in s:
#     a= len(i)
#     if a > b:
#             b=a
#             p=i

# print(f"the longest word in the sentence is:{p} have {b} characators")

""" 9. Remove all spaces from a string."""

# line_str = input("Please enter a string:")

# s=line_str.replace(" ","")

# print(s)

""" 10. Convert the first letter of every word to uppercase without using title()."""

# line_str = input("Please enter a string:")

# s= line_str.split()

# s2 =""

# for i in s:

#     s1 = i.capitalize()
#     s2 = s2 + " " +s1
# print(s2.strip())

""" 11. Extract digits from a string and store them separately"""

# line_str = input("Please enter a alpaha numeric string:")

# s2=""
# s3=""

# for i in line_str:
#     if 47 < ord(i) <58:
#         s2+=i
#     else:
#         s3+=i

# print(f"extracted numbers :{s2} and remaining string is :{s3}")

""" 12. Count the number of words in a sentence."""

# line_str = input("Please enter a string:")

# s= line_str.split()

# num1 = 0

# for i in s:
#     num1+=1
# print(f"There are total {num1} words in the sentence")

""" 13. Replace multiple spaces with a single space."""

# line_str = input("Please enter a string:")

# s=line_str.replace("  "," ")

# s=s.replace("  "," ")

# print(s)

""" 14. Check whether a string contains special characters."""

# line_str = input("Please enter a string:")

# if line_str.isalnum():
#     print(" No special characters  ")
# else:
#     print(" Special characters  ")    

""" 15. Find the ASCII value of each character."""

# line_str = input("Please enter a string:")

# for i in line_str:
#     print (f"The ASCII of {i} is {ord(i)}")

"""  8. Compress a string (example: aaabb → a3b2). """

# line_str = input("Please enter a string:")

# s=line_str
# p=""
# a=1

# for i in range(1,len(line_str)):
#     if s[i-1]==s[i]:
#         a+=1
#     else:
#         p=p+s[i-1]
#         if a>1:
#             p=p+str(a)
#             a=1
# if a>1:
#     p=p+s[-1]+ str(a)
# else:
#     p=p+s[-1]
# print(p)