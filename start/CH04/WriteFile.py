#!/usr/bin/env python3
# Sample script that writes to a file
# By D - 4/28/2026
import os

#get the directory where the script is located
dir_path = os.path.dirname(os.path.realpath(__file__))

#ask for information
name = input("What is your name? ")
color = input("What is your favorite color? ")
pet = input("What was your first pet's name? ")
maiden_name = input("What is your mother's maiden name? ")
school = input("What elementary school did you attend? ")

#open file for writing
f = open(dir_path + "/hackme.txt", "w") 

# write the collected information to the file
f.write("Name: " + name + "\n")
f.write("Favorite Color: " + color + "\n")
f.write("First Pet: " + pet + "\n")
f.write("Mother's Maiden Name: " + maiden_name + "\n")
f.write("Elementary School: " + school + "\n")

#close the file
f.close()

print("\nInformation saved to hackme.txt in " + dir_path)