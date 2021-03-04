# Has Big Lurm been fed?

from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from datetime import datetime
from pyfirmata import Arduino, util
import platformio
import time

"""
board = Arduino("/dev/ttyACM0")

iterator = util.Iterator(board)
iterator.start()

force_1 = board.get_pin("a:0:i")
time.sleep(1.0)
print("Force applied", force_1.read())
"""

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

db = SQLAlchemy(app)

class Shlurm(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    time_fed = db.Column(db.String(50))

@app.route("/", methods = ["GET"])

def index():
    # Show time fed
    big_Shlurm = Shlurm.query.all() # a
    shlurm_fed_list = [big_Shlurm.pop().time_fed] # b
    shlurm_fed = shlurm_fed_list # c
    total_fed = 0
    total_fed = Shlurm.query.count() # d
    cache.clear()

    return render_template("index.html", shlurm_fed = shlurm_fed_list, total_fed = total_fed)

    # To restart db, comment out lines a, b, c and d, and comment everything after "index.html" and add ) after it. Then uncomment everything. Hacks.

@app.route("/add_fed", methods = ["GET", "POST"])

def add_fed():
    timestamp = str(datetime.now().strftime("%c"))
    time_fed = Shlurm(time_fed = timestamp)
    db.session.add(time_fed)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/refresh", methods = ["GET", "POST"])

def refresh():
    big_Shlurm = Shlurm.query.all()
    big_Shlurm = Shlurm.query.all()
    shlurm_fed_list = [big_Shlurm.pop().time_fed]
    shlurm_fed = shlurm_fed_list
    return redirect(url_for("index"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)

# source ~/Dropbox/Developer/Projects/Shlurm_Automator/venv/bin/activate