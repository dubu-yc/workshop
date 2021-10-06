# Team Sneakers: Yoonah Chang (Yelena), Kevin Cao (Pipi), Michael Borczuk (Liberty and Baby Yoda)
# SoftDev
# K10 -- Putting Little Pieces Together
# 2021-10-04

from flask import Flask
import csv
import random
app = Flask(__name__)  # create instance of class Flask


dict = {}

with open('occupations.csv', mode='r') as file:

    # reading the CSV file
    csvFile = csv.DictReader(file)

    # add contents to dictionary, multiply by 10 to make probabilities easier
    for lines in csvFile:
        dict[lines['Job Class']] = float(lines['Percentage']) * 10
    dict.pop('Total')


def print_occupations():
    return "<br />".join(dict.keys())


def choose():

    # generate a random integer
    num = random.randint(0, 999)

    counter = 0

    # adds to counter, once it passes randomly generated number, it prints the key
    for key in dict.keys():
        if counter + dict[key] > num:
            return(key)
            # exit loop once we've found our job
            break
        else:
            counter += dict[key]
            # continue to next iteration so we don't print Jobless every time
            continue
        # if the random int doesn't fall within any range, there is no job
    return("Other Job")


@app.route("/")  # assign fxn to route
def main():
    return heading() + "<br/>" + occupations()


def heading():
    return "<h2> Team Sneakers: Yoonah Chang (Yelena), Kevin Cao (Pipi), Michael Borczuk (Liberty and Baby Yoda) </h2>"


def occupations():
    occupations = print_occupations()
    occupation = "Your occupation is: " + choose()
    return f"<b>List of occupations:</b> <br/><br/> {occupations} <br/><br/> <b>{occupation}</b>"


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
