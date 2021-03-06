'''Hello, Flask!'''

# 1 Inside the "hello_flask" folder, create a file called server.py
# This will be our "server" file where we will set up all of our routes to handle requests.
# You'll want to create a new folder for each assignment moving forward. It will seem tedious at first, but as we add additional files to each project, we'll want to keep everything organized by assignment/project!

# 2 Finally, put the following code inside of server.py:

from ast import Num
# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/s')
def hello_world():
    # Return the string 'Hello World!' as a response
    return render_template("index.html")


@app.route('/Thiery')
def hey_me():
    return 'Hey Thiery Howya doing'


@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello," + name


@app.route('/hello/<string:banana>/<int:num>')
def heya(banana, num):
    return f"Hello {banana * num}"


@app.route('/')
def index():
    # notice the 2 new named arguments!
    return render_template("hello.html", phrase="Hello", times=5)


@app.route('/box')
def boxes():
    return render_template("box.html", times=3)


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27}
    ]
    return render_template("lists.html", random_numbers=[3, 1, 5], students=student_info)


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

# Notice how we are accessing the app object and running the route method, passing in a string that is the route that we want to add to our application. You must do this for every route that you want to add to our application.

# Note: Moving forward, you may see some red squiggly lines under your import statements because your text editor's linter doesn't recognize packages in your virtual environment. You can ignore them unless running the file actually gives you errors!

# Now run the application by navigating to your project directory and running the following command. Be sure the virtual environment is activated.
