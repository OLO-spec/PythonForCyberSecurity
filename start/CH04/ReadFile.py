#!/usr/bin/env python3
# Sample script that reads from a file
# By D - 4/28/2026
import os
#open file for writing
dir_path =os.path.dirname(os.path.realpath(__file__))
f=open(dir_path + "/newtextfile.txt", "r")
#read the file and print to screen
contents = f.read()

#closing the file
f.close()