from flask import Flask
from flask import request
import psycopg2

conn = psycopg2.connect("dbname=names user=postgres password=postgres")
cur = conn.cursor()
app = Flask(__name__)


@app.get("/name")
def get_name():
    _name = request.form['name']
    cur.execute("SELECT * FROM names")
    return cur.fetchall()


@app.post("/name")
def create_name():
    name = request.form['name']
    cur.execute(f"INSERT INTO names(username) VALUES ('{name}')")
    return 'Hi'
