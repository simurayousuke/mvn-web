#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template

from ..app import app
from ..models import db, License, Package, Index, Dependency


@app.route('/<string:group_id>/<string:artifact_id>/', methods=['GET'])
def artifact(group_id, artifact_id):
    results = []
    use_num = 0
    session = db.session
    rs = session.query(Package.index_id, Package.name, Package.description, License.license, Index.version, db.func.count(Index.version).label('use'), Package.date)\
        .join(Index,Index.id == Package.index_id)\
        .join(Dependency, Dependency.dependency_index_id == Index.id)\
        .join(License, License.index_id == Index.id)\
        .filter(Index.group_id == group_id, Index.artifact_id == artifact_id)\
        .group_by(Package.index_id, Package.name, Package.description, License.license, Index.version, Package.date)\
        .order_by(Package.date.desc())
    if rs:
        for r in rs.all():
            results.append(r)
            use_num = use_num + r[5]
        return render_template('artifact.html', results=results, artifact=artifact_id, group=group_id, num=use_num)
    else:
        return 


@app.route('/[artifact]/[version]', methods=['GET'])
def version():
    return render_template('version.html')
