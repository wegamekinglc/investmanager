# -*- coding: utf-8 -*-
u"""
Created on 2018-12-11

@author: cheng.li
"""

import datetime as dt
from dateutil.relativedelta import relativedelta
from flask import Flask
from flask import jsonify
from flaskapp.macro import fetch_data
app = Flask(__name__)

TIME_RANGE = 3


@app.route("/<code>", methods=['GET'])
def series_data(code):
    end_date = dt.datetime(2018, 12, 11)
    start_date = end_date - relativedelta(years=3)
    data = fetch_data(code,
                      start_date.strftime('%Y-%m-%d'),
                      end_date.strftime('%Y-%m-%d'),
                      freq='M')
    return jsonify(data.to_dict())
