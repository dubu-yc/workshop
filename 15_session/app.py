# Team Marshmallow: Liesel Wong (King Hagrid), Yoonah Chang (Yelena), Rachel Xiao (Mooana)
# SoftDev
# K15 -- Sessions Greetings
# 2021-10-18

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
<<<<<<< HEAD
from flask import session           #facilitate flask sessions


app = Flask(__name__)    #create Flask object
app.secret_key = "SoftDev is so fun" #sign session cookies for protection against cookie data tampering
username = "topher" #hardcode username and password
password = "mykolyk"


@app.route("/") #, methods=['GET', 'POST']
def disp_loginpage():
    #Root route loads welcome page if user is logged in or login page if no user is logged in
    #print(session.items())
    if username in session: #checks if user is logged in
        return render_template('response.html', username=username) #welcome page
    else:
        return render_template('login.html') #load login page if user isn't logged in


@app.route("/auth", methods=['GET', 'POST']) #handle both GET and POST requests
def authenticate():
    #user's inputs
    name = ""
    pas = ""

    if request.method == 'GET': #if request method is GET , use request.args
        name = request.args['username']
        pas = request.args['password']
    elif request.method == 'POST':
        name = request.form['username']
        pas = request.form['password']

    #check credentials and render welcome or error page
    try:
        if name != username and pas != password:
            return render_template('login.html', explain="Username and Password are wrong")
        elif name != username:
            return render_template('login.html', explain="Username is wrong")
        elif pas != password:
            return render_template('login.html', explain="Password is wrong")
        else:
            #add session data
            session[username] = password #when a user logs in, a session should be established with the username stored
            return render_template('response.html', username=request.args['username'])  #response to a form submission
    except: #handle all unexpected errors
        return render_template('login.html', explain="something went wrong :(")


@app.route("/logout")
def logout():
    if username in session:
        #print(session.items())
        session.pop(username)
        #print(session.items()) #the dictionary is empty
    return render_template('login.html')
=======

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. Can you predict which?
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests. Process results.
PROTIP: Insert your own in-line comments wherever they will help your future self and/or current teammates understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) # <Flask 'app'>
    print("***DIAG: request obj ***")
    print(request) # <Request 'http://127.0.0.1:5000/' [GET]> --after submitting form--> <Request 'http://127.0.0.1:5000/auth?username=hello&sub1=Submit+Query' [GET]>
                   # request shows the url of the localhost when tracking the form data
    print("***DIAG: request.args ***")
    print(request.args) # ImmutableMultiDict([]) --> ImmutableMultiDict([('username', 'hello'), ('sub1', 'Submit Query')])  |  (this creates a dictionary with
                        # [name of input tag: user input] 
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username']) # hello  |  (this prints the inputted username)
    print("***DIAG: request.headers ***")
    print(request.headers) # Host: 127.0.0.1:5000
    return render_template( 'login.html' )


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    if request.args['username'] != "topher" and request.args['password'] != "mykolyk":
    	return render_template('login.html', explain="Username and password are wrong")
    elif request.args['username'] != "topher":
    	return render_template('login.html', explain="Username is wrong")
    elif request.args['password'] != "mykolyk":
    	return render_template('login.html', explain="Password is wrong")
    else: 
    	return render_template('response.html', username=request.args['username'], password=request.args['password'])  #response to a form submission

>>>>>>> 3fc4df3693c2c5d07de58e98e58859991f0d2db0


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
