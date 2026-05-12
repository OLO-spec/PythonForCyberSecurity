#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By D 5/12/2026
#import modules
import crypt
import os
#function to test password
def test_password(algorithm_salt, hashed_password, password_guess):
    #use salt to hash the guess
    hashed_guess = crypt.crypt(password_guess, algorithm_salt)

    #compare against salted guess against hashed password
    if hashed_guess == hashed_password:
        return True
    return False

#load dictionary
dir_path =os.path.dirname(os.path.realpath(__file__))
f = open(dir_path + "/top1000.txt", "r") 
contents = f.readlines()
#promot user for algorithem/salt 


#prompt user for salted hash


#loop through each password