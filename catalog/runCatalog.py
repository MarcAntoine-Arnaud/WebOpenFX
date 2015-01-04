#!/usr/bin/python
import logging
from flask import Flask, jsonify
from pyTuttle import tuttle

app = Flask(__name__, static_folder='', static_url_path='')

version = "0.0.1"

ofxPluginPath = "/home/marco/dev/TuttleOFX/distScons/marco-N150P-N210P-N220P/gcc-4.8/production/plugin/"
tuttle.core().getPluginCache().addDirectoryToPath(ofxPluginPath)
pluginCache = tuttle.core().getPluginCache()
tuttle.core().preload(False)
plugins = pluginCache.getPlugins()

@app.route('/', methods=['GET'])
def index():
  index = "<html><head><title>WebOpenFX - Catalog</title></head><body><h1><center>WebOpenFX - Catalog</center></h1><br/><br/><ul><li>version: " + str(version) + "</li></ul></body>"
  return index

def getPluginProperties(plugin):
  logging.info('Analyzing plugin for ' + plugin.getRawIdentifier())

  pluginProperties = {
    'id': plugin.getIdentifier(),
    'uri': "/plugins/"+ plugin.getIdentifier(),
    'rawIdentifier': plugin.getRawIdentifier(),
    'version': {
      'major': plugin.getVersionMajor(),
      'minor': plugin.getVersionMinor()
    },
    'pluginApi': plugin.getPluginApi(),
    'pluginApiVersion': plugin.getApiVersion()
  }

  return pluginProperties

@app.route('/plugins', methods=['GET'])
def getPlugins():
  pluginsDescription = {'plugins':[], 'total': len(plugins)}
  for plugin in plugins:
    pluginsDescription['plugins'].append(getPluginProperties(plugin))

  return jsonify(**pluginsDescription)

@app.route('/plugins/<string:pluginId>', methods=['GET'])
def getPlugin(pluginId):
  plugin = pluginCache.getPluginById(str(pluginId))
  pluginDescription = getPluginProperties(plugin)
  return jsonify(**pluginDescription)

if __name__ == '__main__':
  logging.getLogger().setLevel(10)
  app.run(host='0.0.0.0', port=5010, debug=True)
