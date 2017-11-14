#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'Xueqian Lu'
from flask import Flask, render_template
from datetime import datetime
from flask import request
from flask_script import Manager
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'secret key'

class NameForm(Form):
    name = StringField('What is your name ?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index_bs.html', user_agent=user_agent, current_time=datetime.utcnow())

@app.route('/reg')
def register():
    form = NameForm()
    return render_template('register.html', form=form)

@app.route('/user/<name>')
def user(name):
    return render_template('user_bs.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
