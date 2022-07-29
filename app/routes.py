from . import app
from flask import render_template, Flask, request, redirect, url_for
from flask import send_from_directory
from flask_wtf import FlaskForm
import os
import datetime
import mimetypes


mimetypes.add_type('image/svg+xml', '.svg')


@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])

def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

###### projects section - start ######
@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/spaced_repetition")
def spaced_repetition():
    #SpacedRepetition API
    #import SpacedRepetition from SpacedRepetition

    return render_template("spaced_repetition.html")

###### projects section - start ######

###### blogs section  - start ######
@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/mystory")
def mystory():
    return render_template("blog/mystory.html")

###### blogs section - end ######
