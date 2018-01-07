#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from flask import render_template

from ..app import app
from ..models import db, License, Package


@app.route('/', methods=['GET'])
def index():
    session = db.session
    exists_license = session \
        .query(License.license.label('license'), db.func.count(License.index_id).label('num')) \
        .group_by(License.license) \
        .subquery()
    a = session.query(
        db.case(
            [
                (exists_license.c.num >= 30000, exists_license.c.license)
            ],
            else_='Others'
        ).label('license'),
        exists_license.c.num
    ).subquery()
    has_license = session.query(a.c.license, db.func.sum(a.c.num).label('num')).group_by(a.c.license)
    no_license = session.query(Package.index_id.label('index_id')) \
        .except_(session.query(License.index_id)) \
        .subquery()
    no_license_count = session.query(db.literal('None'), db.func.count(no_license.c.index_id))
    result = has_license.union(no_license_count).order_by(db.desc('num'))
    license_info = []
    for l in result.all():
        license_info.append({
            'license': l[0],
            'num': int(l[1])
        })
    st = session \
        .query(db.func.to_char(Package.date, 'YYYY').label('time'), db.func.count(Package.id).label('num')) \
        .filter(Package.date >= '2005-01-01') \
        .group_by('time') \
        .order_by(db.asc('time'))
    statistics_info = []
    for s in st.all():
        statistics_info.append({
            'time': s[0],
            'num': s[1]
        })
    return render_template('index.html', license=json.dumps(license_info), statistics=json.dumps(statistics_info))
