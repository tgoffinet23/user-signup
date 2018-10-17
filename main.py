from flask import Flask, request, redirect, render_template
import cgi
import os
import string

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return redirect("/signup")


@app.route("/signup")
def DisplaySignup():
    return render_template('form.html')


@app.route("/signup", methods= ['POST'])
def ValidateSignup():
    username = cgi.escape(
        request.form['username'])
    password = cgi.escape(
        request.form['password'])
    Confirmpass = cgi.escape(
        request.form['verify'])
    email = cgi.escape(
        request.form['email'])

    usernameError = ""
    passwordError = ""
    ConfirmpassError = ""
    emailError = ""

    if  username == "":
        usernameError = "That's not a valid username"
    elif len(username) > 20 or len(username) < 3:
        usernameError = "That's not a valid username"

    if password == "":
        passwordError = "That's not a valid password"
    elif len(password) > 20 or len(password) < 3:
        passwordError = "That's not a valid password"
    
    if Confirmpass == "":
        ConfirmpassError = "The passwords don't match"
    elif not password == Confirmpass:
        ConfirmpassError = "The passwords don't match"

   
    if len(email) > 0:
        if email.count("@") < 1:
            emailError = "Does not have an @ symbol"
        elif email.count(".") < 1:
            emailError = "Does not have a . symbol"
        elif email.count(" ") > 0:
            emailError = "You need to enter a email"
        elif len(email) > 20 or len(email) < 3:
            emailError = "Does not have at least 3 letter and less than 20"
    
    if not usernameError and not passwordError and not ConfirmpassError and not emailError:
        return redirect('/welcome?username= {0}'.format(username))
        #return "<h1> Hello, "+ username +"! </h1>"
    else:
        return render_template('form.html', 
            username= username, usernameError= usernameError, 
            passwordError= passwordError, ConfirmpassError= ConfirmpassError,
            email= email, emailError= emailError)


@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username= username)



app.run()
