import json
from urllib.request import urlopen

from flask import Flask
from flask import render_template

from maps import state_code

app = Flask(__name__, static_url_path='/static')

API_ENDPOINT = 'https://api.rootnet.in/covid19-in'

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/api/latest/stats', methods=['GET', 'POST'])
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

    URL = "%s/stats/latest" % (API_ENDPOINT)
    raw_data = urlopen(URL).read()
    json_data = json.loads(raw_data)

    result = {value:key for key, value in state_code.items()}

    for item in json_data.get('data', {}).get('regional', []):
        result[item.get('loc')] = item

    return result

@app.route('/api/latest/stats/history', methods=['GET', 'POST'])
def statewise_history():
    """Make a request to https://api.rootnet.in/covid19-in/stats/history

    Returns:
    """

    json_data = json.loads("{}")
    result = json_data
    return json_data


app.run(debug=True, host='0.0.0.0')
