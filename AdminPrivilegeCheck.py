import os, sys
import random
import numpy
from twilio.rest import Client
from configparser import ConfigParser



def checkNum(PhNum):
    configTwilio = ConfigParser()
    configTwilio.read('config.cfg')
    account = configTwilio.get('auth', 'account')
    token = configTwilio.get('auth', 'token')
    servicesid = configTwilio.get('auth', 'servicesid')
    logoncode = configTwilio.get('key', 'passcode')
    list = readToList()

   


    client = Client(account, token)

    phone_numbers = client.messaging \
                      .services(sid=servicesid) \
                      .phone_numbers \
                      .list()
    print(phone_numbers[0].phone_number)
    
    

    #serverPhone = phone_numbers[0].phone_number
    strOfNumbers = ''.join(str(n) for n in list)
    print(strOfNumbers)
    if PhNum in list:
        message = client.messages.create(
        to=strOfNumbers, 
        from_=phone_numbers[0].phone_number,
        body="What is your passkey?")

        print(message.sid)

        
    else:
        message = client.messages.create(
        to=strOfNumbers, 
        from_=phone_numbers[0].phone_number,
        body="You cannot access this.")
        print(message.sid)
    



def addtoFile(num):
    file = open("savedNumbers.txt","a") 
    file.write(num)
    file.close()


def readToList():
    file = open("AdminList.txt", "r")
    list = file.read().splitlines()
    file.close()
    return list

