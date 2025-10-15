#   Test case 1 : write a function to check if a number is even or odd
def checkNumber (num):
    if num % 2 == 0:
        return "The number is Even"
    else:
        return "The number is Odd"
print('Test Case 1')
print(checkNumber(4))
print(checkNumber(7))
print()

# Test case 2 : write a function to check if a number is positive, negative, or zero
def check_Number (num):
    if num > 0:
        return "The number is Positive"
    elif num < 0:
        return "The number is Negative"
    else:
        return "The number is Zero"
print('Test Case 2')
print(check_Number(10))
print(check_Number(-5))
print(check_Number(0))
print()
    
# Test case 3 : write a function to check for anagrams
def check_anagrams (str1, str2):
    if sorted(str1) == sorted(str2):
        return "True"
    else:
        return "False"
print('Test Case 3')
print(check_anagrams("listen", "silent"))
print(check_anagrams("hello", "world"))
print()

# Test Case 4 : write a function to calculate the factorial of a number
def factorial (num):
    if num < 0:
        return "Factorial is not defined for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
print('Test Case 4')
print(factorial(5))
print(factorial(0))
print()

# Test case 5 : write a function if a string is a palindrome
def check_palindrome (s):
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        return "True"
    else:
        return "False"
print('Test Case 5')
print(check_palindrome("racecar"))
print(check_palindrome("python"))
print()

# Test case 6 : write a function if a number is an Armstrong number
def check_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    if sum_of_powers == num:
        return "True"
    else:
        return "False"
print('Test Case 6')
print(check_armstrong(153))
print(check_armstrong(123))
print()

# Test case 7 : create a class to represent a Bank Account with deposit and withdrawal methods
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds"

# Test
print('Test Case 7')
account = BankAccount("Name")
print(account.deposit(1000))  
print(account.withdraw(500))  
print(account.withdraw(600)) 
print() 

# Text Case 8 : create a class to represent a Student with methods to add grades and calc ulate the average
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        return f"Grade {grade} added."

    def calculate_average(self):
        if self.grades:
            average = sum(self.grades) / len(self.grades)
            return f"Average grade: {average}"
        else:
            return "No grades available to calculate average"
        
# Test
print('Test Case 8')
student = Student("Name")
print(student.add_grade(85))
print(student.add_grade(90))
print(student.calculate_average())
print()
