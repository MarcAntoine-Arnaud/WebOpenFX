from flask import Flask # du package flask, importer le module lask
from flask import render_template
from pyTuttle import tuttle

import json



app = Flask(__name__)


#permet d'associer a "/" la methode correspondante


tuttle.core().preload(False)
tuttleCore = tuttle.core()
#pluginCache = tuttle.core().getPluginCache()
#pluginsList = [p.getDescriptor().getLabel() for p in pluginCache.getPlugins()]

#getBinary().getfileName/path() -> savoir d'ou vient le binaire


pluginCache = tuttle.core().getImageEffectPluginCache()

plugins = pluginCache.getPlugins()
allPluginsDatas = []

class PluginData:
    pass

#clipsProperties[]
#paramProperties[]

for plugin in plugins:
    graph = tuttle.Graph()
    node = graph.createNode(plugin.getIdentifier())
    pluginData = PluginData()

    #owner infos
    pluginData.owner = ""

    #descr
    pluginData.identifier = plugin.getIdentifier()
    pluginData.label = node.getLabel()
    pluginData.version = node.getVersionStr()
    pluginData.name = node.getName()
    pluginData.properties = node.getProperties()
    pluginData.description = node.getProperties().getStringProperty("OfxPropPluginDescription");

    #recuperer liste des properties des clips et parametres
    

    #properties // avoir une liste d'objet properties


    #params
    pluginData.nbParams = node.getNbParams()
    #for param in 

    allPluginsDatas.append(pluginData)


for p in allPluginsDatas:
    print(p.identifier)
    print(p.label)
    print(p.version)
    print(p.description)


'''
response = []
for row in z['rows']:
    for key, dict_list in row.iteritems():
        count = dict_list[1]
        year = dict_list[2]
        response.append({'count': count['v'], 'year' : year['v']})

 print json.dumps(response)


pluginsList = [{ "plugins" : [] }]


for plugin in plugins:
    graph = tuttle.Graph()
    node = graph.createNode(plugin.getIdentifier())
    node.getParam()
    pluginsList["plugins"] = { "plugin" : {

                                "identifier" : plugin.getIdentifier(),
                                 "label" : plugin.getDescriptor().getLabel()
                               }
                           }
    plugin.getDescriptor().getDescription()

#pluginsList = [p.getIdentifier() for p in pluginCache.getPlugins()]
#pluginsList = [p.getDescriptor().getLabel() for p in pluginCache.getPlugins()]

 #tuttle.core().getImageEffectPluginCache().getPluginByLabel(

pattern = 'tuttle.'
 '''





#for plugin in tuttleCore.getImageEffectPluginCache():
#
#for plugin_name in pluginsList:
#    match = re.search(pattern, plugin_name)
#    e = match.end()
    #print e
#    print plugin_name[e:]
#    print tuttleCore.getImageEffectPluginCache().getPluginByLabel(plugin_name[e:])


@app.route("/")
def hello():
    
    return "Hello World!"

@app.route('/test/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User TEST %s' % username

@app.route('/test/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/test')
def getPluginList():
    return render_template('index.html', plugins=pluginsDictionnary)



def dico():
  return "starting ..."


#TODO get current plugin

if __name__ == "__main__":
    app.run(debug=True)





