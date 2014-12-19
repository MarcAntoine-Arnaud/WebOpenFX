import logging
from pyTuttle import tuttle
import json

class pointer:
    def __init__(self, p):
        self.p = p


propTypeToPythonType = {
    tuttle.ePropTypeDouble: float,
    tuttle.ePropTypeInt: int,
    tuttle.ePropTypeNone: None,
    tuttle.ePropTypePointer: pointer,
    tuttle.ePropTypeString: str,
}



# TODO tester logs
# export OFX_PLUGIN_PATH=$tuttle_root/OFX

def propertyToJson(prop):
    pythonType = propTypeToPythonType[prop.getType()]

    return {
     "name": prop.getName(),
     "readOnly": prop.getPluginReadOnly(),
     "type": prop.getType(),
     "modifiedBy": prop.getModifiedBy(),
     "values": [pythonType(v) for v in prop.getStringValue().split(', ')],
    }

def propertiesToJson(props):
    properties = []
    for p in props:
        properties.append(propertyToJson(p))
    return properties

def getPluginProperties(identifier):

    logging.info('Analyzing plugin for '+identifier)

    try:
        node = tuttle.createNode(identifier)
    #fix me
    except Exception as e:
        logging.info("Error in node creation: " + str(e))
        return {}
    pluginData = {}

    # Node pluginData
    pluginData["node"] = propertiesToJson(node.getProperties())

    # Properties per Parameter
    params = []
    for param in node.getParamSet().getParams():
        params.append(propertiesToJson(param.getProperties()))
    pluginData["params"] = params

    # Properties per Clip
    clips = []
    for clip in node.getClipImageSet().getClips():
        clips.append(propertiesToJson(clip.getProperties()))
    pluginData["clips"] = clips

    return pluginData

def getPluginsAllProperties(ofxPluginPath):
    ''' 
        get all plugins properties
    '''
    tuttle.core().getPluginCache().addDirectoryToPath(ofxPluginPath)

    pluginCache = tuttle.core().getPluginCache()

    tuttle.core().preload(False)
    plugins = pluginCache.getPlugins()
    allPluginsDatas = []

    for plugin in plugins:
        allPluginsDatas.append(getPluginProperties(plugin.getIdentifier()))
    
    return allPluginsDatas



#for plugin in tuttleCore.getImageEffectPluginCache():
#
#for plugin_name in pluginsList:
#    match = re.search(pattern, plugin_name)
#    e = match.end()
    #print e
#    print plugin_name[e:]
#    print tuttleCore.getImageEffectPluginCache().getPluginByLabel(plugin_name[e:])



#TODO get current plugin

if __name__ == "__main__":
    # app.run(debug=True)

    logging.basicConfig(format='tuttle - %(levelname)s - %(asctime)-15s - %(message)s', filename='console.log', filemode='w', level=logging.DEBUG)


    pluginsAllProperties = getPluginsAllProperties("/home/juliette/Programmation_compilation/webOpenOFX/TuttleOFX/install/")
    print pluginsAllProperties


