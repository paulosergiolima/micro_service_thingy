from flask import Flask, render_template
import requests

app = Flask(__name__)


def create():
    return 'sex'


def get_names():
    return ["Paulo Sergio", "Erickson"]


@app.route("/")
def index():
    return render_template('index.html', names_list=get_names(), created_name=create())


@app.post('/create/<username>')
def create_name(username):
    return username
