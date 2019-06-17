from flask import Flask, request
#from flask_restful import Resource, Api
#from sqlalchemy import create_engine
#from json import dumps
#from flask.ext.jsonpify import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, this is client World!"



def main():
    app.run(debug=True, host="0.0.0.0", port=5000)


if __name__ == '__main__':
    main()


