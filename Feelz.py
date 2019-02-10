from flask import Flask, request, Response
import random
from twilio.rest import Client
#import imageio
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
import os.path
import datetime
import vobject

# Your Account SID from twilio.com/console
account_sid = "ACbd5b543679221d48c0d7fd6b6e1570c1"
# Your Auth Token from twilio.com/console
auth_token  = "63f71b2f8e403b313c598794ca8dfb6f"

number="+19135968817"


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        return handle_request(request.form)

def sendSMS(number, message):
	client = Client(account_sid, auth_token)
	message=client.messages.create(
	    to=number, 
	    from_="+18165337900",
	    body=message)

	print(message.sid)

# converting url to text
def urlToText(url):
	userResp=requests.get(url)
	return (userResp.text)

def handle_request(request_data):
	response = MessagingResponse()
	body = request_data['Body'].strip()
	phone_number = request_data['From']
	body = request_data['Body'].strip()
	response = MessagingResponse()
	message = Message()
	message.body('Hello World!')
	response.append(message)

	sendSMS(number, message)
	response.message("What is your name?")
	name=body.lower()

	response.message("Hi there "+ name +". Tell me how you are feeling today. are you happy? sad? nervous? disappointed? angry? tired? average?")

	# images = []
	# for filename in filenames:
	#     images.append(imageio.imread(filename))
	# imageio.mimsave('/path/to/movie.gif', images)

	if (body.lower()=="happy"):

		response.message("I'm glad to hear that you are happy, "+ name)


	if (body.lower()=="sad"):

		response.message("I'm sorry to hear that, "+ name + "Here are something I do to feel better:\nTake a walk outside]\nListen to uplifting music\nCall or text a loved one\n")
		response.message("Would you like to see a gif that could cheer you up?")

		if(body.lower() =="yes"):
			
			response.message("yeah boi")
			import requests
			import shutil

			url = 'https://media.giphy.com/media/Y8tW6EgVscvGo/giphy.gif'
			response = requests.get(url, stream=True)
			with open('img.png', 'wb') as out_file:
				shutil.copyfileobj(response.raw, out_file)
			del response
		

		if(body.lower()=="no"):
		
			response.message("That is alright, Thanks for chatting with me. I hope you feel better")
		

	if (body.lower()=="nervous"):

		response.message("It's going to be okay, take a few deep breaths with me")
		#breathing gif that katie is providing

	if(body.lower()=="lonely"):

		response.message("Damn lol you feelin lonely? you god damn loser lmfao bet you ain't ever gotten pussy in your life bruh")
		response.message("Im sorry to hear that, "+ name +" I am here for you and I want you to know that you are loved and supported")
		#insert hugging gifs

	if(body.lower()=="angry"):

		response.message("Im sorry to hear that, "+ name +" Let me help you turn your angry energy into something positive")
		response.message("Here are some ways ot burn off energy productively:\n Take a long walk\n Listen to uplifting music")

	if(body.lower()=="tired"):

		response.message("I understand. I recommend taking a break and doing an activity you enjoy. Maybe some excercises will work")


	if (body.lower()=="average"):

		response.message("I'm sorry, get better")

