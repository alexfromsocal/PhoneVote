#from flask import Flask, request, redirect
#from twilio.twiml.messaging_response import MessagingResponse as MR
from twilio.rest import Client
from flask import url_for, session, Flask, request
from configparser import ConfigParser
from twilio.twiml.messaging_response import MessagingResponse
from AdminPrivilegeCheck import checkNum
import os, sys
import random
import numpy
from twilio.rest import Client
from configparser import ConfigParser
#import importlib




app = Flask(__name__)


@app.route('/sms_inbound')


#Receives the incoming SMS to process further for our client.
def incoming_sms():
    configTwilio = ConfigParser()
    configTwilio.read('config.cfg')
    account = configTwilio.get('auth', 'account')
    token = configTwilio.get('auth', 'token')
    servicesid = configTwilio.get('auth', 'servicesid')
    logoncode = configTwilio.get('key', 'passcode')
    client = Client(account, token)


    phone_numbers = client.messaging \
                      .services(sid=servicesid) \
                      .phone_numbers \
                      .list()

    body = request.values.get('Body', None)
    response =MessagingResponse()
    
   
    if str(body).lower() == "logon":
        isAdmin = checkAdmin(request.values.get('From'), client, phone_numbers)
        print("logged")

    else:
        response.message("Your features aren't valid yet")
        
    #Gets the message from sender and grabs the body of it.
    
                             #Taken from Twilio helper library
    return str(response)

def redirect_to_first_question(response, survey):
    first_question = survey.questions.order_by('id').first()
    first_question_url = url_for('question', question_id=first_question.id)
    response.redirect(url=first_question_url, method='GET')


def welcome_user(survey, send_function):
    welcome_text = 'Welcome to the %s' % survey.title
    send_function(welcome_text)


def survey_error(survey, send_function):
    if not survey:
        send_function('Sorry, but there are no surveys to be answered.')
        return True
    elif not survey.has_questions:
        send_function('Sorry, there are no questions for this survey.')
        return True
    return False


def checkAdmin(PhNum, client, phone_numbers):
  
    list = readToList()
   

    #serverPhone = phone_numbers[0].phone_number
    strOfNumbers = ''.join(str(n) for n in list)
    print(strOfNumbers)
    if PhNum in list:
        message = client.messages.create(
        to=PhNum, 
        from_=phone_numbers[0].phone_number,
        body="What is your passkey?")

        print(message.sid)
        return True

        
    else:
        message = client.messages.create(
        to=PhNum, 
        from_=phone_numbers[0].phone_number,
        body="You cannot access this.")
        print(message.sid)
        return False

def readToList():
    file = open("AdminList.txt", "r")
    list = file.read().splitlines()
    file.close()
    return list



@app.route("/sms_outbound", methods=['GET', 'POST']) 
def outgoing_sms():
    body = request.values.get('Body', None)
    resp = MessagingResponse()                               #Taken from Twilio helper library
    resp.message("This is the ship that made the Kessel Run in fourteen parsecs?")
    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)