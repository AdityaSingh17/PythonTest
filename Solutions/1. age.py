"""
To get the user input of name and age, and print the year in which the user will turn 100 years old.
"""

x = str(input("Hello, please enter your name : "))
age = int(input("Please enter your age : "))
year = int(input("What year is it now? "))

print(x+" You will turn 100 years in the year "+str(year-age+100))