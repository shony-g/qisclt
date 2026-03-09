""" 1.  Write a Python program to take a string from the user and print the first character using slicing."""

# line_str = input("Please enter a string:")
# print(line_str[0])

""" 2.  Write a program to display the last character of a string using slicing."""

# line_str = input("Please enter a string:")
# print(line_str[-1])

""" 3.  Given a string, print the first 5 characters using slicing."""

# line_str = input("Please enter a string:")
# print(line_str[:5])

""" 4.  Write a program to print all characters of a string except the first one."""

# line_str = input("Please enter a string:")
# print(line_str[1:])

""" 5.  Write a program to print all characters of a string except the last  one."""

# line_str = input("Please enter a string:")
# print(line_str[:-1])

""" 6.  Given a string, print characters from index 2 to index 6."""

# line_str = input("Please enter a string:")
# print(line_str[2:7])

""" 7.  Write a program to print every character at even index positions using slicing."""

# line_str = input("Please enter a string:")
# print(line_str[::2])

""" 8.  Write a program to print every character at odd index positions using slicing."""

# line_str = input("Please enter a string:")
# print(line_str[1::2])

""" 9.  Write a program to reverse a string using slicing."""

# line_str = input("Please enter a string:")
# print(line_str[::-1])

""" 10. Given a string, print the middle character(s) using slicing (assume length can be even or odd)."""

# line_str = input("Please enter a string:")
# leng = len(line_str)
# mid=leng//2
# if leng%2==0:
#     print(f"The middle charactor is:{line_str[mid-1:mid+1]}")
# else:
#     print(f"The middle charactor is:{line_str[mid:mid+1]}")

""" 11. Write a program to check whether a string is a palindrome using slicing."""

# line_str = input("Please enter a string:")
# case_line = line_str.lower()
# copy_line = case_line[::-1]
# print( case_line, copy_line)

# if case_line==copy_line:
#     print("palindrome")
# else:
#     print("Not a palindrome")

""" 12. Given a string, extract the first half and second half using slicing and print them separately."""

# line_str = input("Please enter a string:")
# leng = len(line_str)
# mid=leng//2

# print(f"The first half:{line_str[:mid]}")
# print(f"The Second half:{line_str[mid:]}")

""" 13. Write a program to remove the first and last two characters from a string using slicing."""

# line_str = input("Please enter a string:")
# print(line_str[2:-2])

""" 14. Given a string, print characters from index 1 to the second last character."""

# line_str = input("Please enter a string:")
# print(line_str[1:-1])

""" 15. Write a program to extract every third character from a string using slicing."""

# line_str = input("Please enter a string:")
# print(line_str[::3])

""" 16. Given a string, reverse only the first half of the string using slicing."""

# line_str = input("Please enter a string:")
# leng = len(line_str)
# mid=leng//2
# fhalf = line_str[:mid:]
# rfhalf = fhalf[::-1]

# print(f"{rfhalf}{line_str[mid:]}")

""" 17. Write a program to extract the domain name from an email ID using slicing."""

# line_str = input("Please enter a email address:")
# mid = line_str.find("@")

# print(f"Domain name:{line_str[mid+1:]}")

""" 18. Given a sentence, extract and print the last word using slicing."""

# line_str = input("Please enter a string:")
# mid = line_str.rfind(" ")

# print(f"Last word:{line_str[mid+1:]}")

""" 19. Write a program to swap the first and last characters of a string using slicing."""

# line_str = input("Please enter a sentence:")

# print(f"{line_str[-1]}{line_str[1:-1]}{line_str[0]}")

""" 20. Given a string, print all characters except vowels using slicing and looping logic."""

# line_str = input("Please enter a sentence:")

# for i in line_str:
#     if i not in 'aeiou':
#         print(i, end="")

""" 21. Write a program to split a string into two parts based on a given index using slicing."""

# line_str = input("Please enter a string:")
# num1 = int(input("Please enter a index:"))

# print(f"The first half:{line_str[:num1]}")
# print(f"The Second half:{line_str[num1:]}")

""" 22. Given a string, print the string in reverse order skipping every second character."""

# line_str = input("Please enter a string:")
# print(line_str[-1::-2])

""" 23. Write a program to extract the username from an email ID using slicing."""

# line_str = input("Please enter a email address:")
# mid = line_str.find("@")

# print(f"user name:{line_str[:mid]}")

""" 24. Given a string, check whether the first half and second half are equal using slicing."""

# line_str = input("Please enter a string:")
# leng = len(line_str)
# mid=leng//2
# fhalf = line_str[:mid:]
# shalf = line_str[mid:]
# if fhalf == shalf:
#     print(f"{fhalf} and {shalf} are equeal")
# else:
#     print(f"{fhalf} and {shalf} are not equeal")

""" 25. Write a program to count how many characters are present in a substring obtained using slicing."""

# line_str = input("Please enter a string:")
# num1 = int(input("Please enter a index:"))
# a=line_str[:num1]
# b= line_str[num1:]
# print(f"The length of first :{len(a)}")
# print(f"The length of second:{len(b)}")

""" 
26. Write a program to demonstrate positive and negative indexing using
    slicing.

27. Given a string, show the difference between string[start:end] and
    string[start:end:step].

28. Write a program to demonstrate slicing with only start index, only
    end index, and only step.

29. Write a program to safely slice a string even if the index range
    exceeds the string length.

30. Write a program to show that string slicing does not modify the
    original string.
"""




