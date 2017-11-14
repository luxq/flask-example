#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'Xueqian Lu'
from flask import Flask
from flask import request
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    response = '<p>Your browser is %s</p>' % user_agent 
    response += '<h1>Hello Flask!</h1>'
    return response

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s!</h1>' % name

if __name__ == '__main__':
    #app.run(host='0.0.0.0', debug=True)
    manager.run()
