#This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
import os


class NotificationManager:
    def __init__(self):
        self.twilio_account_sid = os.environ["twilio_account_sid"]
        self.twilio_auth_token = os.environ["twilio_auth_token"]
        self.twilio_phone_num = os.environ["twilio_phone_num"]
        self.my_phone_num = os.environ["my_phone_num"]

    def send_alert(self, price, city, code, out, ret):
        self.client = Client(self.twilio_account_sid, self.twilio_auth_token)
        self.message = self.client.messages \
            .create(
            body=f"""
                Low price alert! Only ${price} to fly from LONDON-STN to {city}-{code}, from {out} to {ret}.
                """,
            from_=self.twilio_phone_num,
            to=self.my_phone_num
        )

        print(self.message.status)
