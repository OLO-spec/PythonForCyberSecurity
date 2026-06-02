#!/usr/bin/env python3
# Script that checks passwords agains haveibeenpwned.com API
# https://haveibeenpwned.com/API/v3#PwnedPasswords
# By D on 6/2/2026

#import module

import requests
import hashlib
import requests
#function to check passwords
def chek_haveIbeenpwned(sha_prefix):
    pwd_dict = {}
    #Perform API request
    request_url = "https://api.pwnedpasswords.com/range/" + sha_prefix
    results = requests.get(request_url)
    #Confrim if found

#prompt user for password
new_password = input("What password needs to be checked? ")

#Hsh the pssword in SHA-1
encoded_password = new_password.encode()
digest_password = hashlib.sha1(encoded_password)
hashed_password = digest_password.hexdigest()
#split the password hash at 5:0

sha_prefix = hashed_password[0:5]
sha_postfix = hashed_password[5: ]
#Check password
print(sha_prefix)
print[sha_postfix]
print(hashed_password)

#check result

ikh