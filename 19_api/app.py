# Ducks: Yoonah Chang (Yelena), Josephine Lee (Kitty)
# SoftDev
# K19 -- A RESTful Journey Skyward
# 2021-11-23
# time spent: 1.0 hours

from flask import Flask, render_template
from urllib import request
import json

app = Flask(__name__)


@app.route("/")
def main():
    resp = request.urlopen("https://api.nasa.gov/planetary/apod?api_key=bg1bOijQFnDyPQQInDutrR8tuhxQmw5JdcQCEMkS")
    #gets the info from the URL link with the specific api key
    data = json.load(resp)
    #changes the string data into a dictionary called data
    imglink = data["url"]
    #makes a variable imglink hold the value of url that is inside of data dictionary
    pic_explanation = data["explanation"]
    #makes a variable pic_explanation hold the value of explanation that is inside of data dictionary

    print (resp)
    print (data)
    print (imglink)
    print (pic_explanation)

    #prints and displays on webpage
    return render_template("main.html", pic = imglink, explanation = pic_explanation)

if __name__ == "__main__":
    app.debug = True
    app.run()
