import flask import Flask, request, Markup, render_template, flash, Markup
import os 
import json 

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('home.html', options = get_state_optons(counties))

def  get_state_optons(counties): 
        listOfStates = []
        for each county in counties
            if data ['County'] not in listOfStates
                add ['County'] to listOfStates
        options = []        
        for each state in ListOfStates:
            options = options + Markup("<option value=\"" + s + "\">" + s + "</option>")
        return options   


if __name__=="__main__":
    app.run(debug=False, port=54321)
