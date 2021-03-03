from bs4 import BeautifulSoup
import requests
import smtplib
import os

head = {
    "Accept-Language": os.environ["Accept_Language"],
    "User-Agent": os.environ["User_Agent"]
}

URL = "https://www.amazon.ca/gp/product/B00W9XANYY/ref=ox_sc_saved_title_1?smid=AP6E4D3HTEWA&psc=1"

response = requests.get(url=URL, headers=head)
amazon_webpage = response.text
soup = BeautifulSoup(amazon_webpage, "html.parser")

item = soup.find(name="span", id="productTitle").text
item_name = item.strip()

current_cost = soup.find(name="span", id="priceblock_ourprice").text
price = float(current_cost.split()[1])

if price <= 29:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=os.environ["my_email"], password=os.environ["email_pw"])
        connection.sendmail(
            from_addr=os.environ["my_email"],
            to_addrs=os.environ["my_email"],
            msg=f"Subject:Amazon Price Alert!\n\n{item_name} is now ${price}\n\n"
                f"{URL}")
