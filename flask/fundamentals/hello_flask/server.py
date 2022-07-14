'''Hello, Flask!'''

# 1 Inside the "hello_flask" folder, create a file called server.py
# This will be our "server" file where we will set up all of our routes to handle requests.
# You'll want to create a new folder for each assignment moving forward. It will seem tedious at first, but as we add additional files to each project, we'll want to keep everything organized by assignment/project!

# 2 Finally, put the following code inside of server.py:

from ast import Num
from flask import Flask  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/Thiery')
def hey_me():
    return 'Hey Thiery Howya doing'


@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello," + name

@app.route('/hello/<string:banana>/<int:num>')
def heya(banana,num):
    return f"Hello {banana * num}"


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

# Notice how we are accessing the app object and running the route method, passing in a string that is the route that we want to add to our application. You must do this for every route that you want to add to our application.

# Note: Moving forward, you may see some red squiggly lines under your import statements because your text editor's linter doesn't recognize packages in your virtual environment. You can ignore them unless running the file actually gives you errors!

# Now run the application by navigating to your project directory and running the following command. Be sure the virtual environment is activated.
