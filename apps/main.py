# -*- coding: utf-8 -*-

"""
    Main Flask App
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

from flask import Flask
from modules.utils import get_config


######################################################
###
### Setup Main App
###
######################################################

## Get cfg path
cfg = get_config()

## Creating main app
app = Flask(__name__)
app.config.from_pyfile(cfg, silent=True)
config = app.config
