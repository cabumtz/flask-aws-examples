# -*- coding: utf-8 -*-

"""
    Application
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

from apps.main import app
from apps.s3 import app as s3_app
from apps.site import app as site_app


######################################################
###
### Apps
###
######################################################
app.register_blueprint(site_app)
app.register_blueprint(s3_app, url_prefix='/s3')
