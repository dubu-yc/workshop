# Team Sneakers: Yoonah Chang (Yelena), Kevin Cao (Pipi), Michael Borczuk (Liberty and Baby Yoda)
# SoftDev
# K10 -- Putting Little Pieces Together
# 2021-10-04

from flask import Flask
app = Flask(__name__)  # create instance of class Flask


@app.route("/")  # assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)  # where will this go? - terminal
    return "No hablo queso!"


app.run()

'''
It will be similar to v0, but with an extra print statement in the terminal that says "about to print __name__..."
'''
