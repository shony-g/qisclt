# """
# Print this pattern:

# 1)```text
# *
# **
# ***
# ****
# *****
# ```

# 2)```text
# *****
# ****
# ***
# **
# *
# ```

# 3)```text
# *****
# *****
# *****
# *****
# *****
# ```

# 4)```text
#     *
#    **
#   ***
#  ****
# *****
# ```
# 5)```text
# *****
#  ****
#   ***
#    **
#     *
# ```
# 6)```text
# 1
# 12
# 123
# 1234
# 12345
# ```
# 7)```text
# 1
# 22
# 333
# 4444
# 55555
# ```
# 8)```text
# 1
# 21
# 321
# 4321
# 54321
# ```
# 9)```text
# 12345
# 1234
# 123
# 12
# 1
# ```
# 10)```text
# 1
# 23
# 456
# 78910
# ```

# 11)```text
#     *
#    ***
#   *****
#  *******
# *********
# ```

# 12)```text
# *********
#  *******
#   *****
#    ***
#     *
# ```
# 13) ```text
#     1
#    121
#   12321
#  1234321
# 123454321
# ``` 

# 14)```text
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# ```
# 15)```text
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# ``` 
# 16)```text
# 1
# 12
# 123
# 1234
# 12345
# 1234
# 123
# 12
# 1
# ``` 
# 17)```text
# *****
# *   *
# *   *
# *   *
# *****
# ``` 


# 18)```text
# 1
# 01
# 101
# 0101
# 10101
# ```

# """

# class For_pattern:
#     def __init__(self,num):
#         self.num = num
        
#     def pattern1 (self):
#         a = self.num
#         for i in range(1,a+1):
#             for j in range(i):
#                 print ("*", end="")
#             print()
    
#     def pattern2 (self):
#         a = self.num
#         for i in range(a,0,-1):
#             for j in range(i):
#                 print ("*", end="")
#             print()
    
#     def pattern3 (self):
#         a = self.num
#         for i in range(a,0,-1):
#             for j in range(a):
#                 print ("*", end="")
#             print()

#     def pattern4 (self):
#         a = self.num
#         for i in range(1,a+1):
#             for j in range(a-i):
#                 print (" ", end="")
#             for k in range(i):
#                 print ("*", end="")
#             print()
    
#     def pattern5 (self):
#         a = self.num
#         for i in range(a,0,-1):
#             for j in range(a-i):
#                 print (" ", end="")
#             for k in range(i):
#                 print ("*", end="")
#             print()
    
#     def pattern6 (self):
#         a = self.num
#         for i in range(1,a+1):
#             for j in range(1,i+1):
#                 print (j, end="")
#             print()

#     def pattern7 (self):
#         a = self.num
#         for i in range(1,a+1):
#             for j in range(1,i+1):
#                 print (i, end="")
#             print()
    
#     def pattern8 (self):
#         a = self.num
#         for i in range(1,a+1):
#             for j in range(i,0,-1):
#                 print (j, end="")
#             print()
    
#     def pattern9 (self):
#         a = self.num
#         for i in range(a,0,-1):
#             for j in range(1,i+1):
#                 print (j, end="")
#             print()

#     def pattern10 (self):
#         a = self.num
#         b=1
#         for i in range(1,a):
#             for j in range(i):
#                 print (b, end="")
#                 b+=1
#             print()

#     def pattern11 (self):
#         a = self.num
#         for i in range(1,a+1):
#             for j in range(a-i):
#                 print (" ", end="")
#             for k in range((2*i)-1):
#                 print ("*", end="")
#             print()

#     def pattern12 (self):
#         a = self.num
#         for i in range(a,0,-1):
#             for j in range(a-i):
#                 print (" ", end="")
#             for k in range((2*i)-1):
#                 print ("*", end="")
#             print()
    
#     def pattern13 (self):
#         a = self.num
#         for i in range(1,a+1):
#             for j in range(a-i):
#                 print (" ", end="")
#             for k in range(1,i):
#                 print (k, end="")
#             for h in range(i,0,-1):
#                 print (h, end="")
#             print()
    
#     def pattern14 (self):
#         a = self.num
#         for i in range(1,a+1):
#             for j in range(a-i):
#                 print (" ", end="")
#             for k in range(i):
#                 print ("* ", end="")
#             print()

#     def pattern15 (self):
#         a = self.num
#         for i in range(1,a+1):
#             for j in range(i):
#                 print ("*", end="")
#             print()
#         for i in range(a-1,0,-1):
#             for j in range(i):
#                 print ("*", end="")
#             print()

#     def pattern16 (self):
#         a = self.num
#         for i in range(1,a+1):
#             for j in range(1,i+1):
#                 print (j, end="")
#             print()
#         for i in range(a,0,-1):
#             for j in range(1,i):
#                 print (j, end="")
#             print()
    
#     def pattern17 (self):
#         a = self.num
#         for i in range(a):
#             for j in range(a):
#                 if i==0 or i==4 or j==0 or j==4:
#                     print ("*", end="")
#                 else:
#                     print(" ", end="")
#             print()
    
#     def pattern18 (self):
#         a = self.num
#         for i in range(1,a+1):
#             for j in range(i):
#                 if (i+j)%2==1:
#                     print ("1", end="")
#                 else:
#                     print("0", end="")
#             print()

# joy = For_pattern(5)
# joy.pattern1()
# joy.pattern2()
# joy.pattern3()
# joy.pattern4()
# joy.pattern5()
# joy.pattern6()
# joy.pattern7()
# joy.pattern8()
# joy.pattern9()
# joy.pattern10()
# joy.pattern11()
# joy.pattern12()
# joy.pattern13()
# joy.pattern14()
# joy.pattern15()
# joy.pattern16()
# joy.pattern17()
# joy.pattern18()