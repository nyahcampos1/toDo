from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('toDo1.html')

cnx = mysql.connector.connect(user='nyahcampos', password='Welcome123!',
                              host='127.0.0.1',
                              database='toDo')
cnx.close()

app.run(debug = True)