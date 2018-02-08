from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

print("hello world")

seeds = {}
with open("seeds.json") as json_data:
	seeds = json.load(json_data)


# Example of a For Loop:

# for word in myList:
# 	print(word)


@app.route("/")
def hello():
	# business logic goes here
	
	# question = "Question from DB goes here!"
	# choice_list = ["choice A", "choice B", "choice C", "choice Z"]

	question = seeds["question1"]["question"]
	choice_list = seeds["question1"]["choices"]

	return render_template('index.html', question = question, choice_list = choice_list)

@app.route("/kenny")
def kenny():
	return "This is kenny's profile page."

# Instructions on how to launch our Flask server: 
# Type into Terminal:  FLASK_APP=app.py flask run