from flask import Flask # du package flask, importer le module lask
from pyTuttle import tuttle
import logging
import time
import json
import os


app = Flask(__name__)


# TODO analyze types

def getRequest():
    return {
        "nodeName": "tuttle.invert",
        "params":{
            "a": 0,
            "b": 1,
            #"channelGroup": "0",
            "g": 1,
            "gray": 0,
            "r": 0,
        },
        "clips":{
            "output": "images/output/out.jpg",
            "source": "images/input/example.jpg",
        }
    }

#pourquoi sam-do tuttle.invert -h donne moins de parametres avec noms differents ?

def renderImage(ofxPluginPath, request):
    tuttle.core().getPluginCache().addDirectoryToPath(ofxPluginPath)
    pluginCache = tuttle.core().getPluginCache()
    tuttle.core().preload(False)

    g = tuttle.Graph()

    time = 0.0

    reader = g.createNode("tuttle.jpegreader", filename=request["clips"]["source"])
    logging.info('reading '+request["clips"]["source"])
    processNode = g.createNode(request["nodeName"])
    for paramName, paramValue in request["params"].iteritems():
        processNode.getParam(paramName).setValue(paramValue)

    outputImage="images/output/"+"out"+".jpg"
    writer = g.createNode( "tuttle.jpegwriter", filename=outputImage)
    g.connect( [reader, processNode, writer] )

    hashMap = tuttle.NodeHashContainer()
    g.computeGlobalHashAtTime(hashMap, time)
    globalHash = hashMap.getHash(processNode.getName(), time)
    outputImage = "images/output/"+repr(globalHash)+".jpg"


    if os.path.exists(outputImage):
        logging.info(outputImage+" already exists.")
        return

    g.compute( writer )
    logging.info('writing '+outputImage)


def returnImage(ofxPluginPath, request):
    renderImage(ofxPluginPath, request)


if __name__ == "__main__":
    # app.run(debug=True)
    logging.basicConfig(format='tuttle - %(levelname)s - %(asctime)-15s - %(message)s', filename='logs/graph.log', filemode='w', level=logging.DEBUG)
    ofxPluginPath ="/home/juliette/Programmation_compilation/webOpenOFX/TuttleOFX/install/"
    returnImage(ofxPluginPath, getRequest())