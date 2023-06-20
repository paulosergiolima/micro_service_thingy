from flask import Flask, render_template
import requests
import json
app = Flask(__name__)


def create():
    return 'sex'


def get_names():
    r = requests.get('http://s_database:3030/name')
    response = []
    for i in r.json():
        for x in i:
            response.append(x)
    return response


@app.route("/")
def index():
    return render_template('index.html', names_list=get_names(), created_name=create())


@app.post('/create/<username>')
def create_name(username):
    r = requests.post(f'http://s_database:3030/name/{username}')
    return "Ok"
