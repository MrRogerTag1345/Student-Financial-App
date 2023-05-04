"""
-------------------------------------------------------
[Python program that acts as a backend for a Student Financial Web Application.
It uses the Flask framework to control HTML reasources and navigate
users to diffrent endpoints of the website.]
-------------------------------------------------------
Author: Lorand Kis
ID: 210629580
Email: lorandkis101@gmail.com
__updated__ = "2023-02-20"
-------------------------------------------------------
"""
# Imports
import requests
import pandas as pd
import json


from flask import Flask, render_template, url_for, request

# Function for reading an API from the below link
def readAPI():
    api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(api_url)
    if (response.status_code < 300):
        jRes = response.json()

    else:
        jRes = 'Error: ' + str(response.status_code)
    return jRes


# Function for formating JSON DATA for user view
def formatAPI(inAPI):
    df = pd.json_normalize(readAPI())
    outAPI = df.to_string()
    return outAPI

# ----- DATA STRUCTURES FOR USER INFORMATION -------

# Class for Settings Information 
class SettingD:
    def __init__(self, curr = None, lan = None, pas = None, confpas = None):
        assert (pas == confpas), "Passwords are not the same!"
        self.curr = curr
        self.lan = lan
        self.pas = pas
        self.confpas = confpas      

    def get_settings():
        currency = request.form.get("currency")
        language = request.form.get("language")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        return currency, language, password, confirm_password

# Data structure for Income 
class IncomeCellD:
    def __init__(self, source, amount, date, recurring):
        self.source = source
        self.amount = amount
        self.date = date
        self.recurring = recurring

# Data structure for a users complete set of Incomes
class IncomeD:
    def __init__(self):
        self.InList = []
    def set_income(income_List):
        self.InList = income_List
    def add_income(incomeCell):
        self.InList.append(incomeCell)

# Data structure for a Financial Goal
class GoalsCellD:
    def __init__(self, name, amount, date, progress, recurring):
        self.name = name
        self.amount = amount
        self.date = date
        self.progress = progress
        self.recurring = recurring

# Data structure for a users complete set of Financial Goals
class GoalD:
    def __init__(self):
        self.GoalList = []
    def set_income(goal_List):
        self.GoalList = goal_List
    def add_income(goalCell):
        self.GoalList.append(goalCell)


#------------------Functions to Read and Write to Json-----------------------

# Function to write information to Json file

def writeJsonInfo(): # ---- Currently Incomplete ----
    settingState = SettingD(curr = "USD", lan = "eng", pas = "Hello123", confpas = "Hello123")
    stuffs = {"SettingD":vars(settingState)}
    with open("userInformation.json", "w") as f:
        json.dump(stuffs, f, indent=2)

#--------------------------End of Json Functions-----------------------------


# --------------USE OF FLASK FRAMEWORK------------------

# Initialize the Flask Web Application
app = Flask(__name__)

# Home page endpoint
@app.route('/')
@app.route('/home')
def home():
    
    # Render the dashboard HTML resource
    return render_template("dashboard.html")

# GOAL PAGE ENDPOINT
@app.route('/goals', methods=['POST', 'GET'])
def goals():
    # name = formatAPI(readAPI())  # Read from an api
    # Render the goal HTML resource
    return render_template('goal.html')

# EXPENSES PAGE ENDPOINT
@app.route('/expenses', methods=['POST', 'GET'])
def expenses():
    # name = formatAPI(readAPI())  # Read from an api
    # Render the expenses HTML resource
    return render_template('expenses.html')

# INCOME PAGE ENDPOINT
@app.route('/income', methods=['POST', 'GET'])
def income():
    # name = formatAPI(readAPI())  # Read from an api
    # Render the income HTML resource
    return render_template('income.html')

# REPORTS PAGE ENDPOINT
@app.route('/reports', methods=['POST', 'GET'])
def reports():
    # name = formatAPI(readAPI())  # Read from an api
    # Render the reports HTML resource
    return render_template('reports.html')

# SETTINGS PAGE ENDPOINT
@app.route('/settings', methods=['POST', 'GET'])
def settings():
    if (request.method == "POST"):
        # getting input from the setings form
        setList = SettingD.get_settings()
        print(setList)    

    # name = formatAPI(readAPI())  # Read from an api
    # Render the settings HTML resource
    return render_template('settings.html')


if __name__ == "__main__":
    app.run(debug=True)

# -----------------End of test----------------