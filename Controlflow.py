# control flow

for s in range(6):
    print(s)

for i in range(2,20):
    print(i)

for e in range(1,6):
    print(e)

for t in range (3,10,3):
    print(t)

# sum of numbers between 1 to 10

total=0
for i in range (1,501):
    total +=i
print(total)

# square

for x in range (2,20):
    print(x**3)

# reverse

for i in range (10,0,-1):
    print(i)

# count=0

for i in range (1,101):
    if i % 7==0:
        count +=1
        if i == 35:
            break
print (count)

# question
num=int(input("enter the number:"))
for i in range (1,11):
     print(num,"x" , i , "=",num *i)

# employee salary

salaries=[10000,20500,65000,20000,85000]
for salary in salaries:
    print("monthly salary:",salary)

attendance=["present", "absent", "present", "present","absent"]
count=0
for status in attendance:
    if status == "present":
        count += 1
        if status == "absent":
            count +=1
        print("total absent:",count)

# sale report

sales = [1200, 1500, 1000, 1800, 1700, 1300]
total = 0
for amount in sales:
 total +=amount
 average = total / 7
print("total sales:",total)
print ("average sales:",average)

# bonus calculation
salaries = [25000, 30000, 28000, 35000, 40000]

for salary in salaries:
    bonus = salary * 0.10
    print("Salary:", salary, "Bonus:", bonus)
# Inventory Check
items = [
    ("Pen", 25),
    ("Notebook", 7),
    ("Pencil", 15),
    ("Eraser", 5),
    ("Marker", 9)
]

for item, quantity in items:
    if quantity < 10:
        print("Low Stock:", item, "-", quantity)
# Project Hours
hours = [8, 7, 9, 6, 8]

total_hours = 0

for h in hours:
    total_hours += h

print("Total Project Hours:", total_hours)

# email List
emails = [
    "rahul@gmail.com",
    "priya@gmail.com",
    "amit@gmail.com",
    "neha@gmail.com",
    "rohan@gmail.com"
]

for email in emails:
    print(email)

# Performance Rating
scores = [95, 82, 68, 91, 75]

for score in scores:
    if score >= 90:
        print("Excellent")
    elif score >= 70:
        print("Good")
    else:
        print("Needs Improvement")

# nested loop
for i in range (1,4):
    for j in range (1,3):
        print("outer loop:",i,"inner loop:",j)

for r in range (1,5):
    for c in range (1,6):
        print("*",end=" ")
    print()

for r in range (1,5):
    for c in range (r):
        print("*",end="")
    print()

# reverse
for r in range (5,0,-1):
    for c in range (r):
        print("*",end="")
    print ()

for r in range (1,6):
    for c in range (1,r+1):
        print(c,end="")
    print()

for r in range  (1,6):
    for c in range (1,6):
        print(r,end="")
    print()
 

for num in range (2,11):
    print ("multiplication of:",num)
for multiply in range (1,11):
        print (num,"*",multiply,"=",num * multiply)
    

# question

# rectangle pattern
for i in range (1,5):
    for j in range (1,7):
        print("*",end="")
    print() 
    
# increasing triangle


for r in range (1,8):
    for c in range (r):
        print("*",end="")
    print()

# number square

for i in range (4):
    for j in range (1,5):
        print(j, end="")
    print()    

# multiplication tables


for num in range(2, 11):
    print("Multiplication of:", num)

    for multiply in range(1, 11):
        print(num, "*", multiply, "=", num * multiply)

    print("-------------------------")

# classroom seating

for r in range (1,6):
    print("Row:",r)
    for seat in range (1,9):
        print("seat",r,"-",seat)
    for r in range (1,5):
     for seat in range (1,9):
        print(r,"=",seat)

# prim enumbers


for num in range(2, 51):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num)


# pattern challeges


for row in range(1, 6):
    for space in range(5 - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()