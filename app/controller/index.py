#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template

from ..app import app
from ..models import db


@app.route('/', methods=['GET'])
def index():
    data = db.session.execute('SELECT * FROM m2_dependency WHERE id > :id1 AND id < :id2', {'id1': 10, 'id2': 20})
    return render_template('index.html', data=data)
