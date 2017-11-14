#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'Xueqian Lu'
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask import request
from flask.ext.script import Manager
from flask.ext.moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index_bs.html', user_agent=user_agent, current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user_bs.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
