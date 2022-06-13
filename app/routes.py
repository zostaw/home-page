from . import app
from flask import render_template, Flask, request, redirect, url_for
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

@app.route("/blog")
def blog():
    return render_template("blog.html")
