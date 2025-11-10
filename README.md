# Job_Alert_Bot

A Python automation tool that monitors job postings on the General Motors (GM) careers
website and sends SMS notifications when a matching position becomes available.
Built using Python, BeautifulSoup, Playwright, and Textbelt API. This project came about when a
close friend frequently manually checked the website for updates and I thought it'd make
a nice project. Initially I attempted to use Twilio, but was having issues with getting a phone number, so I chose textbelt instead.


## Features 
- **Automated listing monitoring** Periodically scrapes GM's careers page for new listings
- **Keyword filtering** Alerts only for positions that match predefined keyword e.g. "Production", "Engineering", etc.
- **SMS notification** When a new position is found, an SMS notification is sent via **Textbelt**
- **Terminal-based** Simple CLI interface, may add a GUI later as a practice. Who knows.

## Tech Stack
| Component | Description |
|-----------|-------------|
| **BeautifulSoup4** | HTML Parsing |
| **Playwright** | Browser automation |
| **Requests** | HTTP requests and web scraping |
| **Textbelt API** | SMS notification |
| **cron / schedule** | Automated periodic checks |
---


