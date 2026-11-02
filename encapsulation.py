# oop object oriented programine principle

# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self . age = age
#         self.__salary = salary

#     def get_salary(self):
#         return self.__salary    

#     def inc_salary(self, amount):
#         if amount >0:
#             self.__salary += amount
#             print("salary updated")
#         else:    
#             print("Invalid amount")

# emp=Employee("Nirupama",20,50000)
# print("salary:",emp.get_salary())

# emp.inc_salary(5500)
# print("new balance:",emp.get_salary)
        
# Inheritance

# Single Inheritance

# class Animal():
#     def property(self):
#         print("Animal has 4 legs")

# class Dog(Animal):
#     def bark(Self):
#         print("Dog barks")

# d=Dog()  
# d.property()
# d.bark()

# multiple inheritance

# class Father():
#     def skill1(self):
#         print("Driving")

# class Mother():
#     def skill2(self):
#         print("Cooking")

# class Child(Father, Mother):
#     def Qualities(self):
#         print("Inherited skills from perents:") 

# x=Child()
# x.Qualities()
# x.skill1()
# x.skill2()


# multilevel inheirtance

# class Grandfather():
#     def house(self):
#         print("Grandfather's house")

# class Father(Grandfather):
#     def bike(self):
#         print("Father's bike")

# class Son(Father):
#     def laptop(self):
#         print("Son's Laptop")

# class Grandson(Father,Son):
#     def car(self):
#         print("Grandson's car")        
    
# g=Grandson()
# g.house()
# g.bike()
# g.laptop()

              
# Hirarchical inheritance

# class Institute():
#     def name(self):
#         print("NSTIW Allahabad")

# class Teacher (Institute):
#     pass
# class Student(Institute):
#     pass
# class Housekeeping(Institute):
#     pass

# t=Teacher()
# s=Student()
# h=Housekeeping()


# s.name()
# t.name()
# h.name()

# Question no.1
# Single Inheritance
# Student Management System

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# class student(Person):
#     def __init__(self, name, age, roll_no, course):
#         super().__init__(name, age)
#         self.roll_no = roll_no
#         self.course = course

#     def display_student(self):
#         self.display_details()
#         print("Roll No:", self.roll_no)
#         print("Course:", self.course)

# s1 = student("Nirupama",20, 101, "Python")

# s1.display_student()

# Question no.2
# Bank Account System

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposites:", amount)

# class SavingAccount(BankAccount):
#     def __init__(self, account_number, balance, interest_rate):
#         super().__init__(account_number,balance)
#         self.interest_rate = interest_rate
#     def calculate_interest(self):
#         interest = self.balance * self.interest_rate / 100
#         return interest

#     def display_details(self):
#         print("Account Number:",self.account_number)
#         print("Balance:", self.balance)
#         print("Interest Rate:", self.interest_rate, "%")
#         print("Interest Earned:", self.calculate_interest())

# a1 = SavingAccount(12345, 10000, 5)
# a1.deposit(2000)
# a1.display_details()

# Question no. 3
# Family Assets

# class Grandfather:
#     def house(self):
#         print("Grandfather has a house.")


# class Father(Grandfather):
#     def bike(self):
#         print("Father has a bike.")


# class Son(Father):
#     def laptop(self):
#         print("Son has a laptop.")


# s1 = Son()

# s1.house()
# s1.bike()
# s1.laptop()

# Question no.4
# Employee Hirarchy

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def get_name(self):
#         print("Name:", self.name)


# class Employee(Person):
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self.emp_salary = salary

#     def salary(self):
#         print("Salary:", self.emp_salary)


# class Manager(Employee):
#     def __init__(self, name, salary, team_size):
#         super().__init__(name, salary)
#         self.team_size_value = team_size

#     def display_team(self):
#         print("Team Size:", self.team_size_value)


# m1 = Manager("Rahul", 50000, 10)

# m1.get_name()
# m1.salary()
# m1.display_team()

# Question no.5
# College Management System

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# class Student(Person):
#     def __init__(self, name, age, marks):
#         super().__init__(name, age)
#         self.marks = marks

#     def display_student(self):
#         self.display_details()
#         print("Marks:", self.marks)


# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject

#     def display_teacher(self):
#         self.display_details()
#         print("Subject:", self.subject)


# s1 = Student("Aman", 18, 85)
# t1 = Teacher("Priya", 35, "Python")

# print("Student Details")
# s1.display_student()

# print("\nTeacher Details")
# t1.display_teacher()

# Question no.6
# Vehicle Management System

# class Vehicle:
#     def start(self):
#         print("Vehicle is starting.")


# class Car(Vehicle):
#     def air_condition(self):
#         print("Car has air conditioning.")


# class Bike(Vehicle):
#     def helmet_required(self):
#         print("Helmet is required for riding a bike.")


# class Bus(Vehicle):
#     def passenger_capacity(self):
#         print("Bus can carry 50 passengers.")


# c1 = Car()
# b1 = Bike()
# bus1 = Bus()

# print("Car:")
# c1.start()
# c1.air_condition()

# print("\nBike:")
# b1.start()
# b1.helmet_required()

# print("\nBus:")
# bus1.start()
# bus1.passenger_capacity()



