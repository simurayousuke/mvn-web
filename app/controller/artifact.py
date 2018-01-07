#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template

from ..app import app


@app.route('/artifact', methods=['GET'])
def artifact():
    return render_template('artifact.html')
