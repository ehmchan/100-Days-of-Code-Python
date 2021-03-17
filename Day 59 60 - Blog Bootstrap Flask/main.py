from flask import Flask, render_template, request
import requests
import smtplib
import os

blog_response = requests.get(url=f"https://api.npoint.io/0996c981cff4e74026a9")
posts = blog_response.json()
send_email = os.environ["email"]
pw = os.environ["email_pw"]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=send_email, password=pw)
            connection.sendmail(
                from_addr=send_email,
                to_addrs=send_email,
                msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")

        return render_template("contact.html", meth=request.method)
    else:
        return render_template("contact.html")

@app.route('/post/<int:num>')
def show_post(num):
    requested_post = None
    for post in posts:
        if post["id"] == num:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
