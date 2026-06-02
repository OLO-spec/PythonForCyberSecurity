#!/usr/bin/env python3
# Dad Jokes
#By D, 6/1/2026

import requests

def get_dad_jokes():
    url="https://icanhazdadjoke.com/"

#Define headers so api is in json
headers = {"Accept": "application/json"}\

try:
    response = requests.get(url, headers=headers)

    #Check that its sucsecsful
    if response.status_code == 200:
        joke_data = response.json()

        #print joke from repository
        print(joke_data.get("joke"))

    else:
        print()"failed to get joke/ Status code: {response.status.code}"

    