# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab5B.py
size = int(input("Please enter a value for the size: "))
print(f"This is the requested {size}x{size} box:")
for i in range(size):
    for i in range(size):
        print("*", end="")
    print("")
print(f"This is the requested right-facing {size}x{size} right-triangle:")
for i in range(size):
    for i_ in range(i+1):
        print("*", end="")
    print("")
print(f"This is the requested left-facing {size}x{size} right-triangle:")
for i in range(size):
    for i_ in range(size-(i+1)):
        print(" ", end="")
    for i_ in range(i+1):
        print("*", end="")
    print("")