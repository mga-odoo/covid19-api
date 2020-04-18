# -*- coding: utf-8 -*-
#!/usr/bin/env python

import json
from urllib.request import urlopen

def fetch_data(api=API_ENDPOINT, url='/api/latest/stats'):
    """method takes input and fetch data from data source and return json data

    @api: api endpoint
    @url: api url to access the data
    """

    URL = "%s%s" % (api, url)
    raw_data = urlopen(URL).read()
    json_data = json.loads(raw_data)
    return json_data
