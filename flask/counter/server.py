from flask import Flask,render_template,redirect,request,session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

count = 0 

@app.route("/")
def counter():
    print(request.form)
    global count
    count += 1 
    return render_template("index.html", count = count)

@app.route('/addTwo',methods =['POST'])
def addTwo():
    print('GLOBAL COUNT =')
    global count
    count += 1
    print(count)
    return redirect('/')

@app.route('/reset',methods=['POST'])
def reset():
    global count
    count = 0 
    print(count)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
