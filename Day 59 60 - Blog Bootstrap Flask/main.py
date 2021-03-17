from flask import Flask, render_template
import requests

blog_response = requests.get(url=f"https://api.npoint.io/0996c981cff4e74026a9")
posts = blog_response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
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
