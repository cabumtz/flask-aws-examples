# -*- coding: utf-8 -*-

"""
    Site app
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import os
from flask import Blueprint, render_template, request
from flask import url_for, redirect
from apps.main import app as main_app
from modules.utils import allowed_file, get_path
from werkzeug import secure_filename
from boto.s3.connection import S3Connection
from boto.s3.key import Key


######################################################
###
### App and connections
###
######################################################

app = Blueprint('s3', __name__)
conn = S3Connection(main_app.config['AWS_ACCESS_KEY'], main_app.config['AWS_SECRET_KEY'])


######################################################
###
### Routes
###
######################################################

@app.route('/')
def index():
    buckets = conn.get_all_buckets()
    names = [bucket.name for bucket in buckets] 
    for name in names:
        print name
    return render_template('s3/index.html', names=names)


@app.route('/view/bucket/<name>/')
def view_bucket(name):
    bucket = conn.lookup(name)
    files = [file.name for file in bucket] 
    return render_template('s3/bucket.html', files=files, bucket=name)


@app.route('/create/bucket/', methods=['POST'])
def create_bucket():
    if request.method == 'POST':
        bucket = request.form['name']
        conn.create_bucket(bucket)
    return redirect('/s3/')


@app.route('/delete/bucket/<name>/')
def delete_bucket(name):
    conn.delete_bucket(name)
    return redirect('/s3/')


@app.route('/upload/object/<bucket>/', methods=['GET', 'POST'])
def upload_object(bucket):
     
    UPLOAD_FOLDER = main_app.config['UPLOAD_FOLDER']
    ALLOWED_EXTENSIONS = main_app.config['ALLOWED_EXTENSIONS']
    
    if request.method == 'POST':
        file = request.files['file']

        if file and allowed_file(file.filename, ALLOWED_EXTENSIONS):
            filename = secure_filename(file.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(path)
            b = conn.get_bucket(bucket)
            s3_obj = Key(b)
            s3_obj.key = file.filename
            s3_obj.set_contents_from_filename(get_path(path))
            s3_obj.set_acl('public-read')
            os.remove(get_path(path))

    return redirect('/s3/view/bucket/%s/' % bucket)


