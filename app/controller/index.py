#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from flask import render_template

from ..app import app
from ..models import db, License, Package


@app.route('/', methods=['GET'])
def index():
    session = db.session
    exists_license = session.query(License.index_id.label('index_id'), License.license.label('license'))
    no_license = session.query(Package.index_id, db.literal('None')) \
        .except_(session.query(License.index_id, db.literal('None')))
    all_license = exists_license.union(no_license).subquery()
    all_rows = session \
        .query(all_license.c.license, db.func.count(all_license.c.index_id).label('num')) \
        .group_by(all_license.c.license) \
        .subquery()
    data = session.query(
        all_rows.c.num,
        db.case(
            [
                (all_rows.c.num >= 30000, all_rows.c.license)
            ],
            else_='Other'
        ).label('license')
    ).subquery()
    data = session.query(data.c.license, db.func.sum(data.c.num)).group_by(data.c.license)
    license_info = []
    for l in data.all():
        license_info.append({
            'license': l[0],
            'num': int(l[1])
        })
    return render_template('index.html', data=json.dumps(license_info))
