""" Q. Write a program to input a 3-digit number and calculate the sum of its digits.
        Write a program to input a 3-digit number and reverse the number.
        Write a program to input a number and calculate the sum of first and last digit.
        Write a program to check if a number entered by the user is even or odd.
        Write an if-statement to check if a number is positive, negative, or zero.
        Accept a number and check if it is a multiple of both 3 and 5.
        Check if a given number lies within the range 10 to 50 (inclusive).
        Check if a number is a three-digit number.
        Check if a number is divisible by 7 but not a multiple of 5.
        FizzBuzz (Interview Classic): Print "Fizz" if div by 3, "Buzz" if div by 5, "FizzBuzz" if both.
        Write a program to print numbers from 1 to 20 using range().
        Write a program to print even numbers from 1 to 50.
        Write a program to print odd numbers from 1 to 50.
        Write a program to print numbers from 10 to 1 in reverse order.
        Write a program to print the multiplication table of a given number.
        Write a program to find the sum of numbers from 1 to N.
        Write a program to find the factorial of a number.
        Write a program to print the square of numbers from 1 to 10.
        Write a program to print the cube of numbers from 1 to 10.
        Write a program to find the sum of even numbers from 1 to 100.
        Write a program to find the sum of odd numbers from 1 to 100.
        Write a program to print the following pattern: 1 12 123 1234 12345
        Write a program to check whether a number is prime or not.
        Write a program to print Fibonacci series up to N terms.
"""
# class Num_games:
#     """different operation using single intiger number"""
#     def __init__(self,num):
#         self.num = int(num)
#         print("The number is :",self.num)

#     def sum_digit(self):
#         """Calculate the sum of its digits."""
#         lcl_num= abs(self.num)
#         total = 0
#         while lcl_num != 0:
#             total  += lcl_num%10
#             lcl_num = lcl_num//10
#         print("The sum of digit is :",int(total ))

#     def reverse_digit(self):
#         """ reverse the number"""
#         lcl_num= abs(self.num)
#         reverse =0
#         while lcl_num !=0:
#             reverse = (lcl_num%10) + (reverse *10)
#             lcl_num //= 10
        
#         if self.num <0:
#             reverse = -reverse

#         print("The reverse of digit is :", reverse)
    
#     def first_last(self):
#         """ calculate the sum of first and last digit"""
#         lcl_num = abs(self.num)
#         last_num = lcl_num%10

#         while lcl_num >= 10:
#             lcl_num = lcl_num//10
        
#         first_num = lcl_num
#         total = first_num + last_num
#         print("The sum of first and last digit is :",total)

#     def even_odd (self):
#         """ even or odd"""
#         lcl_num = abs(self.num)
#         output = "Even Number" if lcl_num %2==0 else "Odd number"
#         print(output)
                
#     def posi_neg(self):
#         """ a number is positive, negative, or zero."""
#         lcl_num = self.num
#         output = "Positive Number" if lcl_num >0 else "Negative Number" if lcl_num <0 else "The number is Zero"
#         print(output)
    
#     def three_five(self):
#         """ multiple of both 3 and 5"""
#         lcl_num = self.num
#         output = "The number is multiple of both 3 and 5" if lcl_num % 15 == 0 else "Not a multiple of both 3 and 5"
#         print(output)
            
#     def num_range(self):
#         """ number lies within the range from 10 to 50 """
#         lcl_num = self.num
#         output = "The number is within the range 10 to 50" if 10 <=lcl_num <=50 else "Not within the range 10 to 50"
#         print(output)

#     def three_digit(self):
#         """ number is a three-digit number"""
#         lcl_num = self.num
#         output = "The number is a three-digit number" if 100 <= lcl_num <= 999 else "Not a three-digit number"
#         print(output)

#     def seven_notfive(self):
#         """ divisible by 7 but not a multiple of 5"""
#         lcl_num = self.num
#         output = "The number is divisible by 7 but not a multiple of 5" if lcl_num %5 !=0 and lcl_num%7 == 0 else "Not a a valid number"
#         print(output)

#     def fizzbuzz (self):
#         """ "Fizz" if div by 3, "Buzz" if div by 5, "FizzBuzz" if both"""
#         lcl_num = self.num
#         output = "FizzBuzz" if lcl_num% 15 == 0 else "Fizz" if lcl_num%3 ==0 else "Buzz" if lcl_num%5 ==0 else "Not a valid number"
#         print(output)
            
#     def print_num(self):
#         """from 1 to 20 using range()"""
#         a= self.num
#         print("Print Numbers")
#         for i in range(1,a+1):
#             print(i, end=" ")
#         print()
    
#     def print_even(self):
#         """ print even numbers"""
#         a= self.num
#         print("Print Even Numbers")
#         for i in range(1,a+1):
#             out = i if i%2 ==0 else " "
#             print(out, end="")
#         print()

#     def print_odd(self):
#         """ print odd numbers"""
#         a= self.num
#         print("Print Odd Numbers")
#         for i in range(1,a+1):
#             out = i if i%2 !=0 else " "
#             print(out, end="")
#         print()
    
#     def print_reverse(self):
#         """ print reverse order"""
#         a= self.num
#         print("print reverse order")
#         for i in range(a, 0,-1):
#             print(i, end=" ")
#         print()
    
#     def print_mult(self):
#         """ multiplication table of a given number."""
#         a = self.num
#         print(f"multiplication table of {a}")
#         for i in range(1,13):
#             print(f"{i} X {a} = {i*a}")
#         print()

#     def print_sum(self):
#         """sum of numbers from 1 to N"""
#         a = self.num
#         total = a*(a+1)//2
#         print(f"sum of numbers from 1 to {a} : {total}")

#     def print_factorial(self):
#         """Calculate the factorial of a number."""
#         a = self.num

#         if a < 0:
#             print("Factorial is not defined for negative numbers")
#             return
        
#         factorial =1
#         for i in range(2, a+1):
#             factorial *= i
#         print(f"Factorial of {a} is :{factorial}")
    
#     def print_square(self):
#         """print the square of numbers"""
#         a = self.num
#         print("The squares of numbers")
#         for i in range(1,a+1):
#             n_sum = i**2
#             print(n_sum, end=" ")
#         print()
    
#     def print_cube(self):
#         """ cube of numbers"""
#         a = self.num
#         print("The Cubes of numbers")
#         for i in range(1,a+1):
#             n_sum = i**3
#             print(n_sum, end=" ")
#         print()
    
#     def sum_even(self):
#         """the sum of even numbers"""
#         a= self.num
#         n_sum =0
#         print(f"The sum of even numbers upto {a}")
#         for i in range(1,a+1):
#             out = i if i%2 ==0 else 0
#             n_sum+=out
#         print(n_sum)
    
#     def sum_odd(self):
#         """ sum of odd numbers"""
#         a= self.num
#         n_sum =0
#         print(f"The sum of odd numbers upto {a}")
#         for i in range(1,a+1):
#             out = i if i%2 !=0 else 0
#             n_sum+=out
#         print(n_sum)
    
#     def sum_series(self):
#         """ pattern: 1 12 123 1234"""
#         a= self.num
#         n_sum =0
#         print(f"pattern creation upto {a} digits")
#         for i in range(1,a+1):
#             n_sum = i + n_sum*10
#             print(n_sum, end=" ")

#     def prime_check (self):
#         """Check whether a number is prime or not."""
#         a= self.num
        
#         if a <= 1:
#             print("The number must be greater than 1")
#             return
        
#         is_prime = True

#         for i in range(2,int(a**0.5)+1):
#             if a % i == 0:
#                 is_prime= False
#                 break
#         print(f"{a} Prime Number" if is_prime else f"{a} Not a prime number")
    
#     def fibonacci(self):
#         """ Fibonacci series up to N terms"""
#         a= self.num
#         print(f"Fibonacci series up to {a}")
#         if a <= 0:
#             print("The number must be greater than 0")
#             return
#         first= 0
#         second = 1
#         for i in range(a):
#             print(first, end=" ")
#             first, second = second, first + second
#         print()
        

       


        
# test1 = Num_games(-22)
# test1.sum_digit()
# test1.reverse_digit()
# test1.first_last()
# test1.even_odd()
# test1.posi_neg()
# test1.three_five()
# test1.num_range()
# test1.three_digit()
# test1.notseven_butfive()
# test1.fizzbus()
# xb1=Num_games(12)
# xb1.print_num()
# xb1.print_even()
# xb1.print_odd()
# xb1.print_reverse()
# xb1.print_mult()
# xb1.print_sum()
# xb1.print_factorial()
# xb1.print_square()
# xb1.print_cube()
# xb1.sum_even()
# xb1.sum_odd()
# xb1.sum_series()
# xb1.prime_check()
# xb1.fibonacci()