# -*- coding: utf-8 -*-

"""
    Utils
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import os
import os.path
import sys


######################################################
###
### Functions
###
######################################################

def get_path(path=''):
    """
    Get path for application files
    """
    dirname = os.path.dirname(sys.argv[0])
    return os.path.abspath(dirname) + '/' + path


def get_config():
    """
    Get config profile 
    Defaul is production if development profile not present
    """
    cfg = get_path('/settings/development.cfg')
    if os.path.isfile(cfg):
        print " * Development profile"
        return cfg 
    else:
        print " * Production profile"
        return get_path('/settings/production.cfg')


def allowed_file(filename, ALLOWED_EXTENSIONS):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

