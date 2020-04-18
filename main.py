# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Flask
from flask import render_template

from services import rootnet

app = Flask(__name__, static_url_path='/static')
app.debug = True

app.register_blueprint(rootnet.app)

@app.route('/')
def root():
    return render_template('index.html')

app.run(debug=True, host='0.0.0.0')