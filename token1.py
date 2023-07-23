import requests
import json
from getpass import getpass
from pprint import pprint
from requests.auth import HTTPBasicAuth

username = input("please provide your username: ")
password = getpass("please enter your password: ")

url = "https://sandboxdnac.cisco.com"
authAPI = "/dna/system/api/v1/auth/token"
deviceListAPI = "/dna/intent/api/v1/network-device"

authPayload = {}
authHeaders = {
  'Accept': 'application/json',
  'content-type': 'application/json',
  'Authorization' : 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

dnaAuth = url + authAPI

response = requests.post(dnaAuth, auth=HTTPBasicAuth(username, password), headers=authHeaders, data=authPayload, verify=False)

tokenJSON = response.json()

TOKEN = tokenJSON['Token']

print('Your tonken was successfully generate. The value of your tokenis:\n' + TOKEN)

dnaDeviceList = url + deviceListAPI
getPayload={}
getHeaders = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-Auth-Token': TOKEN 
}  
 
getResponse = requests.get(dnaDeviceList, headers=getHeaders, data=getPayload, verify=False)

getJSON = getResponse.json()
 
pprint(getJSON)

