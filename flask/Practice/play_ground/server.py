from distutils.log import debug
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def playground():
    times = 3 
    return render_template("index.html",times = times)


@app.route('/play/<num>/<color>')
def playground_times(num,color):
    times = int(num)
    return render_template("index.html",times = times,color = color)

if __name__=="__main__":
    app.run(debug=True)