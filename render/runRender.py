#!/usr/bin/python

import os
import tempfile
from flask import Flask, request, jsonify
import renderScene

currentAppDir = os.path.dirname(__file__)
tmpRenderingPath = os.path.join(currentAppDir, "tmp")
if not os.path.exists(tmpRenderingPath):
  os.mkdir(tmpRenderingPath)

app = Flask(__name__, static_folder='', static_url_path='')

version = "0.0.1"
renders = []


@app.route('/', methods=['GET'])
def index():
    index = "<html><head><title>WebOpenFX - Render</title></head><body><h1><center>WebOpenFX - Render</center></h1><br/><br/><ul><li>version: " + str(version) + "</li></ul></body>"
    return index

@app.route('/render/', methods=['POST'])
def newRender():
    # print request.form
    # print request.args
    # print request.data
    project = request.get_json()
    user = 'marco'
    tmpFile = tempfile.mkstemp(prefix='tuttle_', suffix="_"+user+".jpg", dir=tmpRenderingPath)
    renderId = 0
    if len(renders) > 0:
        renderId = 1 + int(renders[len(renders)-1]['id'])

    ret = {
      "id" : renderId,
      "scene" : project,
      "resources": [
        "/render/"+str(renderId)+"/resources/"+os.path.basename(tmpFile[1])
      ]}
    renders.append( ret )

    r = renderScene.RenderScence()
    r.setProject(project, outputFilename=tmpFile[1])
    r.render()

    return jsonify(**ret)

@app.route('/render/', methods=['GET'])
def getRenders():
    totalRenders = {"renders": renders}
    return jsonify(**totalRenders)

@app.route('/render/<int:renderId>', methods=['GET'])
def getRender(renderId):
    return renderId

@app.route('/render/<int:renderId>/resources/', methods=['GET'])
def resources(renderId):
    resources = { "resources": []}
    return jsonify(**resources)
  
@app.route('/render/<int:renderId>/resources/<resourceId>', methods=['GET'])
def resource(renderId, resourceId):
  return app.send_static_file('tmp/' + resourceId)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)
