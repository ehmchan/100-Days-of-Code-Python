from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
p = Post()

@app.route('/')
def home():
    po = p.all_posts
    return render_template("index.html", posts=po)

@app.route('/post/<num>')
def blog(num):
    po = p.all_posts
    return render_template("post.html", posts=po, blogid=num)

if __name__ == "__main__":
    app.run(debug=True)
