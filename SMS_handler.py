from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse as MR
from twilio.rest import Client
from configparser import ConfigParser as cp
import importlib




app = Flask(__name__)

config = cp.ConfigParser()
config.read('config.cfg')
account = config.get('auth', 'account')
token = config.get('auth', 'token')


@app.route("/sms", methods=['GET', 'POST'])
client = Client(account, token)


#Receives the incoming SMS to process further for our client.
def incoming_sms():
    
    #Gets the message from sender and grabs the body of it.
    body = request.values.get('Body', None)
    resp = MR.MessagingResponse()                               #Taken from Twilio helper library
    resp.message("This is the ship that made the Kessel Run in fourteen parsecs?")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)