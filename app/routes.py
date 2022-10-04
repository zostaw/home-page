from . import app
from flask import render_template, Flask, request, redirect, url_for, jsonify, json
from flask import send_from_directory
from flask_wtf import FlaskForm
import os
import datetime
import mimetypes
import numpy as np

mimetypes.add_type('image/svg+xml', '.svg')


from .SpacedRepetition import SpacedRepetition
db = SpacedRepetition(7, 5, "learning_words")


@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])

def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

###### projects section - start ######

@app.route("/process_test", methods=['GET', 'POST'])
def process_test():
    print("process_test")
    if request.method == "POST":
        qtc_data = request.get_json()
        print(qtc_data)
        results = {'processed': 'true'}
        return jsonify(results)

@app.route('/sr_get_all_boxes', methods=['POST'])
def sr_get_all_boxes():
    output = request.get_json()

    boxes_list = str(db.ReturnAllBoxes())
    print(boxes_list)
    return jsonify(boxes_list)


@app.route('/sr_get_records', methods=['POST'])
def sr_get_records():
    output = request.get_json()

    records_list = db.ReturnAllRecords()
    print(records_list)
    dict = {}
    dict["name"]=records_list[1]
    dict["question"]=records_list[2]
    dict["answer"]=records_list[3]
    return dict


@app.route("/employee.json")
def employee():
    return "employee.json"

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/spaced_repetition")
def spaced_repetition():
    #SpacedRepetition API
    #import SpacedRepetition from SpacedRepetition
    #a=get_records()


    return render_template("spaced_repetition.html")

###### projects section - start ######

###### blogs section  - start ######
@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/mystory")
def mystory():
    return render_template("blog/mystory.html")

@app.route("/drawing")
def drawing():
    return render_template("blog/drawing.html")

###### blogs section - end ######
