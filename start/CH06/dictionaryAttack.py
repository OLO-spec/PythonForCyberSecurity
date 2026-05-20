#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By D 5/12/2026
#import modules

import os
import crypt

#function to test password
def test_password(algorithm_salt, hashed_password, password_guess):
    #use salt to hash the guess
    hashed_guess = crypt.crypt(password_guess, algorithm_salt)

    #compare against salted guess against hashed password
    if hashed_guess == hashed_password:
        return True
    return False

#define our list of dictionaries from smallest to largest
dictionary_files = ["top100.txt", "top1000.txt"]

#prompt user for algorithem/salt 
algorithm_salt = input("What is the algorithm and salt? ")
#prompt user for salted hash
hashed_password = input("what is the full hashed password? ")

#go through each dictionary file one by one
for file_name in dictionary_files:
    print("Searching inside: {0}...".format(file_name))
    
    #load current dictionary
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    #check if the file exists before trying to open it
    if os.path.exists(dir_path + "/" + file_name):
        f = open(dir_path + "/" + file_name, "r") 
        passwords = f.readlines()
        f.close()
        
        # loop through each password in the current file
        match_found = False
        for password in passwords:
            password = password.strip()
            result = test_password(algorithm_salt, hashed_password, password)
            if result: 
                print("Match found: {0}".format(password))
                match_found = True
                break
                
        #if a match was found in the smaller list stop searching entirely
        if match_found:
            break
    else:
        print("File {0} not found, skipping.".format(file_name))