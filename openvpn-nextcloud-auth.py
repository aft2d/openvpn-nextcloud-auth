#!/usr/bin/python3

import requests
import os
import sys

base_url = "https://nextcloud.example.org"


def log(message):
    print("[" + sys.argv[0] + "] " + message)


log("NextCloud auth script received auth request")

if len(sys.argv) > 1 and len(sys.argv[1]) > 0:
    log("Detected call with 'via-file' option")
    log("Reading credentials from " + sys.argv[1])
    file = open(sys.argv[1], "r")
    data = file.read()
    username, password, *z = data.split("\n")

elif "username" in os.environ:
    log("Detected call with 'via-env' option")

    if "password" in os.environ:
        username = os.environ['username']
        password = os.environ['password']

    else:
        log("Unable to read password from environment variable")
        log("Hint: https://community.openvpn.net/openvpn/ticket/747")
        exit(1)

else:
    log("Unable detect if script was called with via-env or with via-file")
    exit(1)

log("Authenticating user '" + username + "'")

url = base_url + '/ocs/v1.php/cloud/users/' + username
log("Sending request to " + url)

session = requests.Session()
session.auth = (username, password)
response = session.get(url, headers={"OCS-APIRequest": "true"})
if response.status_code == 200:
    log("Authentication successful!")
    exit()

log("Authentication failed!")
log("Status code: " + str(response.status_code))
log("Response: \n" + response.text)
exit(1)
