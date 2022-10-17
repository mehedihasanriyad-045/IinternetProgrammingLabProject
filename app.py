from crypt import methods
from pickle import FALSE
import re
from flask import Flask, render_template, jsonify, request
from DatabaseMysql import DatabaseMysql
from DatabaseSqlite import DatabaseSqlite
from database_configure import getDatabase
import json

app = Flask(__name__)

@app.route('/api/authentication', methods=['POST', 'GET'])
def getUserData():
    config = {
    "sqlite": {
        "filename": "sqlite.db"
    }, 
    "mysql": {
        "host": "localhost",
        "user": "root",
        "password": "riyad",
        "db": "docter_pad"
    },
    "databaseToUse" : "mysql" 
    } 
    # initiats a database
    # function returns a database depending on the config specification
    # sqlite / mysql

    database = getDatabase(config, debug=True)

    # Connects and executes queries needed
    database.connect()

    output = request.get_json();
    if len(output.keys()) < 2:
        return {"Status" : "BAD response"}

    email = output['email']
    password = output['password']

    query = dict();

    query["table"] = "authentication"
    query["all"] = False
    columns = []
    columns.append("email");
    columns.append("user_role");
    columns.append("user_id")

    query["columns"] =  columns

    whereDict = {}

    whereDict["column"] =  "email"
    whereDict["operator"] =  "="
    whereDict["value"] = email


    whereDict1 = {}

    whereDict1["column"] = "user_password"
    whereDict1["operator"] = "="
    whereDict1["value"] = password

    whereList = []
    whereList.append(whereDict)
    whereList.append(whereDict1)

    query["where"] =  whereList


    print(query)


    query_str = '{"table": "authentication", "all": true, "columns": ["email", "user_password", "user_role"], "where": [{"column": "email","operator": "=","value": "mehedi.24csedu.045@gmail.com"}]}'

    querys = json.loads(query_str)
    print(type(querys))
    res = database.select(query)
    response = {}
    if(len(res) > 0):
        response["email"] = res[0][0]
        response["user_role"] = res[0][1]
        response["user_id"] = res[0][2]
        return response;
    else:
        return {"Status" : "Not valid"}
   



@app.route('/')
def home():
   return render_template('home.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True) 