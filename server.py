from flask import Flask
app = Flask(__name__)

print("hello world")


# Example of a For Loop:

# for word in myList:
# 	print(word)


@app.route("/")
def hello():
	# business logic goes here
	a = 1
	b = 2
	c = "Kenny1"
	d = 'Homepage!!!'

	myList = [a, b, c, d, "Kenny3"]

	# by default, Flask requires return a String
	# goal is to learn how to return an .html file
	return d

@app.route("/kenny")
def kenny():
	return "This is kenny's profile page."

# Instructions on how to launch our Flask server: 
# Type into Terminal:  FLASK_APP=hello.py flask run