# scons: pluginCheckerboard pluginBlur pluginPng

from flask import Flask # du package flask, importer le module lask
from flask import render_template
from pyTuttle import tuttle


app = Flask(__name__)
tuttle.core().preload(False)
tuttleCore = tuttle.core()




g = tuttle.Graph()
read = g.createNode( "tuttle.jpegreader",filename="images_test/input/crabe.jpg")
blur = g.createNode( "tuttle.blur", size=[9.0, 0.15], border="Black" )
write = g.createNode( "tuttle.jpegwriter", filename="images_test/output/crabe1.jpg" )
g.connect( [read, blur, write] )
g.compute( write )

@app.route("/")
def hello():
    
    return "test"

#TODO get current plugin

if __name__ == "__main__":
    app.run(debug=True)





