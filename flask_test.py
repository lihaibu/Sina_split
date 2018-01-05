# coding=utf-8

from flask import Flask, render_template
from xinlang_split import  mongo_op

app = Flask(__name__)

mongo_util = mongo_op.MongoUtil()

@app.route('/')
def home():
    return "hello world"

@app.route('/data')
def data():
    datalist = mongo_util.get_data_list()
    return render_template('about.html',data_list = datalist)

if __name__ == '__main__':
    app.run()