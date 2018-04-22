#from flask import Flask, request, redirect
#from twilio.twiml.messaging_response import MessagingResponse as MR
from twilio.rest import Client
from configparser import ConfigParser
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from AdminPrivilegeCheck import checkNum
#import importlib




app = Flask(__name__)

config = ConfigParser()
config.read('config.cfg')
account = config.get('auth', 'account')
token = config.get('auth', 'token')

client = Client(account, token)


@app.route("/sms_inbound", methods=['GET', 'POST'])


#Receives the incoming SMS to process further for our client.
def incoming_sms():
   
    #Gets the message from sender and grabs the body of it.
    body = request.values.get('Body', None)
    resp = MessagingResponse()                               #Taken from Twilio helper library
    resp.message("This is the ship that made the Kessel Run in fourteen parsecs?")


    if str(body).lower() == "logon":
        resp.message("Checking your credentials...")
        print(resp)
        checkNum(request.values.get('From'))

    else:
        None

    return str(resp)


@app.route("/sms_outbound", methods=['GET', 'POST']) 
def outgoing_sms():
    body = request.values.get('Body', None)
    resp = MessagingResponse()                               #Taken from Twilio helper library
    resp.message("This is the ship that made the Kessel Run in fourteen parsecs?")
    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)