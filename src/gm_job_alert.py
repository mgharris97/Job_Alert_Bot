#import load_dotenv function from python-dotenv library
from dotenv import load_dotenv 
import os
## Import CLient class from Twilio's REST API 
from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
load_dotenv()

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone = os.getenv("TWILIO_PHONE")
my_phone = os.getenv("MY_PHONE")

#Twilio client initiate
client = Client(account_sid, auth_token)

#Test SMS
message = client.messages.create(
    body = "This is a test message",
    from_=twilio_phone, to=my_phone)

#print ("Message was sent using Twilio number")

#def fetch_jobs():
#   url = os.getenv("URL")


