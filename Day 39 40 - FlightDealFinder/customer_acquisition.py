import os
import requests

print("Welcome to Eugenia's Flight Club.\n"
      "We find the best flight deals and email you.")
first = input("What is your first name?\n").title()
last = input("What is your last name?\n").title()
email = input("What is your email?\n").lower()
confirm_email = input("Type your email again,\n").lower()

user_data = {
    "user": {
        "firstName": first,
        "lastName": last,
        "email": email,
    }
}

if email == confirm_email:
    endpoint = os.environ["SH_users"]
    add_user_response = requests.post(url=endpoint, json=user_data, auth=(os.environ["SH_USER"], os.environ["SH_PW"]))
    add_user_response.raise_for_status()

    print("Success! Your email has been added.")
else:
    print("Sorry emails do not match.")