#!/usr/bin/python
import logging
from flask import Flask, jsonify
from pyTuttle import tuttle

app = Flask(__name__, static_folder='', static_url_path='')

version = "0.0.1"

tuttle.core().preload(False)
pluginCache = tuttle.core().getPluginCache()
plugins = pluginCache.getPlugins()

@app.route('/', methods=['GET'])
def index():
  index = "<html><head><title>WebOpenFX - Catalog</title></head><body><h1><center>WebOpenFX - Catalog</center></h1><br/><br/><ul><li>version: " + str(version) + "</li></ul></body>"
  return index

class pointer:
    def __init__(self, p):
        self.p = p

propTypeToPythonType = {
    tuttle.ePropTypeDouble: float,
    tuttle.ePropTypeInt: int,
    tuttle.ePropTypeNone: None,
    tuttle.ePropTypePointer: str,
    tuttle.ePropTypeString: str,
}

def getDictOfProperty(prop):
  pythonType = propTypeToPythonType[prop.getType()]

  return {
   "name": prop.getName(),
   "readOnly": prop.getPluginReadOnly(),
   "type": prop.getType(),
   "modifiedBy": prop.getModifiedBy(),
   "values": [pythonType(v) for v in prop.getStringValue().split(', ')]
  }

def getDictOfProperties(props):
  properties = []
  for p in props:
    properties.append(getDictOfProperty(p))
  return properties

def getPluginProperties(plugin):
  logging.info('Analyzing plugin for ' + plugin.getRawIdentifier())

  pluginProperties = {
    'id': plugin.getIdentifier(),
    'uri': "/plugins/"+ plugin.getIdentifier(),
    'version': {
      'major': plugin.getVersionMajor(),
      'minor': plugin.getVersionMinor()
    }
  }

  try:
    node = tuttle.createNode(plugin.getIdentifier())
  except Exception as e:
    logging.error("Error in node creation: " + str(e))
    return pluginProperties

  # plugin properties
  pluginProperties["properties"] = getDictOfProperties(node.getProperties())

  # list all properties on parameters of the node
  params = []
  for param in node.getParamSet().getParams():
    params.append(getDictOfProperties(param.getProperties()))
  pluginProperties["parameters"] = params

  # list all properties on Clips
  clips = []
  for clip in node.getClipImageSet().getClips():
      clips.append(getDictOfProperties(clip.getProperties()))
  pluginProperties["clips"] = clips

  return pluginProperties

@app.route('/plugins/', methods=['GET'])
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
  # logging.getLogger().setLevel(10)
  app.run(host='0.0.0.0', port=5010, debug=True)
