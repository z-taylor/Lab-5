# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab5A.py
numList = []
print("Please enter 10 numbers and this program will display the largest.")
for i in range(10):
    i+=1
    numList.append(int(input(f"Please enter number {i}: ")))
print(f"The largest number was {max(numList)}")