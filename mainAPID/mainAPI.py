from flask import Flask, request, render_template, flash, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
#from flask_restful import Resource, Api
#from sqlalchemy import create_engine
#from json import dumps
#from flask.ext.jsonpify import jsonify
import time
import psycopg2

DBUSER = 'root'
DBPASS = 'toor'
DBHOST = 'db'
DBPORT = '5432'
DBNAME = 'credsDB'

#intilazing the app
app = Flask(__name__)

#connecting to Database
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)

#To turn off the Flask-SQLAlchemy event system (and disable the warning)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#for session usage + encryption
app.secret_key = DBPASS


db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(db.String(80), unique=True)
    pw_hash = db.Column(db.String(80))
    token = db.Column(db.String(256))

    def __init__(self, username, pw_hash, token):
        self.username = username
        self.pw_hash = pw_hash
        self.token = token

def database_initialization_sequence():
    db.create_all()
    tuser = User('hunter2','VerySecurePassword!','The Token')
    db.session.add(tuser)
    db.session.rollback()
    db.session.commit()

@app.route('/')
def index():
    return "Hello, this is mainAPI"



def main():
    dbstatus = False
    while dbstatus == False:
        try:
            db.create_all()
        except:
            time.sleep(2)
        else:
            dbstatus = True
    database_initialization_sequence()
    app.run(debug=True, host="0.0.0.0", port=1800)


if __name__ == '__main__':

    main()





