# Ducks: Yoonah Chang (Yelena), Josephine Lee (Kitty)
# SoftDev
# K19 -- A RESTful Journey Skyward
# 2021-11-23
# time spent: 1.0 hours

from flask import Flask, render_template
import requests
app = Flask(__name__) 

with open("key_nasa.txt", "r", encoding="utf-8") as api:
    NasaAPIKey = api.read().strip()

@app.route("/") 
def main():
    api_request = requests.get("https://api.nasa.gov/planetary/apod", params={"api_key": NasaAPIKey})
    if api_request.status_code == 200:
        pic_explanation = api_request.json()["explanation"]
        pic = api_request.json()["hdurl"]
        return render_template("main.html", pic=pic, pic_explanation=pic_explanation)

    return render_template("main.html")

if __name__ == "__main__":
    app.debug = True
    app.run()