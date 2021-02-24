#This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
import os
import smtplib


class NotificationManager:
    def __init__(self):
        self.twilio_account_sid = os.environ["twilio_account_sid"]
        self.twilio_auth_token = os.environ["twilio_auth_token"]
        self.twilio_phone_num = os.environ["twilio_phone_num"]
        self.my_phone_num = os.environ["my_phone_num"]
        self.my_email = os.environ["my_email"]
        self.email_pw = os.environ["email_pw"]


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

    def send_email(self, price, city, code, out, ret, to_email):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.email_pw)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=to_email,
                msg=f"Subject:Flight Deal!\n\nLow price alert! Only ${price} to fly from LONDON-STN to {city}-{code}, from {out} to {ret}.\n"
                    f"https://www.google.com/flights?hl=en#flt=STN.{code}.{out}*{code}.STN.{ret}")

