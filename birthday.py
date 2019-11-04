import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    birthday = now.month == 8 and now.day == 17
    return render_template("index.html", birthday=birthday)