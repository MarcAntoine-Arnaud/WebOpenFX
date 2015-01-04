#!/usr/bin/python

from flask import Flask

app = Flask(__name__, static_folder='', static_url_path='')

version = "0.0.1"

@app.route('/', methods=['GET'])
def index():
    index = "<html><head><title>WebOpenFX - Catalog</title></head><body><h1><center>WebOpenFX - Catalog</center></h1><br/><br/><ul><li>version: " + str(version) + "</li></ul></body>"
    return index


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
