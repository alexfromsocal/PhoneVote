from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse as MR
from twilio.rest import Client
import importlib



app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])


def incoming_sms():
    