from flask import Flask, request, Markup, render_template, flash, Markup
import os 
import json 

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('home.html', options = get_state_optons(counties))
    

@app.route("/FunFacts")
def FunFact():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('FunFacts.html', options = get_state_optons(counties))

def  get_state_optons(counties): 
        listOfStates = []
        for data in counties:
            if not (data ['State'] in listOfStates):
                listOfStates.append (data['State'])
        options = '' 
        for data in listOfStates:
            options = options + Markup("<option value=\"" + data + "\">" + data + "</options>")
        return options   
       
@app.route("/FunFacts")
def render_FunFacts():
    fact = request.args['FunFact']
    for data in counties:
        if fact == ['State']:
            response = ['Language Other than English at Home']
    
        return render_template('response.html', responseFromServer=response)   


if __name__=="__main__":
    app.run(debug=False, port=54321)
