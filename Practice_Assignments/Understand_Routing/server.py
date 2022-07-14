'''1. Understanding Routing'''

# Practice building a server with Flask from scratch
# Get comfortable with routes and passing information to the routes

from distutils.log import debug
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<name>')
def hello(name):
    print(name)
    return "Hi " + name


@app.route('/repeat/<int:num>/<string:banana>')
def heya(banana,num):
    return f"{banana * num}"

if __name__ == "__main__":

    app.run(debug=True)

#4.

#Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times

