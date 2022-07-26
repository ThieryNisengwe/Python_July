from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def checkerboard():
    return render_template("index.html",x=8,y=8,a='black',b='red')


@app.route("/4")
def checkerboard4():
    return render_template("index.html",x=8,y=4)

@app.route('/<int:num1>/<int:num2>')
def checkerboardx(num1,num2):
    return render_template('index.html',x=num1,y=num2)

@app.route('/<int:num1>/<int:num2>/<color1>/<color2>')
def checkerboardclr(num1,num2,color1,color2):
    return render_template('index.html',x=num1,y=num2,a=color1,b=color2)



if __name__=="__main__":
    app.run(debug=True)