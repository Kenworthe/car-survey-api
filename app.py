from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from bson import json_util
import json

print('Hi! Running car-survey-api...')

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

		return 'Hello, welcome to the car-survey API! Visit /api/questions or /api/cars for data.'

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

@app.route("/api/questions", methods=['GET'])
def fetch_all_questions():
	# results = list(mongo.db.questions.find({}))
	# return json.dumps(results, default=json_util.default)
	results = get_questions_from_seed()
	return jsonify(results)

@app.route("/api/cars", methods=['GET'])
def fetchAllCars():
	# results = list(mongo.db.cars.find({}))
	# return json.dumps(results, default=json_util.default)
	results = get_cars_from_seed()
	return jsonify(results)

# @app.route("/cars/<make>", methods=['GET'])
# def fetchOneCar(make):
# 	results = list(mongo.db.cars.find({"make": make}))
# 	return json.dumps(results, default=json_util.default)


# Instructions on how to launch our Flask server: 
# Type into Terminal:  python3 app.py

# TODO: change below host='0.0.0.0' to be production-ready.

if __name__ == '__main__':
	app.run(host='0.0.0.0')
    # app.run(debug=True)
	# app.run()
