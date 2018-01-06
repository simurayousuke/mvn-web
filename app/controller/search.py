#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template

from ..app import app


@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html')
