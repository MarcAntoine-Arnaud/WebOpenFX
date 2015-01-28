#!/usr/bin/python
from flask import Flask
app = Flask(__name__, static_folder='', static_url_path='')

from server import analyzePlugin
from server import analyzer
from server import plugin

import ConfigParser

configParser =  ConfigParser.RawConfigParser()
configParser.read('server/configuration.conf')

app.run(host=configParser.get("APP_ANALYZER", "host"), port=configParser.getint("APP_ANALYZER", "port"), debug=True)
