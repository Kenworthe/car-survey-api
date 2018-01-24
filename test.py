
from flask import Flask
app = Flask(__name__)


print("hello world")

a = 1
b = 2
c = 'Sarath'
d = "sarath"
 
# print (a,b,c,d)
# print (c+d)

myList = [a, b, c, d, "sarath24"]

for x in myList:
    print (x)


@app.route("/")
def hello():
    return "Hello World"