"""Nested for loop"""
# for i in range(0,3):
#         for j in range(0,3):
#             print(i,j)
#         print()
             
# for i in range(1,5):
#         for j in range(i):
#                 print(j,end=" ")
#         print()

# row=3
# for i in range(row):
#     for j in range(row):
#         print("*",end=" ")
#     print()

# w=4
# h=3
# for i in range(h):
#     for j in range(w):
#         print("*",end=" ")
#     print()
 

# n=5
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if row==1 or  row==n or col==1 or col==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
       
# row=4
# for i in range(row):
#     for j in range(row):
#         print(f"{i}",end=" ")
#     print()

# row=5
# for i in range(row):
#     for j in range(row):
#         print(f"{j}",end=" ") 
#     print()

# row=3
# count=1
# for i in range(row):
#     for j in range(row):
#         print(f"{count}",end=" ")
#         count+=1
#     print()

# row=3
# count=5
# for i in range(row):
#     for j in range(row):
#         print(f"{count}",end=" ")
#         count+=5
#     print() 

# row=4
# for i in range(row+1):
#     for j in range(i):
#         print(f"{i}",end=" ")
#     print() 

"""inverted right triangle"""
# for i in range(5,0,-1):
#     for j in range(i):
#         print(f"{j}",end=" ")
#     print() 

# row=5
# for i in range(row):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(i,row):
#         print(f"*",end=" ")
#     print()

# row=6
# for i in range(row,0,-1):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(i,row):
#         print("*",end=" ")
#     print()                           

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or  i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# row=6
# for i in range(row):
#     for j in range(row-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print() 

# n=5
# #upper part
# for i in range(n):
#     print(" " * ( n-i-1 )+ "*" * (2*i+1) )
# #lower part
# for i in range(n-2,-1,-1):
#     print(" " * (n-i-1) + "*" * (2*i+1))

# n=5
# # upper part
# for i in range(n,0,-1):
#     print("*" * i)
# # lower part
# for i in range(2,n+1):
#         print("*"*i) 




    


  









