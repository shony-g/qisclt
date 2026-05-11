""" --- PART 1: DICTIONARY BASICS & CREATION ---"""

""" 1. Create a dictionary representing a 'Laptop' with keys: brand, model, and price."""

# laptop = {"brand":"Hp", "model":"Victus", "Price":56000}

# print(laptop)

""" 2. Access the value of the 'model' key using square brackets."""

# print(laptop["model"])

""" 3. Access the value of a key that doesn't exist using .get() and explain why it's safer than []."""

# print(laptop.get("model"))
# print(laptop.get("size")) ,""" give no error and give none"""
# # print(laptop["size"]) //privide error

"""" 4. Create an empty dictionary using both {} and the dict() constructor."""
# new_dict = {}
# print(type(new_dict))
# lap_top = dict()
# print(type(lap_top))

""" 5. Add a new key-value pair 'processor': 'i7' to an existing dictionary."""

# laptop = {"brand":"Hp", "model":"Victus", "Price":56000}

# laptop["processor"]= "i7"

# laptop.update({'processor':"i7"})

# print(laptop)

""" 6. Update the 'price' of the laptop to a new value."""
# laptop.update({"Price":70000})
# laptop["Price"] = 50000
# print(laptop)

""" 7. Use the len() function to find how many key-value pairs are in a dictionary."""
# print(laptop)

# print(len(laptop))

""" 8. Create a dictionary where the keys are numbers 1 to 5 and the values are their squares."""

# sqrs = {x:x**2 for x in range(1,6)}
# print(sqrs)

""" 9. Check if a specific key exists in a dictionary using the 'in' operator."""

# sqrs = {x:x**2 for x in range(1,6)}
# print(sqrs)

# num = int(input("Please enter a number:"))

# for x in sqrs:
#     if x==num:
#         print(f"{num} in the dictionary")

# print(f"not in the dictionary")

""" 10. Delete a key-value pair using the 'del' keyword and handle the case if the key is missing."""

# sqrs = {x:x**2 for x in range(1,6)}
# print(sqrs)

# num = int(input("Please enter a number:"))

# if num in sqrs:
#     del sqrs[num]
#     print (sqrs)
# else:
#     print("not in the dictionary")

""" --- PART 2: METHODS & MANIPULATION ---"""

""" 11. Use the pop() method to remove a key and store its value in a variable."""

# sqrs = {x:x**2 for x in range(1,6)}
# print(sqrs)

# num = sqrs.pop(2)
#print(sqrs)

# print(num)

""" 12. Use popitem() to remove the last inserted item and explain its behavior in Python 3.7+."""

# sqrs = {x:x**2 for x in range(1,6)}
# print(sqrs)

# num = sqrs.popitem()

# print(num)
# print(sqrs)

""" 13. Use the keys() method to print all the keys in a dictionary."""

# sqrs = {x:x**2 for x in range(1,6)}
# print(sqrs)

# for x in sqrs.keys():
#     print(x)

""" 14. Use the values() method to print all the values in a dictionary."""

# sqrs = {x:x**2 for x in range(1,6)}
# print(sqrs)

# for x in sqrs.values():
#     print(x)

"""15. Use the items() method to iterate through a dictionary and print "Key: Value" for each pair."""

# sqrs = {x:x**2 for x in range(1,6)}
# print(sqrs)

# for x,y in sqrs.items():
#     print(x, y)

""" 16. Merge two dictionaries: {'a': 1, 'b': 2} and {'c': 3, 'd': 4} using the update() method."""

# a1 = {'a': 1, 'b': 2}
# a2 = {'c': 3, 'd': 4}

# a1.update(a2)

# print(a1)

""" 17. Clear all items from a dictionary using the clear() method."""

# sqrs = {x:x**2 for x in range(1,6)}
# print(sqrs)

# sqrs.clear()

# print(sqrs)

""" 18. Use the setdefault() method to add a key 'country' with value 'India' only if it doesn't exist."""

# std1 = {'name':'shony', 'age':45}

# print(std1)

# std1.setdefault('Country', 'India')

# print(std1)

""" 19. Create a shallow copy of a dictionary and show that modifying the copy doesn't change the original."""
# std1 = {'name':'shony', 'age':45}
# print(std1)

# std2 = std1.copy()

# print(std2)

# std2['name']= 'Priyanka'

# print(std2)
# print(std1)

""" 20. Create a dictionary from two lists: one for keys and one for values using the zip() function."""

# lst1 = ['name','age','place']
# lst2 = ['shony',45,'clt']

# d1= dict(zip(lst1,lst2))

# print(lst1, lst2, d1)


""" --- PART 3: NESTED DICTIONARIES (API STYLE) ---"""

""" 21. Create a nested dictionary called 'Employees' containing data for three different people."""

# Employees = {'emp1':{'name':'shony','age':45, 'team':'python'},'emp2':{'name':'Priya','age':42, 'team':'python'}}

# print(Employees)

""" 22. Access a value inside a nested dictionary (e.g., Employees['emp1']['salary'])."""

# Employees = {'emp1':{'name':'shony','age':45, 'team':'python'},'emp2':{'name':'Priya','age':42, 'team':'python'}}

# print(Employees)

# print(Employees['emp2']['age'])

""" 23. Update a value inside a nested dictionary."""
# Employees = {'emp1':{'name':'shony','age':45, 'team':'python'},'emp2':{'name':'Priya','age':42, 'team':'python'}}

# print(Employees)

# Employees['emp2'].update({'team':'Java'})

# print(Employees)

""" 24. Add a new nested dictionary (a new employee) to the existing 'Employees' structure."""

# Employees = {'emp1':{'name':'shony','age':45, 'team':'python'},'emp2':{'name':'Priya','age':42, 'team':'python'}}

# print(Employees)

# jasi = {'name':'Jaskirat','age':42, 'team':'bensal'}

# Employees.update({'emp3':jasi})

# print(Employees)

""" 25. Write a loop to print only the names of all employees from the nested 'Employees' dictionary."""
# Employees = {'emp1':{'name':'shony','age':45, 'team':'python'},'emp2':{'name':'Priya','age':42, 'team':'python'}}

# print(Employees)

# for x in Employees.values():
#     for y in x.values():
#         print(y)

""" 26. Create a dictionary where a key points to a list of values (e.g., 'hobbies': ['coding','reading'])."""

# students ={'name':['shony',"Priyanka"], "age":[45,42],'hobbies':['python',"music",'watching movies']}

# print(students)

""" 27. Append a new hobby to the list inside that dictionary."""

# students ={'name':['shony',"Priyanka"], "age":[45,42],'hobbies':['python',"music",'watching movies']}

# print(students)
# # students['hobbies']+=['music']
# # students['hobbies'].append('music')
# # students.setdefault('hobbies',[]).append('music')
# print(students)

""" 28. Given a dictionary of students and their marks (a list), calculate the average marks for one student."""

# students = {'sho':[20,21,18,24,19],'pri':[21,22,17,23,18], 'ach':[21,24,14,21,18],}
# avar = dict()

# for x,y in students.items():
#     s=0
#     leM = len(students[x])
#     for i in y:
#         s+=i
#     avg = s/leM
#     print(f"The avarage of {x} is {avg}")
#     avar.update({x:avg})

# print(avar)

""" 29. Flatten a simple nested dictionary (convert {'a': {'b': 1}} to {('a', 'b'): 1})."""

# d= {'a': {'b': 1}}
# d2= dict()

# for x,y in d.items():
#     for i,j in y.items():
#         d2[x,i]=j

# print(d2)

""" 30. Represent a JSON response from a weather API as a nested dictionary and extract the 'temperature'."""

# weather_data = {
#     "location": "Calicut",
#     "current": {
#         "temperature": 32,
#         "humidity": 70,
#         "condition": "Sunny"
#     }
# }

# print(weather_data['current']['temperature'])

""" --- PART 4: COMPREHENSIONS & LOGIC ---"""

""" 31. [Comprehension] Create a dictionary of even numbers between 1-10 as keys and their cubes as values."""

# dEven = {x:x**3 for x in range(1,11) if x%2==0}

# print(dEven)

""" 32. [Comprehension] Given a dictionary, create a new one with only items where the value is > 100"""

# samDict = {'a':12, 'b':121,'c':89,'d':201,'e':765}

# comdic = {x:y for x,y in samDict.items() if y>100}

# print(comdic)

"""33. [Comprehension] Swap keys and values in a dictionary (Reverse Mapping). """

# samDict = {'a':12, 'b':121,'c':89,'d':201,'e':765}

# revdic = {y:x for x,y in samDict.items()}

# print(revdic)

""" 34. Sort a dictionary by its keys in alphabetical order."""

# samdic = {'lion':4,'tiger':7,'elephant':19,'dear':87}

# sordic = {x:samdic[x] for x in sorted(samdic)}

# print(sordic)

""" 35. Sort a dictionary by its values in ascending order."""

# samdic = {'lion':14,'tiger':75,'elephant':9,'dear':57}

# keySor = sorted(samdic, key=samdic.get)

# print(keySor)

# sordic = {x:samdic[x] for x in keySor}

# print(sordic)

""" 36. Find the key with the maximum value in a dictionary of product prices."""

# samdic = {'veg':50, 'grilled':450,'brosted':650, "boiled":250, 'meat':200}

# keySor = sorted(samdic,key=samdic.get)

# d= keySor[-1]

# print(f"cosltly key :{d}")

""" 37. Count the frequency of each character in a string "Python Trainer" using a dictionary."""

# str1 = "Python trainer"

# kalidic = dict()

# for x in str1:
#     kalidic.setdefault(x, str1.count(x))

# print(kalidic)

""" 38. Combine two dictionaries by adding values for common keys."""

# samdic1 = {'veg':50, 'grilled':450,'Paneer':650, "boiled":250, 'meat':200}

# samdic2 = {'veg':50, 'Sabji':450,'brosted':650, "Moru":250, 'meat':200}

# d = samdic1.copy()

# for x,y in samdic2.items():
#     d[x] = d.get(x,0) + y

# print(d)

""" 39. Convert a dictionary into a list of tuples."""

samdic1 = {'veg':50, 'grilled':450,'Paneer':650, "boiled":250, 'meat':200}

lisdic = list(samdic1.items())

print(lisdic)

""" 40. Check if all values in a dictionary are the same."""

# samdic1 = {'veg':50, 'grilled':50,'Paneer':50, "boiled":50, 'meat':50}

# setdic = {x for x in samdic1.values()}

# if len(setdic) == 1:
#     print(f"all valuses in Dict are same: {setdic}")
# else:
#     print(f"all valuses in Dict are not same: {setdic}")


""" 
--- PART 5: INDUSTRIAL & INTERVIEW SCENARIOS ---
41. [JSON] Use the 'json' module to convert a dictionary into a JSON string.
42. [Data Cleaning] Remove all keys from a dictionary that have None or empty string
values.
43. [Security] Explain why a list cannot be used as a dictionary key, but a tuple can.
44. [Logic] Write a program to find the sum of all values in a numeric dictionary.
45. [Simulation] Use a dictionary to simulate a simple "Switch-Case" statement logic.
46. [Efficiency] Compare the time it takes to find a value in a list of 10,000 items vs. a
dictionary.
47. [Functionality] Use **kwargs in a function to accept arbitrary keyword arguments as a
dictionary.
48. [Mapping] Create a dictionary to map Roman numerals to Integers (e.g., 'I': 1, 'V': 5).
49. [Logic] Given a list of words, group them by their starting letter using a dictionary.
50. [Interview Question] Explain the difference between '==' and 'is' when comparing two
identical dictionaries."""