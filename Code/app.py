from flask import Flask, redirect, url_for, request, render_template
import flask_login
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

app = Flask(__name__)
app.secret_key = 'super secret string'  # Change this!

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


@app.route('/login', methods = ["POST","GET"])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    email = request.form['email']
    if email in users and request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'


@app.route('/register')
def register():
    return render_template("debug.html") #Sends the client to the void

@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

#@app.route('/salt',methods = ['POST', 'GET'])
#def salt():
    ...

#Flask Login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


users = {'a': {'password': 'a'}}

class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user

if __name__ == '__main__':


    app.run()