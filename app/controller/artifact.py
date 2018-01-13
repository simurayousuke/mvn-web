#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template

from ..app import app
from ..models import db, License, Package, Index, Dependency
from sqlalchemy.orm import aliased


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
    rs = rs.all()
    if rs:
        for r in rs:
            results.append(r)
            use_num = use_num + r[5]
        return render_template('artifact.html', results=results, artifact=artifact_id, group=group_id, num=use_num)
    else:
        return render_template('error.html')


@app.route('/<string:group_id>/<string:artifact_id>/<string:version>', methods=['GET'])
def version(group_id, artifact_id, version):
    results = []
    session = db.session
    aliased_license = aliased(License)
    aliased_index = aliased(Index)
    rs = session.query(Index.id, License.license, Package.name, Package.description, Package.home_page, Package.date, aliased_license.license, aliased_index.group_id, aliased_index.artifact_id, aliased_index.version)\
        .join(License, License.index_id == Index.id)\
        .join(Package, Package.index_id == Index.id)\
        .join(Dependency, Dependency.index_id == Index.id)\
        .join(aliased_license, Dependency.dependency_index_id == aliased_license.index_id)\
        .join(aliased_index, Dependency.dependency_index_id == aliased_index.id)\
        .filter(Index.group_id == group_id, Index.artifact_id == artifact_id, Index.version == version)
    rs = rs.all()
    if rs:
        for r in rs:
            results.append(r)
        return render_template('version.html', results=results, artifact=artifact_id, group=group_id, version=version)
    else:
        return render_template('error.html')