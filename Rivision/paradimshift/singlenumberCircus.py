""" 4. Write a program to input a 3-digit number and calculate the sum of its digits.
        Write a program to input a 3-digit number and reverse the number.
        Write a program to input a number and calculate the sum of first and last digit.
        Write a program to check if a number entered by the user is even or odd.
        Write an if-statement to check if a number is positive, negative, or zero.
        Accept a number and check if it is a multiple of both 3 and 5.
        Check if a given number lies within the range 10 to 50 (inclusive).
        Check if a number is a three-digit number.
        Check if a number is divisible by 7 but not a multiple of 5.
"""
# class Num_games:
#     """different operation using single intiger number"""
#     def __init__(self,num):
#         self.num = int(num)
#         self.sum_num = 0
#         self.rever_num = 0
#         self.sum_fl = 0
#         print("The number is :",self.num)

#     def sum_digit(self):
#         """Calculate the sum of its digits."""
#         lcl_num= abs(self.num)
#         while lcl_num != 0:
#             self.sum_num  = int(lcl_num%10) + self.sum_num 
#             lcl_num = lcl_num//10
#         print("The sum of digit is :",int(self.sum_num ))

#     def reverse_digit(self):
#         """ reverse the number"""
#         lcl_num= abs(self.num)
#         while lcl_num !=0:
#             self.rever_num = int(lcl_num%10) + self.rever_num *10
#             lcl_num = lcl_num//10
#         print("The reverse of digit is :",int(self.rever_num))
    
#     def first_last(self):
#         """ calculate the sum of first and last digit"""
#         lcl_num = abs(self.num)
#         first_num = 0
#         last_num = lcl_num%10
#         while lcl_num !=0:
#             self.rever_num = lcl_num%10 + self.rever_num *10
#             first_num = lcl_num%10
#             lcl_num = lcl_num//10
#         self.sum_fl = first_num + last_num
#         print("The sum of first and last digit is :",int(self.sum_fl))

#     def even_odd (self):
#         """ even or odd"""
#         lcl_num = abs(self.num)
#         if lcl_num %2==0:
#             print("Even Number")
#             return True
#         else:
#             print("Odd number")
#             return False
        
#     def posi_neg(self):
#         """ a number is positive, negative, or zero."""
#         lcl_num = self.num
#         if lcl_num >0:
#             print("Positive Number")
#         elif lcl_num <0:
#             print("Negative Number")
#         else:
#             print("The number is Zero")
    
#     def three_five(self):
#         """ multiple of both 3 and 5"""
#         lcl_num = self.num
#         if lcl_num % 15 == 0:
#             print("The number is multiple of both 3 and 5")
#         else:
#             print("Not a multiple of both 3 and 5")
    
#     def num_range(self):
#         """ number lies within the range from 10 to 50 """
#         lcl_num = self.num
#         if 10 <lcl_num <50:
#             print("The number is within the range 10 to 50")
#         else:
#             print("Not within the range 10 to 50")

#     def three_digit(self):
#         """ number is a three-digit number"""
#         lcl_num = self.num
#         if 100 <= lcl_num <= 999:
#             print("The number is a three-digit number")
#         else:
#             print("Not a three-digit number")
    
#     def notseven_butfive(self):
#         """ divisible by 7 but not a multiple of 5"""
#         lcl_num = self.num
#         if lcl_num %5 !=0 and lcl_num%7 == 0:
#             print("The number is divisible by 7 but not a multiple of 5")
#         else:
#             print("Not a a valied number")


        
# test1 = Num_games(49)

# test1.sum_digit()
# test1.reverse_digit()
# test1.first_last()
# test1.even_odd()
# test1.posi_neg()
# test1.three_five()
# test1.num_range()
# test1.three_digit()
# test1.notseven_butfive()