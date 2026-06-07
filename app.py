from flask import Flask, render_template, request, redirect, url_for, session
import re

app = Flask(__name__)
import os
app.secret_key = os.environ.get("SECRET_KEY", "birthday_secret_2024")

VALID_Q1 = {"amogh", "amogh gupta", "amoghgupta"}
VALID_Q2 = {"forever", "infinity"}

def check_q1(val):
    return re.sub(r'\s+', ' ', val.strip().lower()) in VALID_Q1

def check_q2(val):
    return val.strip().lower() in VALID_Q2

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        a1 = request.form.get("q1", "")
        a2 = request.form.get("q2", "")
        if check_q1(a1) and check_q2(a2):
            session["verified"] = True
            return redirect(url_for("birthday"))
        else:
            error = "Oops! Wrong answers, my love 💕 Try again..."
    return render_template("login.html", error=error)

@app.route("/birthday")
def birthday():
    if not session.get("verified"):
        return redirect(url_for("login"))
    return render_template("birthday.html")

@app.route("/breakup")
def breakup():
    if not session.get("verified"):
        return redirect(url_for("login"))
    return render_template("breakup.html")

@app.route("/noway")
def noway():
    if not session.get("verified"):
        return redirect(url_for("login"))
    return render_template("noway.html")

if __name__ == "__main__":
    app.run(debug=True)
