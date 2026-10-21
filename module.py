# Python Modules built-in modules

# import math

# print("square root:",math.sqrt(100))
# print("square of :",math.pow(5,3))
# print("factorial:",math.factorial(5))

# import random

# number=random.randint(1,10)
# print(number)

# print(random.choice(["anjali","Nikita","Khushi","Shreya"]))

# import statistics

# marks=[50,60,60,70,80,85]
# print(statistics.mean(marks))
# print(statistics.median(marks))
# print(statistics.mode(marks))

# import os

# print(os.name) 
# print(os.getcwd())
# os.mkdir("module_ton

# USER DEFINED MODULES

# import modules1

# print(modules1.add(12,5))

# print(modules1.sub(12,5))

# print(modules1.div(12,5))

# print(modules1.mul(12,5))

# total=modules1.a + modules1.b
# print(total)

# question

# import calculator

# print(calculator.add(8,4))

# print(calculator.sub(8,4))

# print(calculator.div(8,4))

# print(calculator.mul(8,4))

# total=calculator.a + calculator.b
# print(total)


# import math

# print("square root:",math.sqrt(200))
# print("square of:",math.pow(4,3))
# print("factorial:",math.factorial(6))


# import random

# questions = ["what is python?","what is variable?","what is loop?","what is funtion?","what is module?"]
# print(random.choice(questions)) 


# pip is an standard package installer for python

# python file Handling

# file=open ("test.txt","mode")


# r- read > read an existing file
# w-write > create a file or overwrite an existing file
# a-append > add data to the End 
# x-exculsive creation > create a file only if it does not existing
# r+-read and write > opens an exiting file for both operation

# file=open("aipa.txt","w")
# file.write("hello Students of AIPA")
# file.close()

# with open("aipa2.txt","w")as file:
#           file.write("Hello Students of AIPA NSTI ALD")
# # append "a" - add a new line to an existing file

# with open("aipa2.txt","a") as file:
#     file.write("/nprayagraj")
#     file.write("/n india")

# import time

# with open("aipa.txt","r") as file:
    # for line in file:
    #     print(line.strip())
    #     time.sleep(2)

    # x=file.read()
    # print(x)

    # x=file.read(52)
    # print(x)

    # print(file.readline())
    # print(file.readline())
    # print(file.readline())

    # print(file.readline().strip())
    # print(file.readline().strip())
    # print(file.readline().strip())

    # lines=file.readlines()

    # print(lines)

# "x" - creates a new file if the file does not already exist 
# try:
#     with open("aipa2.txt","x")as file:
#         file.write("x mode")

# except:
#     print("File already exists")
   
# import csv 

# std=[
#     ["Shreya",27,"AIPA"],
#     ["Ajeet",27,"AIPA"],
#     ["Aditya",27,"AIPA"],
#     ["Khushi",27,"AIPA"],
#     ["Nirupama",27,"AIPA"]]

# with open("studnet.csv","w",newline="") as file:
#     writer=csv.writer(file)
#     writer.writerows(std)

# with open("student.csv","r") as file:
#     reader= csv.reader(file)
#     for row in reader:
#         print(row)    

# handling Directories & Files 

import os,shutil,pathlib

# print(os.getcwd())  current working directory

# os.mkdir("21 oct") create a directory

# os.rmdir("21 oct") remove a directory

# # print(os.listdir(".")) list files

# shutil.rmtree("21 oct")  remove everything in a directory

# os.rename("aipa.txt","copa.txt")  renmae a file

# shutil.copy("aipa2.txt","aipa3.txt")  copy a File 

# shutil.move("A.txt","b.txt") move a file


# from pathlib import path 

# filename=input("enter the filename:")

# path=Path(filename)

# if path.exists():
#     print("File exists")
# else:
#     print("File does not exists")


# Question
# 1. Directory information

# from pathlib import Path

# # Current working directory
# current_path = Path.cwd()
# print("Current Working Directory:", current_path)

# # List all files and folders
# print("\nFiles and Folders:")

# for item in current_path.iterdir():
#     print(item.name)
# import os,shutil,pathlib

# print(os.getcwd())

# 2.File Existence

# from pathlib import Path

# filename = input("Enter filename: ")

# file_path = Path(filename)

# if file_path.exists() and file_path.is_file():
#     print("File exists.")
# else:
#     print("File does not exist.")

# 3.Create Nested Folders

# from pathlib import Path

# folder = Path("College/Students/AIPA")

# folder.mkdir(parents=True, exist_ok=True)

# print("Folders created successfully!")

# 4. Find File Types

# from pathlib import Path

# folder = Path(input("Enter folder path: "))

# if folder.is_dir():
#     for file in folder.iterdir():
#         if file.is_file() and file.suffix.lower() in [".csv", ".txt"]:
#             print(file.name)
# else:
#     print("Folder does not exist.")

# 5. Backup a file

# from pathlib import Path
# import shutil

# source = Path("notes.txt")
# backup_folder = Path("backup")

# if source.is_file():
#     backup_folder.mkdir(parents=True, exist_ok=True)

#     shutil.copy2(source, backup_folder / source.name)

#     print("Backup created successfully!")
# else:
#     print("Source file not found.")

# 6. Move Files

# from pathlib import Path
# import shutil

# source_folder = Path("practice")
# pdf_folder = Path("PDF")

# if source_folder.is_dir():
#     pdf_folder.mkdir(parents=True, exist_ok=True)

#     for file in source_folder.glob("*.pdf"):
#         if file.is_file():
#             shutil.move(str(file), str(pdf_folder / file.name))
#             print("Moved:", file.name)
# else:
#     print("Practice folder does not exist.")

# 7. Directory Backup

# from pathlib import Path
# import shutil

# source = Path("test")
# destination = Path("test_backup")

# if source.is_dir():
#     if not destination.exists():
#         shutil.copytree(source, destination)
#         print("Directory backup created successfully!")
#     else:
#         print("Backup folder already exists.")
# else:
#     print("Test directory does not exist.")


















































































































































































