# This python code ask a user his name and the year that he born then print My name is (user name) and I'm (age) years old.

name = input("Enter your name: ")
birth_year = int(input("Which year did you born? "))
age = 2024 - birth_year

print("My name is " + name + " and I'm " + str(age) + " years old.")
