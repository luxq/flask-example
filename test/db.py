#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'xueqian Lu'
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

