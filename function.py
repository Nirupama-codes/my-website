# Greeting Funtion
# def greeting(name):
#     print("Welcome", name)

# greeting("Nirupama")

# Addition funtion
# def addition(a, b):
#     return a + b

# result = addition(10, 20)
# print("Sum =", result)

# even or odd
# def even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# print(even_odd(8))
# print(even_odd(7))

# factorial calculator
# def factorial(n):
#     result = 1

#     for i in range(1, n + 1):
#         result = result * i

#     return result

# print("Factorial =", factorial(5))

# largest of three numbers
# def largest(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c

# print("Largest =", largest(10, 25, 15))

# grade calculator
# def grade(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 75:
#         return "B"
#     elif marks >= 60:
#         return "C"
#     elif marks >= 40:
#         return "D"
#     else:
#         return "Fail"

# marks = int(input("Enter your marks: "))
# print("Grade =", grade(marks))

# list statics
# def total(numbers):
#     return sum(numbers)

# def average(numbers):
#     return sum(numbers) / len(numbers)

# def minimum(numbers):
#     return min(numbers)

# def maximum(numbers):
#     return max(numbers)

# nums = [10, 20, 30, 40, 50]

# print("Total =", total(nums))
# print("Average =", average(nums))
# print("Minimum =", minimum(nums))
# print("Maximum =", maximum(nums))

# banking application
# balance = 1000

# def deposit(amount):
#     global balance
#     if amount > 0:
#         balance += amount
#         print("Amount deposited successfully")
#     else:
#         print("Enter a valid amount")

# def withdraw(amount):
#     global balance
#     if amount <= 0:
#         print("Enter a valid amount")
#     elif amount <= balance:
#         balance -= amount
#         print("Withdrawal successful")
#     else:
#         print("Insufficient balance")

# def show_balance():
#     print("Current Balance =", balance)

# while True:
#     print("\n1. Deposit")
#     print("2. Withdraw")
#     print("3. Check Balance")
#     print("4. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         amount = float(input("Enter deposit amount: "))
#         deposit(amount)

#     elif choice == "2":
#         amount = float(input("Enter withdrawal amount: "))
#         withdraw(amount)

#     elif choice == "3":
#         show_balance()

#     elif choice == "4":
#         print("Thank you!")
#         break

#     else:
#         print("Invalid choice")

# student record processor
# students = [
#     {"name": "Aman", "marks": [80, 70, 90]},
#     {"name": "Riya", "marks": [60, 65, 70]},
#     {"name": "Rahul", "marks": [30, 35, 40]},
#     {"name": "Neha", "marks": [85, 90, 95]}
# ]

# def calculate_average(marks):
#     return sum(marks) / len(marks)

# def passing_students(students):
#     for student in students:
#         avg = calculate_average(student["marks"])

#         print(student["name"], "Average =", avg)

#         if avg >= 40:
#             print("Status: Pass")
#         else:
#             print("Status: Fail")

# passing_students(students)






















































