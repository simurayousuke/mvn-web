#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from flask import render_template

from ..app import app
from ..models import db, License


@app.route('/', methods=['GET'])
def index():
    # data = db.session.execute('SELECT * FROM m2_dependency WHERE id > :id1 AND id < :id2', {'id1': 10, 'id2': 20})
    data = db.session.query(License.license, db.func.count('*').label('num')).group_by(License.license).all()
    license_info = []
    for l in data:
        license_info.append({
            'license': l[0],
            'num': l[1]
        })
    return render_template('index.html', data=json.dumps(license_info))
