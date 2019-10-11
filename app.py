from flask import Flask, render_template, redirect, request
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    #return "Hello"
	# now = datetime.datetime.now()
	# newDay = now.day
	# newMonth = now.month
	# newYear = newDay == 1 and newMonth == 1
	# newYear = True
	names = ["Nana","King","Prempeh","A","Thank You God, I'm getting there "]
	return render_template("index.html", content = names )

@app.route("/prempeh")
def prempeh():
	title = "ANGELA MY LOVE"
	return render_template("index.html", content = title)

@app.route("/donate", methods=["GET","POST"])
def donate():
	name = request.form.get("name")
	return render_template("donate.html", content = name )


@app.route("/nana")
def nana():
	return "Welcome Nana Prempeh"


# @app.route("/final")
# def final():
# 	return "Ok, learn at your pace and push yourself"
	
# @app.route("/<string:name>")
# def name(name):
# 	name = name.upper()
# 	return f"Welcome {name}"




