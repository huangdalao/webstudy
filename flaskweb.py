from flask import Flask,jsonify,request,abort,Response
from time import time
from uuid import uuid4
import json

app = Flask(__name__)

class Todo(object):
    def __init__(self,content):

@app.route('/index')
def index():
    return jsonify(msg='hello world')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)