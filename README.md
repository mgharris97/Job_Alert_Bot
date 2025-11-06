# Job_Alert_Bot

A Python automation tool that monitors job postings on the General Motors (GM) careers
website and sends SMS notifications when a matching position becomes available.
Built using Python, BeautifulSoup, Requests, and Twilio. This project came about when a
close friend frequently manually checked the website for updates and I thought it'd make
a nice project.


## Features 
- **Automated listing monitoring** Periodically scrapes GM's careers page for new listings
- **Keyword and location filtering** Alerts only for positions that match predefined keyword and location criteria
- **SMS notification** When a new position is found, an SMS notification is sent via **Twilio**
- **Terminal-based** Simple CLI interface, may add a GUI. Who knows.

## Tech Stack
| Component | Description |
|-----------|-------------|
| **BeautifulSoup4** | HTML Parsing |
| **Requests** | HTTP requests and web scraping |
| **Twilio API** | SMS notification |
| **cron / schedule** | Automated periodic checks |
---


