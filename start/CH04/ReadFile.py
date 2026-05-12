#!/usr/bin/env python3
# Sample script that reads from a file
# By D - 4/28/2026
import os
#open file for writing
dir_path =os.path.dirname(os.path.realpath(__file__))

f=open(dir_path + "/hackme.txt", "r")

#print heading message
print("Here is someone to hack - information")
print("------------------")

#read the file and print to screen

contents = f.read()
print(contents)

#closing the file
f.close()