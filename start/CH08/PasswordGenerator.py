#By D on 6/7/26

import hashlib
import random
import string
import requests


#function to check passwords
def check_haveIbeenpwned(sha_prefix):
    request_url = "https://api.pwnedpasswords.com/range/" + sha_prefix
    results = requests.get(request_url)

    #return the leaked postfixes as a list for an exact match check
    return [line.split(":")[0] for line in results.text.splitlines()]


#generate password using letters, digits, and punctuation
characters = string.ascii_letters + string.digits + "!@#$%^&*"

while True:
    new_password = "".join(random.choice(characters) for i in range(16))

    #hash the password in SHA-1
    encoded_password = new_password.encode()
    digest_password = hashlib.sha1(encoded_password)
    hashed_password = digest_password.hexdigest().upper()

    #pslit the password hash at 5:0
    sha_prefix = hashed_password[0:5]
    sha_postfix = hashed_password[5:]

    #check password
    leaked_postfixes = check_haveIbeenpwned(sha_prefix)

    #check result
    if sha_postfix not in leaked_postfixes:
        print("Password has not been found, and it is safe to use! ")
        print("Your secure password is: " + new_password)
        break 