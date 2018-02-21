from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import json

app = Flask(__name__)

print("hello world")

seeds = {}
with open("seeds.json") as json_data:
	seeds = json.load(json_data)


# Example of a For Loop:

# for word in myList:
# 	print(word)


@app.route("/", methods=['GET', 'POST'])
def hello():

	if request.method == 'GET':
		question = seeds["question1"]["question"]
		choice_list = seeds["question1"]["choices"]

		return render_template('index.html', question = question, choice_list = choice_list)

	if request.method == 'POST':
	
		question = request.form.get('question')
		selection = request.form.get('selection')

		print(question + ' ' + selection)

		# save choice from POST json to "selected choices object"

		# use business logic to determine next question based on that choice

		# pull next question from DB

		#return JSON for next question as "data"

		data = {}
		return jsonify(data)


@app.route("/kenny")
def kenny():
	return "This is kenny's profile page."


# Instructions on how to launch our Flask server: 
# Type into Terminal:  python3 app.py

if __name__ == '__main__':
    app.run(debug=True)