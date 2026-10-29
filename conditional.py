# if else
import os

name = input("What is your name?")
age = input("Enter the  age")

if not age.isnumeric():
    print("Invalid age")
    # terminate
    os._exit(0)

if int(age) > 18:
    print(name + " is an Adult")
else:
    print("Child")
