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


def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    # if body.lower()=="good":
    message="Hi I'm IRIS, an Immediately Responsive Intelligent System"
    user=request.form['Body']

    if user=="good":
        message="Glad to hear it! I hope you continue to feel this way! Celebrate this feeling and hold onto what happened ot make you feel this way so that you can repeat it in the future!"

    if user=="sad"
        message="I’m sorry to hear that. Here are some things I do to make me feel better: take a walk outside, listen to uplifting music, call or message a loved one, or watch or read something positive to take my mind off of what I’m feeling."

    if user=="nervous"
        message="It’s going to be ok! This feeling will not last forever."
    if user=="lonely"
        message="I’m here for you and know that you are loved, supported, and important. The world would not be the same without you! For a loving quote respond"

    if user=="angry"
        message="“Let me help you turn your anger into something positive. Here are some ways to burn off energy productively: take a long walk, remove yourself from the situation, paint of draw, listen to loud music, or take a break from what you are doing."

    if user=="tired"
        message="I understand what you are feeling well. I recommend taking a break to do an activity you enjoy, taking a nap, getting a coffee, doing 20 jumping jacks, listening to a pump-up playlist, or standing up to stretch for a bit."

    if user=="average"
        message="There are many things to look forward to!"
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





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
# response.message("What is your name?")
# name=body.lower()
# response.message("Hi there "+ name +". Tell me how you are feeling today. are you happy? sad? nervous? disappointed? angry? tired? average?")

