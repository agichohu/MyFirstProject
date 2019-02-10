from flask import Flask, request, redirect
from twilio.rest import Client
from twilio.twiml.messaging_response import Message, MessagingResponse

from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse




account_sid = "ACbd5b543679221d48c0d7fd6b6e1570c1"
# Your Auth Token from twilio.com/console
auth_token  = "63f71b2f8e403b313c598794ca8dfb6f" 

number="+19135968817"



app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
# def main():
#     if request.method == 'POST':
#         return handle_request(request.form)

# def handle_request(request_data):
#     response = MessagingResponse()
#     body = request_data['Body'].strip()
message ="Hi I'm IRIS, an Immediately Responsive Intelligent System"

def sms_reply(message):
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    # if body.lower()=="good":

    resp = MessagingResponse()
	    # Add a message
    
    resp.message(message)

	     # Add a picture message
	    #msg.media("https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg")

    return str(resp)

def sendSMS(number, message):
    client = Client(account_sid, auth_token)
    message=client.messages.create(
        to=number, 
        from_="+18165337900",
        body=message)

    print(message.sid)

    sendSMS(number, message)

    message="How are you feeling today? "

    sendSMS(number, message)
    #if body.lower()=='sad'

message="I'm glad to hear that. You are amazing! Remember that"

sms_reply(message)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
# response.message("What is your name?")
# name=body.lower()
# response.message("Hi there "+ name +". Tell me how you are feeling today. are you happy? sad? nervous? disappointed? angry? tired? average?")

