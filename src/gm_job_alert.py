#import load_dotenv function from python-dotenv library
import requests
#from requests_html import HTMLSession
from dotenv import load_dotenv 
import os
## Import CLient class from Twilio's REST API 
from twilio.rest import Client
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

load_dotenv()

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone = os.getenv("TWILIO_PHONE")
my_phone = os.getenv("MY_PHONE")

#Twilio client initiate
client = Client(account_sid, auth_token)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
    context = browser.new_context(user_agent=(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/118.0.5993.117 Safari/537.36"
    ))
    page = context.new_page()
    page.goto(os.getenv("URL"), timeout=60000)
    page.wait_for_timeout(5000)  # wait 5s
    rendered_site = page.content()
    print(rendered_site[:1000])
    browser.close()

    soup = BeautifulSoup(rendered_site, "html.parser")
    jobs=[]
    for i in soup.select("a.stretched-link", limit=10):
        #Extract all text in <a> tag removing leading and trailing white spaces
        title = i.get_text(strip=True)
        ##i.get("href","") returns and appends value of the href attribute from <a> tag to the main url
        link = "https://search-careers.gm.com" + i.get("href", "")
        #store the job and link in the jobs list 
        jobs.append((title, link))
    #if jobs is empty...
    if not jobs:
        print ("no job found")
    else:
        #print job titles and links 
        for title, link in jobs:
            print(title, "->", link)

        
        











