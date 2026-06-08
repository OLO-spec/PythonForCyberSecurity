#!/usr/bin/env python3
# Script that checks passwords agains haveibeenpwned.com API
# https://haveibeenpwned.com/API/v3#PwnedPasswords
# By D on 6/2/2026

#import module

import requests
import hashlib
import requests
#function to check passwords
def check_have_been_pwned(sha_prefix):
    pwnd_dict = {}
    request_url = "https://api.pwnedpasswords.com/range/" + sha_prefix

    #perform API request
    response = requests.get(request_url)

    #confirm if request was successful
    if response.status_code == 200:
        lines = response.text.splitlines()
        for line in lines:
            suffix, count = line.split(":")
            pwnd_dict[suffix] = int(count)

    return pwnd_dict

#prompt user for password
new_password = input("What password needs to be checked? ")

#Hsh the pssword in SHA-1
encoded_password = new_password.encode()
digest_password = hashlib.sha1(encoded_password)
hashed_password = digest_password.hexdigest()
#split the password hash at 5:0

sha_prefix = hashed_password[0:5]
sha_postfix = hashed_password[5:]

print(f"Prefix sent: {sha_prefix}")
print(f"Postfix looked for: {sha_postfix}")
print(f"Full Hash: {hashed_password}\n")

pwnd_dict = check_have_been_pwned(sha_prefix)

#check result
if sha_prefix in pwnd_dict:
    print(
        "Password has been compromised {0} times ".format(pwnd_dict[sha_postfix])
    )
else:
    print("Password has not been found, it is safe to use! ")
