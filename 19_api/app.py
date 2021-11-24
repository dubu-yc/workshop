# Ducks: Yoonah Chang (Yelena), Josephine Lee (Kitty)
# SoftDev
# K19 -- A RESTful Journey Skyward
# 2021-11-23
# time spent: 1.0 hours

from flask import Flask, render_template
from urllib3 import request
import json

app = Flask(__name__) 


@app.route("/") 
def main():
    resp = request.urlopen("https://api.nasa.gov/planetary/apod?api_key=bg1bOijQFnDyPQQInDutrR8tuhxQmw5JdcQCEMkS")
    
    data = json.load(resp)
  
    imglink = data['url']
                  
    pic_explanation = data['explanation']
    
    print (resp)
    print (data)
    print (imglink)
    print (pic_explanation)

    return render_template("main.html", img = imglink, pic_explanation)

if __name__ == "__main__":
    app.debug = True
    app.run()
