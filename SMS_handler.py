from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse as MR
from twilio.rest import Client
import importlib



app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])



#Receives the incoming SMS to process further for our client.
def incoming_sms():
    
    #Gets the message from sender and grabs the body of it.
    body = request.values.get('Body', None)
    resp = MessagingResponse()


if __name__ == "__main__":
    app.run(debug=True)