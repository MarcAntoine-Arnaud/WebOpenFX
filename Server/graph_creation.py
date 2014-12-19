# scons: pluginCheckerboard pluginBlur pluginPng

from flask import Flask # du package flask, importer le module lask
from flask import render_template
from pyTuttle import tuttle


app = Flask(__name__)

# TODO analyze types
# hash https://github.com/tuttleofx/TuttleOFX/blob/e71af98bdaa75f09c6d7830560af84a645ff0710/libraries/tuttle/pyTest/testGlobalHash.py

nodeName = "tuttle.blur"
paramArgs = {
	size: [9.0, 0.15]
	border: "Black"
}


def plop():
	tuttle.core().preload(False)
	tuttleCore = tuttle.core()

	g = tuttle.Graph()
	read = g.createNode( "tuttle.jpegreader",filename="images_test/input/crabe.jpg")

	processNode = g.createNode( nodeName )
	for paramName, paramValue in paramArgs.iteritems():
		processNode.getParam(paramName).setValue(paramValue)


	# globalHash = processNode..... hasher le graphe de noeuds
	globalHash = "..."
	outputImage = "images_test/output/"+globalHash+".jpg"

	if os.apth.exists(outputImage);
		return outputImage

	write = g.createNode( "tuttle.jpegwriter", filename=outputFile )
	g.connect( [read, blur, write] )
	g.compute( write )

	return outputImage


@app.route("/")
def hello():
    
    return "test"

#TODO get current plugin

if __name__ == "__main__":
    app.run(debug=True)





