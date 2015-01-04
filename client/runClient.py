#!/usr/bin/python
import requests
from flask import Flask, render_template

app = Flask(__name__, static_folder='', static_url_path='')

version = "0.0.1"
catalogRootUri = "http://localhost:5010"
renderRootUri = "http://localhost:5011"

globalParameters = {
  "WOFX_TITLE": "WebOpenFX",
  "WOFX_VERSION": version,
  "WOFX_STANDARD_LINK": "http://openeffects.org/",
  "WOFX_PLUGINS_LINK": "/plugins"
}

@app.route('/', methods=['GET'])
def index():
  parameters = dict(globalParameters)
  return render_template('index.html', data=parameters)

@app.route('/plugins/', methods=['GET'])
def plugins():
  parameters = dict(globalParameters)
  plugins = requests.get(catalogRootUri+"/plugins")
  parameters['WOFX_PLUGINS'] = plugins.json()
  return render_template('plugins.html', data=parameters)

@app.route('/plugins/<string:pluginId>', methods=['GET'])
def plugin(pluginId):
  parameters = dict(globalParameters)
  plugin = requests.get(catalogRootUri+"/plugins/"+pluginId)
  parameters['WOFX_PLUGIN'] = plugin.json()
  return render_template('plugin.html', data=parameters)

@app.route('/resource/<path:path>', methods=['GET'])
def resource(path):
  return app.send_static_file('resources/' + path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
