from distutils.log import debug
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

if __name__=='__main__':
    app.run(debug=True)