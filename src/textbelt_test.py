from dotenv import load_dotenv
import os
#from requests_html import HTMLSession
import requests
load_dotenv()

resp = requests.post('https://textbelt.com/text', {
  'phone': os.getenv("MY_PHONE"),
  'message': 'Hello world',
  'key': os.getenv("TEXTBELT_KEY"),
})
print(resp.json())

