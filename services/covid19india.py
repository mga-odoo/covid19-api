# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Blueprint

from maps import state_code
from tools import fetch_data

API_ENDPOINT = 'https://api.covid19india.org/'

app = Blueprint('covid19india', __name__, template_folder='templates')

@app.route('/covid19india/api/case_by_district', methods=['GET', 'POST'])
def case_by_district():
    json_data = fetch_data(API_ENDPOINT, '/v2/state_district_wise.json')
    #change data structure if you want data in other format
    result = json_data
    return result
