from flask import Flask, request, redirect
from twilio.rest import Client
from twilio.twiml.messaging_response import Message, MessagingResponse

from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

     # Add a picture message
    #msg.media("https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


account_sid = "ACbd5b543679221d48c0d7fd6b6e1570c1"
# Your Auth Token from twilio.com/console
auth_token  = "63f71b2f8e403b313c598794ca8dfb6f" 

number="+19135968817"

def sendSMS(number, message):
	client = Client(account_sid, auth_token)
	message=client.messages.create(
	    to=number, 
	    from_="+18165337900",
	    body=message)

	print(message.sid)




sendSMS(number, message)


# response.message("What is your name?")
# name=body.lower()
# response.message("Hi there "+ name +". Tell me how you are feeling today. are you happy? sad? nervous? disappointed? angry? tired? average?")