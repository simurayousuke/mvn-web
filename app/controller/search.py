#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template

from ..app import app
from ..models import db, License, Package, Index, Dependency


@app.route('/search/<string:key>', methods=['GET'])
def search(key):
    results = []
    session = db.session
    rs = session.query(Index.id, Index.group_id, Index.artifact_id, Package.name, Package.description, License.license, db.func.count('*').label('num'))\
        .join(Package, Package.index_id == Index.id)\
        .join(License, License.index_id == Index.id)\
        .join(Dependency, Dependency.dependency_index_id == Index.id)\
        .filter(Index.artifact_id.like('%'+ key + '%'))\
        .group_by(Index.id, Index.group_id, Index.artifact_id, Package.name, Package.description, License.license)\
        .order_by(db.desc('num'))
    rs = rs.all()
    for r in rs:
        results.append(r)
    return render_template('search.html', results=results)
