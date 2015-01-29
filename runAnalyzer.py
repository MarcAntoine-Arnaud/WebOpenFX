#!/usr/bin/python

import analyser

import ConfigParser

configParser =  ConfigParser.RawConfigParser()
configParser.read('configuration.conf')

analyser.app.run(host=configParser.get("APP_ANALYZER", "host"), port=configParser.getint("APP_ANALYZER", "port"), debug=True)
