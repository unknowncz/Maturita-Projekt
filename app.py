
from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)

@app.route('/',methods = ["POST", "GET"])
def home():
    if request.method == "POST": #Checks if the request was POST

        if request.form.get("loginbutton") == "Log In" : #Checks if the request form has a name "loginbutton" with the value "Log In"
            return redirect("/login") #Redirects to login page

        elif request.form.get("registerbutton") == "Register": 
            return redirect("/register")

        else:
            print("yall fucked up") #Yall fucked up

    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template("debug.html") #Sends the client to the void

#@app.route('/salt',methods = ['POST', 'GET'])
#def salt():
    ...



if __name__ == '__main__':


    app.run()