"""

============================================================
SECTION H - SCOPE (LOCAL / GLOBAL / LEGB)
============================================================

77. Create a global variable `company_name` and print it inside a function.

78. Create a local variable inside a function and try printing it outside.

79. Write a program to show difference between local and global variables.

80. Create a function where local variable and global variable have same name.
    Observe which one gets priority.

81. Use `global` keyword to modify a global variable inside a function.

82. Create nested functions and demonstrate enclosed scope.

83. Write a program to demonstrate LEGB rule clearly.

============================================================
SECTION I - NESTED FUNCTIONS + CLOSURES
============================================================

84. Write a nested function where inner function prints outer variable.

85. Create a function `outer_message()` and define `inner_message()` inside it.

86. Write a closure function `multiplier(n)` that returns another function.
    Example:
    double = multiplier(2)
    print(double(10))  # 20

87. Write a closure `discount_calculator(percent)`.

88. Write a closure `salary_increment(percentage)`.

89. Write a closure `message_sender(prefix)`.

90. Write a closure `power_of(n)`:
    square = power_of(2)
    cube = power_of(3)

============================================================
SECTION J - MULTIPLE RETURN VALUES
============================================================

91. Write a function that returns sum and product of two numbers.

92. Write a function that returns quotient and remainder.

93. Write a function that returns name, total marks, and grade.

94. Write a function that returns min and max from 3 numbers.

95. Write a function that returns area and perimeter of rectangle.

96. Write a function that returns monthly EMI and total payable amount.

============================================================
SECTION K - PASS BY OBJECT REFERENCE / MUTABLE / IMMUTABLE
============================================================

97. Pass an integer to a function and try changing it inside.
    Check whether original changes.

98. Pass a string to a function and try changing it inside.

99. Pass a list to a function and append values.
    Check whether original list changes.

100. Pass a dictionary to a function and update a key.

101. Write a function that receives a list and modifies it.

102. Write another function that receives a copy of the list and modifies it.

103. Compare the outputs of Question 101 and 102.

104. Write a function that accepts a dictionary of student marks and adds a new subject.

============================================================
SECTION L - RECURSION
============================================================

105. Write a recursive function to print numbers from 1 to n.

106. Write a recursive function to print numbers from n to 1.

107. Write a recursive function to find factorial.

108. Write a recursive function to find Fibonacci series up to n terms.

109. Write a recursive function to calculate sum of first n natural numbers.

110. Write a recursive function to calculate power(a, b).

111. Write a recursive function to reverse a string.

112. Write a recursive function to count digits in a number.

113. Write a recursive function to find sum of digits.

114. Write a recursive function to check palindrome string.

115. Write a recursive function to search an element in a list.

============================================================
SECTION M - LAMBDA FUNCTIONS
============================================================

116. Write a lambda function to square a number.

117. Write a lambda function to add two numbers.

118. Write a lambda function to find maximum of two numbers.

119. Write a lambda function to check even/odd.

120. Write a lambda function to get first character of a string.

121. Write a lambda function to calculate discount amount.

122. Write a lambda function to classify age:
    child / adult / senior

123. Write a lambda function to convert Celsius to Fahrenheit.

============================================================
SECTION N - HIGHER ORDER FUNCTIONS
============================================================

124. Write a function `apply_operation(func, value)` and pass different functions to it.

125. Create a function `calculator(operation, a, b)` where operation is another function.

126. Write a function that returns another function for tax calculation.

127. Write a function that returns another function for salary bonus calculation.

128. Write a function `process_data(func, data)`.

============================================================
SECTION O - map() PRACTICALS
============================================================

129. Use `map()` to convert a list of temperatures from Celsius to Fahrenheit.

130. Use `map()` to calculate squares of a list of numbers.

131. Use `map()` to calculate cube of numbers.

132. Use `map()` to convert names to uppercase.

133. Use `map()` to add 5% bonus to salaries.

134. Use `map()` to add GST to a list of product prices.

135. Use `map()` to calculate lengths of words in a list.

136. Use `map()` to format email usernames into full email IDs.

137. Use `map()` to convert a list of strings into integers.

============================================================
SECTION P - filter() PRACTICALS
============================================================

138. Use `filter()` to get only even numbers from a list.

139. Use `filter()` to get only odd numbers.

140. Use `filter()` to get numbers greater than 50.

141. Use `filter()` to get students who passed (mark >= 40).

142. Use `filter()` to get products above 1000 rupees.

143. Use `filter()` to get valid usernames with length >= 5.

144. Use `filter()` to get emails containing "@gmail.com".

145. Use `filter()` to get strings that start with a vowel.

146. Use `filter()` to get positive numbers only.

============================================================
SECTION Q - reduce() PRACTICALS
============================================================

147. Use `reduce()` to find sum of a list.

148. Use `reduce()` to find product of a list.

149. Use `reduce()` to find maximum value in a list.

150. Use `reduce()` to concatenate a list of words into a sentence.

151. Use `reduce()` to find total cart amount.

152. Use `reduce()` to count total characters from a list of strings.

153. Use `reduce()` to merge a list of dictionaries.

============================================================
SECTION R - DECORATORS
============================================================

154. Create a decorator that prints:
    "Function started" before execution.

155. Create a decorator that prints:
    "Function ended" after execution.

156. Create a decorator `timer_decorator` to show function execution message.

157. Create a decorator `login_required` to simulate login access.

158. Create a decorator `admin_only` to simulate admin access.

159. Create a decorator `uppercase_output` to convert returned text to uppercase.

160. Create a decorator `greet_decorator` to wrap greeting functions.

161. Create a decorator that logs function name before execution.

162. Create a decorator that checks if division by zero is attempted.

163. Create a decorator that validates if all arguments are positive numbers.

============================================================
SECTION S - DOCSTRINGS
============================================================

164. Write docstrings for a function `add(a, b)`.

165. Write docstrings for `calculate_salary()`.

166. Write docstrings for `validate_login()`.

167. Write docstrings for `discount_calculator()`.

168. Write docstrings for `student_grade()`.

169. Write docstrings for `loan_eligibility()`.

170. Access and print docstrings using `__doc__`.

171. Use `help()` on a user-defined function.

============================================================
SECTION T - MINI INDUSTRY-STYLE FUNCTION TASKS
============================================================

172. Build a function-based Student Result System:
    - calculate total
    - calculate average
    - find grade
    - print result summary

173. Build a function-based Employee Payroll System:
    - calculate basic salary
    - calculate bonus
    - calculate deductions
    - generate payslip

174. Build a function-based Ecommerce Cart System:
    - add item
    - calculate subtotal
    - apply discount
    - apply GST
    - generate invoice

175. Build a function-based ATM System:
    - deposit
    - withdraw
    - check balance
    - mini statement

176. Build a function-based Banking Interest Calculator:
    - simple interest
    - compound interest
    - loan EMI

177. Build a function-based Login + Signup Validator.

178. Build a function-based Attendance Report System.

179. Build a function-based Library Fine Calculator.

180. Build a function-based Electricity Bill Calculator.

181. Build a function-based Food Order Billing System.

182. Build a function-based Bus Ticket Booking Summary.

183. Build a function-based Resume Formatter.

184. Build a function-based Online Exam Result Checker.

185. Build a function-based Employee ID Generator.

============================================================
SECTION U - INTERVIEW-FOCUSED THINKING QUESTIONS
============================================================

186. What is the difference between parameter and argument?
    Demonstrate using code.

187. What is the difference between `print()` and `return()`?
    Explain with code.

188. Why are functions important in real projects?

189. What is the use of default arguments in production applications?

190. Where do we use `*args` and `**kwargs` in real software systems?

191. Why is recursion risky if base case is missing?

192. Why is lambda useful but not always preferred in large projects?

193. What are decorators and where are they used in Django / Flask / APIs?

194. Why are docstrings important in teams and real companies?

195. Explain Python scope with a practical example.

196. Explain closure with a practical real-world example.

197. What is higher-order function? Give one practical use case.

198. What is the difference between mutable and immutable objects during function calls?

199. Why is type hinting useful in modern Python development?

200. Write one complete answer:
    "How functions help build clean, reusable, and scalable code."

============================================================
BONUS CHALLENGE LABS (VERY IMPORTANT FOR INTERVIEWS)
============================================================

201. Build a menu-driven calculator using functions only.

202. Build a reusable validation module using multiple functions.

203. Build a small utility library:
    - prime checker
    - palindrome checker
    - factorial
    - string reverse
    - vowel counter

204. Build a reusable ecommerce helper file with:
    - tax calculator
    - discount calculator
    - stock checker
    - shipping fee calculator

205. Build a mini "user service" using functions:
    - create user
    - validate user
    - generate username
    - format profile

206. Build a mini "report generator" using functions.

207. Build a mini "student analytics system" using map(), filter(), reduce().

208. Build a mini "secure password checker" using functions and decorators.

209. Build a mini "attendance automation" using nested functions and closures.

210. Build a mini "invoice engine" using multiple return values and reusable functions.

============================================================
TRAINER NOTE
============================================================

Recommended Lab Flow for Students:
- Level 1: Questions 1 to 40
- Level 2: Questions 41 to 100
- Level 3: Questions 101 to 170
- Level 4: Questions 171 to 210

Best Practice for Students:
- Use proper function names
- Add docstrings
- Add type hints wherever possible
- Test each function with multiple inputs
- Focus on return-based logic
- Write reusable and readable code
- Avoid hardcoding values unless required

This question bank is designed for:
- Logic building
- Lab practice
- Viva preparation
- Technical interviews
- Industry coding habits
- Python backend foundation"""

