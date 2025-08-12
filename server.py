# save this as app.py
from flask import Flask, render_template,send_from_directory

app = Flask(__name__)

@app.route("/")
def hello(username=None,post_id=None):
    return render_template('index.html', name=username, post_id=post_id)
    #return "Hello, World!"


@app.route("/about")
def about():
    return "This is the about page"


#print(hello())