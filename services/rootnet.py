# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Blueprint

from maps import state_code
from tools import fetch_data

app = Blueprint('rootnet', __name__, template_folder='templates')

API_ENDPOINT = 'https://api.rootnet.in/covid19-in'

@app.route('/rootnet/api/latest/stats', methods=['GET', 'POST'])
def statewise():
    """Make a request to https://api.rootnet.in/covid19-in/stats/latest

    Returns:
    {
        "Andaman and Nicobar Islands": {
            "confirmedCasesForeign": 0,
            "confirmedCasesIndian": 12,
            "deaths": 0,
            "discharged": 11,
            "loc": "Andaman and Nicobar Islands",
            "totalConfirmed": 12
        },
    }
    """

    json_data = fetch_data(API_ENDPOINT, '/stats/latest')
    result = {value:key for key, value in state_code.items()}
    for item in json_data.get('data', {}).get('regional', []):
        result[item.get('loc')] = item

    return result

@app.route('/rootnet/api/latest/stats/history', methods=['GET', 'POST'])
def statewise_history():
    """Make a request to https://api.rootnet.in/covid19-in/stats/history

    Returns:
    """

    json_data = fetch_data(API_ENDPOINT, '/stats/history')
    result = json_data
    return json_data
