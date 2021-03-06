#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'Xueqian Lu'
from flask import Flask, render_template
from flask import request
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', user_agent=user_agent)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    #app.run(host='0.0.0.0', debug=True)
    manager.run()
