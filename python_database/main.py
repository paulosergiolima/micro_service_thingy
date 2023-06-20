from flask import Flask
from flask import request
import psycopg2

conn = psycopg2.connect("host=mydb dbname=names user=postgres password=postgres")
cur = conn.cursor()
app = Flask(__name__)

cur.execute("CREATE TABLE names (name VARCHAR(50) );")
conn.commit()

@app.get("/name")
def get_name():
    cur.execute("SELECT * FROM names")
    conn.commit()
    result = cur.fetchall()
    cool_list = []
    print(result)
    for i in result:
        for x in i:
            print(x)
            cool_list.append(x)
    print(cool_list)
    
    return result


@app.post("/name/<name>")
def create_name(name):
    cur.execute(f"INSERT INTO names(name) VALUES ('{name}')")
    conn.commit()
    return 'Hi'
if __name__ == '__main__':
    print("girl")
    app.run(host='0.0.0.0' ,debug=False, port=3030)