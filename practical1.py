# # a = 10
# # b = 10.5
# # c = "10"
# # d = True
# # print(type(a))
# # print(type(b))
# # print(type(c))
# # print(type(d))

# # create variable
# # studentname = "Nirupama"
# # studentage = 19
# # course = "AIPA"
# # percentage = 85.5
# # passed = True
# # print(studentname)
# # print(type(studentname))
# # print(studentage)
# # print(type(studentage))
# # print(percentage)
# # print(type(percentage))
# # print(passed)
# # print(type(passed))

# # employee data 
# # employee_id = 102
# # employee_name = "Ragini"
# # salary = 35000.50
# # department = "sales"
# # is_active = True
# # print(employee_id)
# # print(type(employee_id))
# # print(employee_name)
# # print(type(employee_name))
# # print(salary)
# # print(type(salary))
# # print(department)
# # print(type(department))
# # print(is_active)
# # print(type(is_active))

# # list
# # student_name = ["Priya","Naincy","Nehu","Varu","Vivek"]
# # print(student_name)
# # print(student_name[0])
# # print(student_name[4])
# # student_name.append("Nayra")
# # student_name.remove("Nehu")
# # print(student_name)

# # tupple

# # months = ("january","march ","may","july","sepetember")
# # print("months")
# # print(months[0])
# # print(months[4])
# # print(len(months))

# # dictionary

# # student={
# #     "name":"ajjet",
# #     "age":24,
# #     "course":"AIPA",
# #     "marks":80.5,
# #     "city":"MAU"
# # }
# # print(student["name"])
# # print(student["marks"])
# # student["marks"] = 90
# # student["gender"]="Male"
# # print(student)






# # python opretors
# # Arithmetic Operators

# # a=10
# # b=3
# # print(a+b)
# # print(a-b)
# # print(a*b)
# # print(a/b)
# # print(a%b)
# # print(a//b)
# # print(a**b)

# # assignment operator

# # x=50

# # x += 10
# # x -= 10
# # x *= 10
# # # x /= 10
# # x //= 10
# # x %= 10
# # print(x)

# # comparison operators

# # age=int(input("enter your age !"))
# # if age <=18:
# #     print("eligible for vote!")
# # else:
# #     print("not eligible for vote")

# # x=5
# # y=4

# # if x >= y:  
# # print("x is greater")
# # else:
# # print("invalid")

# # marks=100
# # print(marks <=40)
# # if marks  >=30:
# #     print("pass")
# # else:
# #     print("fail")
 
# # print(marks <=99)
# # if marks >=56:
# #     print("pass")
# # else:
# #     print("fail")


# # a=10
# # b=40

# # if a >= b:
# #     print("both are equal")
# # else:
# #     print("b is greater")

# # a = int(input("enter first no.:"))
# # b = int(input("enter second no.:"))

# # if a > b:
# #     print("first number is greater.")
# # elif b > a:
# #     print("second number is greter.")
# # else:
# #     print("both are equal.")

# # password="niru@1234"

# # enter=input("Enter your password:")
# # if password == enter:
# #     print("login successfully")
# # else:
# #     print("invalid password")


# # marks=int(input("enter your marks"))
# # if marks >= 90:
# #     print("excellent")
# # elif marks >= 75:
# #     print("very good")
# # elif marks >= 60:
# #     print("good")
# # elif marks >= 40:
# #     print("pass")
# # else:
# #     ("fail")            

# control flow

# for s in range(6):
#     print(s)

# for i in range(2,20):
#     print(i)

# for e in range(1,6):
#     print(e)

# for t in range (3,10,3):
#     print(t)

# sum of numbers between 1 to 10

# total=0
# for i in range (1,501):
#     total +=i
# print(total)

# square

# for x in range (2,20):
#     print(x**3)

# reverse

# for i in range (10,0,-1):
#     print(i)

# # count=0

# for i in range (1,101):
#     if i % 7==0:
#         count +=1
#         if i == 35:
#             break
# print (count)

# question
# num=int(input("enter the number:"))
# for i in range (1,11):
#      print(num,"x" , i , "=",num *i)

# employee salary

# salaries=[10000,20500,65000,20000,85000]
# for salary in salaries:
#     print("monthly salary:",salary)

# attendance=["present", "absent", "present", "present","absent"]
# count=0
# for status in attendance:
#     if status == "present":
#         count += 1
#         if status == "absent":
#             count +=1
#         print("total absent:",count)

# sale report

# sales = [1200, 1500, 1000, 1800, 1700, 1300]
# total = 0
# for amount in sales:
#  total +=amount
#  average = total / 7
# print("total sales:",total)
# print ("average sales:",average)

# bonus calculation
# salaries = [25000, 30000, 28000, 35000, 40000]

# for salary in salaries:
#     bonus = salary * 0.10
#     print("Salary:", salary, "Bonus:", bonus)
# Inventory Check
# items = [
#     ("Pen", 25),
#     ("Notebook", 7),
#     ("Pencil", 15),
#     ("Eraser", 5),
#     ("Marker", 9)
# ]

# for item, quantity in items:
#     if quantity < 10:
#         print("Low Stock:", item, "-", quantity)
# Project Hours
# hours = [8, 7, 9, 6, 8]

# total_hours = 0

# for h in hours:
#     total_hours += h

# print("Total Project Hours:", total_hours)

# email List
# emails = [
#     "rahul@gmail.com",
#     "priya@gmail.com",
#     "amit@gmail.com",
#     "neha@gmail.com",
#     "rohan@gmail.com"
# ]

# for email in emails:
#     print(email)

# Performance Rating
# scores = [95, 82, 68, 91, 75]

# for score in scores:
#     if score >= 90:
#         print("Excellent")
#     elif score >= 70:
#         print("Good")
#     else:
#         print("Needs Improvement")

# nested loop
# for i in range (1,4):
#     for j in range (1,3):
#         print("outer loop:",i,"inner loop:",j)

# for r in range (1,5):
#     for c in range (1,6):
#         print("*",end=" ")
#     print()

# for r in range (1,5):
#     for c in range (r):
#         print("*",end="")
#     print()

# reverse
# for r in range (5,0,-1):
#     for c in range (r):
#         print("*",end="")
#     print ()

# for r in range (1,6):
#     for c in range (1,r+1):
#         print(c,end="")
#     print()

# for r in range  (1,6):
#     for c in range (1,6):
#         print(r,end="")
#     print()
 

# for num in range (2,11):
#     print ("multiplication of:",num)
# for multiply in range (1,11):
#         print (num,"*",multiply,"=",num * multiply)
    

# question

# rectangle pattern
# for i in range (1,5):
#     for j in range (1,7):
#         print("*",end="")
#     print() 
    
# increasing triangle


# for r in range (1,8):
#     for c in range (r):
#         print("*",end="")
#     print()

# number square

# for i in range (4):
#     for j in range (1,5):
#         print(j, end="")
#     print()    

# multiplication tables


# for num in range(2, 11):
#     print("Multiplication of:", num)

#     for multiply in range(1, 11):
#         print(num, "*", multiply, "=", num * multiply)

#     print("-------------------------")

# classroom seating

# for r in range (1,6):
#     print("Row:",r)
#     for seat in range (1,9):
#         print("seat",r,"-",seat)
#     for r in range (1,5):
#      for seat in range (1,9):
#         print(r,"=",seat)

# prim enumbers


# for num in range(2, 51):
#     count = 0

#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1

#     if count == 2:
#         print(num)


# pattern challeges


# for row in range(1, 6):
#     for space in range(5 - row):
#         print(" ", end="")

#     for star in range(2 * row - 1):
#         print("*", end="")

#     print()

# # WHILE LOOP

# # i=1
# # while i <= 10:
# #     print(i)
# #     i +=1
    
# # even number b/t 1 to 20 
# i=2

# # while i <= 20:
# #     if i == 12:
# #        i += 2
# #        continue
# #     print(i)
# #     i += 2
    
#     # calculator program

# # print("my calculator !")
# # print("type 'exit' to quit")
# # while True:
# #     op=input("enter opretion (+,-,*,/ or exit):")
# #     if op == "exit":
# #        print("Calculator closed!")
# #     break
# # num1=float(input("enter first number:"))
# # num2=float(input("entr second number:"))

# # if op == "+":
# #     print(num1,"+",num2,"=",num1+num2)
# # elif op == "-":
# #     print(num1,"-",num2,"=",num1-num2)
# # else:
# #     print("invalid opreation")

# # for i in range(1,11):
# #     if i == 7:
# #         continue
# #     print(i)

# # function in pyhton

# # a function is a reusable block of code that performs a specific task.
# # it runs when it is called.

# # 10, 15, 20, 25, 30, 40 


# # def multiply(x):
# #     for i in range (1,11):
# #         print(x, "x",i, "=", x*i)

# # multiply(11)

# # def add():
# #     a=10
# #     b=20
# #     print(a+b)
# # add()

# # def add(a,b):
# #     return a+b
# # def sub(a,b):
# #     return a-b
# # def multiply(a,b):
# #     return a*b
# # def div(a,b):
# #     if b ==0:
# #         return "cannot divide by zero"
# #     return a/b

# # print(multiply(12,10))
# # print(sub(100,50))

# # print(div(100,5))
# # marks=[22,55,35,41]
# # len(makrs)

# # def cal_total(marks):
# #     return sum(marks)
# # def cal_avg(marks):
# #     return sum(marks)/len(marks)
# # def result(average):
# #     if average >=40:
# #         print("pass")
# #     else:
# #         print("fail")
# # std_name = input("enter student name: ")

# # marks=[]

# # for i in range (1,6):
# #     mark = int(input("enter marks for subject " + str(i)+": "))
# #     marks.append(mark)

# # total=cal_total(marks)
# # average=cal_avg(marks)
# # result=result(average)

# # print("Student name:",std_name)
# # print("Total:",total)
# # print("Average:",average)
# # print("Result:,result")

















































































































































































