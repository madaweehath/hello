'''This program asks you to enter your first and last name and your grade in three courses: Math, English,
 Computer Science. then compute your grade avrage and display your name and your grade average'''
#Define the variables
FirsN = input("Enter your first name:")
LastN = input("Enter your last name:")
MathG = int(input("Enter you Math grade:"))
EnglishG = int(input("Enter your English grade:"))
ComputerG = int(input("Enter your Computer Science grade:"))
print("First name:", FirsN)
print("Last name:", LastN)
average= (MathG+EnglishG+ComputerG)/3
print("your average grade is",average)
