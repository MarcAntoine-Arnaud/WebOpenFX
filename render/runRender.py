#!/usr/bin/python

from flask import Flask, request, jsonify

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
    renderId = 0
    if len(renders) > 0:
        renderId = 1 + int(renders[len(renders)-1]['id'])

    ret = { "id" : renderId, "scene" : request.get_json() }
    renders.append( ret )

    return jsonify(**ret)

@app.route('/render/', methods=['GET'])
def getRenders():
    totalRenders = {"renders": renders}
    return jsonify(**totalRenders)

@app.route('/render/<renderId>', methods=['GET'])
def getRender(renderId):
    return renderId

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)
