from django.shortcuts import render
from django.http import JsonResponse
import secrets
import hashlib
import requests
import logging
import os
import json


#create log file
logformat='%(asctime)s [%(levelname)s] %(message)s'
logging.basicConfig(filename='var/log/emarket.log', level=logging.DEBUG,FORMAT=logformat)

#salt generator
def generatesalt():
     secret=secrets.token_hex(16)
     return secret

#hash generator
def generatehash(salt,password):
    saltedpass= password + salt
    hashedpass=hashlib.sha256(saltedpass.encode()).hexdigest()
    return hashedpass

#STK push api
def apicall(number,amount):
  try: 
      url="https://tinypesa.com/api/v1/express/initialize"
      details={
          "amount": amount,
          "msisdn": number
      }
      payload =json.dumps(details)
      apikey=os.environ.get("apikey")
      header={
          "Content-Type":"application/json",
          "Apikey": apikey
      }
      response=requests.post(url,data=payload,headers=header)
      if response.status_code ==200:
          print("STK push sucess")
      else:
          print(response.json())
  except Exception as e:
      logging.error(f'An error occurred: {e}')



def login():
    try:
        email=requests.get('username')
        password=requests.get('password')
        #get credentials from database and compare them
        if password:
          data={"Data":"Login success"}
          response=JsonResponse(data)
          return response
        else:
           data={"Data":"Login failed"}
           response=JsonResponse(data)
           return response           
    except Exception as e:
         logging.error(f"An Error occured {e}", exc_info=True)
def signup():
    try:
        email=requests.get('username')
        password=requests.get('password')
        #store credentials in database
        data={"Data":"sign up success"}
        response=JsonResponse(data)
        return response
    except Exception as e:
         logging.error(f"An Error occured {e}", exc_info=True)   
#def homepage():

