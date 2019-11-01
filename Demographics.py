import flask import Flask, request, Markup, render_template, flash, Markup
import os 
import json 

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

def your_interesting_demographic_function(counties):
    get_state_optons
        List lostOfStates is initialized to an empty list
        for each county in counties
            if data ['county'] not in listOfStates
                add 


if __name__=="__main__":
    app.run(debug=False, port=54321)
