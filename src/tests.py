from dotenv import load_dotenv
import os
#from requests_html import HTMLSession
import requests



from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
    context = browser.new_context(user_agent=(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/118.0.5993.117 Safari/537.36"
    ))
    page = context.new_page()
    page.goto("https://search-careers.gm.com/en/jobs/?search=&country=United+States+of+America&region=Indiana&location=Roanoke&pagesize=20#results", timeout=60000)
    page.wait_for_timeout(10000) 
    html = page.content()
    print(html[:1000])
    browser.close()

