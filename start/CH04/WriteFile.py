#!/usr/bin/env python3
# Sample script that writes to a file
# By D - 4/28/2026
import os
#open file for writing
dir_path =os.path.dirname(os.path.realpath(__file__))
f=open(dir_path + "/newtextfile.txt", "w")

#write to file
print ("hello world")
f.write("Hello World, have a good day\n")
f.write("Have a good day")

#closing the file
f.close()