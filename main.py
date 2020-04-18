# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Flask
from flask import render_template

from services import rootnet
from services import covid19india

app = Flask(__name__, static_url_path='/static')

app.register_blueprint(rootnet.app)
app.register_blueprint(covid19india.app)

@app.route('/')
def root():
    return render_template('index.html')

app.run(debug=True, host='0.0.0.0')
