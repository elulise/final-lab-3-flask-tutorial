# Elise Ullestad
# SE 331 Software Engineering Class
# Lab 3
# https://code.visualstudio.com/docs/python/tutorial-flask 
# Activate Environment .venv\Scripts\Activate.ps1
# python -m flask run

import re
from datetime import datetime
from flask import render_template

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/hello/<name>")
def hello_there(name):
    print("http://127.0.0.1:5000/hello/VSCode")
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend" 

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content 

    
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")