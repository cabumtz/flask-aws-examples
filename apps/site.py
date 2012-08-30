# -*- coding: utf-8 -*-

"""
    Site app
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import os
from flask import Blueprint, render_template, request


######################################################
###
### App
###
######################################################

app = Blueprint('site', __name__)


######################################################
###
### Routes
###
######################################################

@app.route('/')
def index():
    return render_template('site/index.html')
