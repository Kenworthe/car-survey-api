from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from bson import json_util
import json

print("hello world")

app = Flask(__name__)

# TODO: actually wire up the mongodb. put connection info into yaml file.
# TODO: REPLACE SEEEDS.JSON WITH DB INFO CONFIG.JSON
app.config['MONGO_DBNAME'] = 'pythonTest'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/pythonTest'
mongo = PyMongo(app)

def get_questions_from_seed():
	with app.open_resource('static/questions.json') as json_data:
		# questions = read(json_data)
		questions = json.load(json_data)
		return questions

def get_cars_from_seed():
	with app.open_resource('static/cars.json') as json_data:
		# questions = read(json_data)
		cars = json.load(json_data)
		return cars


@app.route("/", methods=['GET', 'POST'])
def home():

	if request.method == 'GET':

		# results = list(mongo.db.questions.find({}))
		# print(results)

		# first = results[0]

		# return json.dumps(results, default=json_util.default)
		return 'hello, this is the home page!'
		# return render_template('index.html', question = first["question"], choice_list = first["choices"])

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

@app.route("/questions", methods=['GET'])
def fetch_all_questions():
	# results = list(mongo.db.questions.find({}))
	# return json.dumps(results, default=json_util.default)
	results = get_questions_from_seed()
	return jsonify(results)

@app.route("/cars", methods=['GET'])
def fetchAllCars():
	# results = list(mongo.db.cars.find({}))
	# return json.dumps(results, default=json_util.default)
	results = get_cars_from_seed()
	return jsonify(results)

# @app.route("/cars/<make>", methods=['GET'])
# def fetchOneCar(make):
# 	results = list(mongo.db.cars.find({"make": make}))
# 	return json.dumps(results, default=json_util.default)

# @app.route("/refreshCars", methods=['GET'])
# def refreshCars():

# 	mongo.db.cars.delete_many({})

# 	mongo.db.cars.insert_many([
# 		{
# 			"make":"Honda",
# 			"model":"CR-V",
# 			"year":"2005", 
# 			"bodyType":"Luxury Sports SUV/Supercar"
# 		},
# 		{
# 			"make":"Toyota",
# 			"model":"RAV4",
# 			"year":"2018", 
# 			"bodyType":"Large Coupe"
# 		},
# 		{
# 			"make":"Tesla",
# 			"model":"Model S",
# 			"year":"2017", 
# 			"bodyType":"Electric"
# 		},
# 	])
# 	return "done!"

# @app.route("/refreshQuestions", methods=['GET'])
# def refreshQuestions():

# 	mongo.db.questions.delete_many({})

# 	mongo.db.questions.insert_many([
# 		{
# 			"id": "1",
# 			"question": "Would you want a new or used car?",
# 			"choices": ["New", "Used"]
# 		},
# 		{
# 			"id": "2",
# 			"question": "What is your budget?",
# 			"choices": []
# 		}
# 	])
# 	return "done!"

@app.route("/kenny")
def kenny():
	return "This is kenny's profile page."

# Instructions on how to launch our Flask server: 
# Type into Terminal:  python3 app.py

if __name__ == '__main__':
	app.run(host='0.0.0.0')
    # app.run(debug=True)
	# app.run()
