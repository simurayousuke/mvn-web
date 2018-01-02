#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

from .app import app

db = SQLAlchemy(app)


class Dependency(db.Model):
    __tablename__ = 'm2_dependency'
    __table_args__ = (
        db.Index('m2_dependency_group_id_artifact_id_version_index', 'group_id', 'artifact_id', 'version'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    index_id = db.Column(db.Integer, nullable=False, index=True)
    dependency_index_id = db.Column(db.ForeignKey('m2_index.id'), index=True)
    optional = db.Column(db.Boolean, nullable=False, index=True, server_default=db.FetchedValue())
    scope = db.Column(db.Text, nullable=False, server_default=db.FetchedValue())
    group_id = db.Column(db.Text)
    artifact_id = db.Column(db.Text)
    version = db.Column(db.Text)

    dependency_index = db.relationship('Index', primaryjoin='Dependency.dependency_index_id == Index.id',
                                       backref='m2_dependencies')


class Index(db.Model):
    __tablename__ = 'm2_index'
    __table_args__ = (
        db.Index('m2_index_group_id_artifact_id_index', 'group_id', 'artifact_id'),
    )

    id = db.Column(db.Integer, unique=True, server_default=db.FetchedValue())
    group_id = db.Column(db.Text, primary_key=True, nullable=False, index=True)
    artifact_id = db.Column(db.Text, primary_key=True, nullable=False)
    version = db.Column(db.Text, primary_key=True, nullable=False)


class License(db.Model):
    __tablename__ = 'm2_license'
    __table_args__ = (
        db.Index('m2_license_index_id_license_uindex', 'index_id', 'license'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    index_id = db.Column(db.ForeignKey('m2_index.id'), nullable=False, index=True)
    license = db.Column(db.Text, nullable=False, index=True)

    index = db.relationship('Index', primaryjoin='License.index_id == Index.id', backref='m2_licenses')


class Package(db.Model):
    __tablename__ = 'm2_package'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    index_id = db.Column(db.ForeignKey('m2_index.id'), nullable=False, unique=True)
    name = db.Column(db.Text, index=True)
    description = db.Column(db.Text)
    home_page = db.Column(db.Text, index=True)
    organization = db.Column(db.Text, index=True)
    date = db.Column(db.Date, index=True)

    index = db.relationship('Index', primaryjoin='Package.index_id == Index.id', backref='m2_packages')
