#!/usr/bin/python
from flask import Flask, jsonify
from pyTuttle import tuttle
from ofxPlugins import analyze
import ConfigParser, requests, json


app = Flask(__name__, static_folder='', static_url_path='')

configParser =  ConfigParser.RawConfigParser()
configParser.read('configuration.conf')

version = "0.0.1"

@app.route('/plugins', methods=['GET'])
def getPlugins():
    pluginsDescription = {'plugins':[], 'total': 0}
    for plugin in plugins:
        pluginsDescription['plugins'].append(analyze.getPluginProperties(plugin))

    headers = {
        'content-type': 'application/json'
    }

    return jsonify(**pluginsDescription)


@app.route('/plugins/<string:pluginId>', methods=['GET'])
def getPlugin(pluginId):
    plugin = pluginCache.getPluginById(str(pluginId))
    pluginDescription = analyze.getPluginProperties(plugin)
    return jsonify(**pluginDescription)

