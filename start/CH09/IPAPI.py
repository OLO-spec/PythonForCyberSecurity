#made by D on 6/14/26

import json
import requests

#look up public IP

#function to look up IP
def check_ip_details(target_ip):
    request_url = "http://ip-api.com/json/" + target_ip
    results = requests.get(request_url)

    #return data as a dictionary
    return results.json()

#target IP to investigate
target_ip = "1.1.1.1"

#check Ip
ip_data = check_ip_details(target_ip)

#check details
if ip_data["status"] == "success":
    print("IP found, analysis completed, detailsd retrieved and are below. ")
    print("IP Adress: " + ip_data["query"])
    print("IP Adress: " + ip_data["city"] + ip_data["country"])
    print("Provider/ISP: " + ip_data["isp"])
else:
    print("Failed to retrive details for IP adress.")

