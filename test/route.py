#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'Xueqian Lu'
from flask import Flask, render_template,request, session, redirect, url_for, flash
from datetime import datetime
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

@app.route('/', methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        oldname = session.get('name')
        if oldname is not None and oldname != form.name.data:
            flash('looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('register.html', form=form,name=session.get('name'))

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
