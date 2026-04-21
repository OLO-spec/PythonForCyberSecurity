#!/usr/bin/env python3
# A more complex "Hello World" script in python with Inputs
# Created 4/20/26

#Ask user for their name
user_name = input("What is your name? ")

#Print hello and their name
print("Hello {0}".format(user_name))
print(f"Hello {user_name}")
print("Hello "+ user_name)
print("Hello", user_name)
message = "Hello {0}".format(user_name)
print(message)