from dotenv import load_dotenv
import os
from twilio.rest import Client   # ← this import is crucial!

# Load .env variables
load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone = os.getenv("TWILIO_PHONE")
my_phone = os.getenv("MY_PHONE")

client = Client(account_sid, auth_token)

# test sms
message = client.messages.create(
    body="Test message from Job Alert Bot!",
    from_=twilio_phone,
    to=my_phone
)

print("Message sent SID:", message.sid)
