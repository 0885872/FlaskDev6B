"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, url_for
from flask.templating import render_template
import mysql.connector
from flask import json
from flask import jsonify
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/w1', methods=['GET', 'POST'])
def w1():
    return render_template('w1.html')

@app.route('/ttev1')
def ttev1():
    return render_template('ttev1.html')

@app.route('/answersttev1.json')
def jsoninize():
    a = []
    sql1 = "SELECT answer FROM ttev1;";
    db = mysql.connector.connect(user="root", passwd="usbw", host="vvdsl2.xs4all.nl",database="dev6")
    execute = db.cursor()
    execute.execute(sql1)
    answer = execute.fetchall()
    db.close()
    print(answer)
    collectionString = "answersdata=[{\n"
    first = True;
    for row in answer:

        if (first == False):
            collectionString += ",{\n"
        else:
            first = False;
        collectionString += ("\t\"answer\":\"" + str(row[0]) + "\"}\n")
    collectionString += "]"
    return collectionString

@app.route('/answersttev2.json')
def jsoni():
    sql1 = "SELECT answer FROM ttev2;";
    db = mysql.connector.connect(user="root", passwd="usbw", host="vvdsl2.xs4all.nl",database="dev6")
    execute = db.cursor()
    execute.execute(sql1)
    answer = execute.fetchall()
    db.close()
    print(answer)
    collectionString = "answersdata=[{\n"
    first = True;
    for row in answer:

        if (first == False):
            collectionString += ",{\n"
        else:
            first = False;
        collectionString += ("\t\"answer\":\"" + str(row[0]) + "\"}\n")
    collectionString += "]"
    return collectionString


@app.route('/answersw1.json')
def jsoniz():
    a = []
    sql1 = "SELECT answer FROM w1;";
    db = mysql.connector.connect(user="root", passwd="usbw", host="vvdsl2.xs4all.nl",database="dev6")
    execute = db.cursor()
    execute.execute(sql1)
    answer = execute.fetchall()
    db.close()
    print(answer)
    collectionString = "answersdata=[{\n"
    first = True;
    for row in answer:

        if (first == False):
            collectionString += ",{\n"
        else:
            first = False;
        collectionString += ("\t\"answer\":\"" + str(row[0]) + "\"}\n")
    collectionString += "]"
    return collectionString


@app.route('/answersw2.json')
def jsonize():
    sql1 = "SELECT answer FROM w2;";
    db = mysql.connector.connect(user="root", passwd="usbw", host="vvdsl2.xs4all.nl",database="dev6")
    execute = db.cursor()
    execute.execute(sql1)
    answer = execute.fetchall()
    db.close()
    print(answer)
    collectionString = "answersdata=[{\n"
    first = True;
    for row in answer:

        if (first == False):
            collectionString += ",{\n"
        else:
            first = False;
        collectionString += ("\t\"answer\":\"" + str(row[0]) + "\"}\n")
    collectionString += "]"
    return collectionString


@app.route('/w2', methods=['GET', 'POST'])
def w2():
    return render_template('w2.html')


@app.route('/ttev2', methods=['GET', 'POST'])
def ttev2():
    return render_template('ttev2.html')

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
