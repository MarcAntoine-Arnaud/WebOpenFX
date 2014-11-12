from flask import Flask
from flask import render_template



app = Flask(__name__)


def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string



# @app.route('/hello/')
# @app.route('/hello/<name>')




dico = {
    # clef:valeur
    "plugins" : [
        {
            "id" : "colorwheel",
            "name" : "Color Wheel",
            "version" : "2.0",
            "author" : "Armand Biteau",
            "parameters" : [
                {
                    "id" : "MinColor",
                    "name" : "Min Color"
                },
                 {
                    "id" : "MaxColor",
                    "name" : "Max Color"
                }

            ]
        },
        {
            "id" : "crop",
            "name" : "Image croper",
            "version" : "3.2",
            "author" : "Hugo Garrido",
            "parameters" : [
                {
                    "id" : "wid",
                    "name" : "Width"
                },
                 {
                    "id" : "hei",
                    "name" : "Height"
                }

            ]
        }
        ,
        {
            "id" : "opacity",
            "name" : "Opacity",
            "version" : "1.2",
            "author" : "Juliette Belin",
            "parameters" : [
                {
                    "id" : "intensity",
                    "name" : "Intensity"
                },
                 {
                    "id" : "imgIn",
                    "name" : "Image In"
                }

            ]
        }
    ]
}





@app.route('/plugins')
@app.route('/plugins/<pluginName>')
def getPlugins(pluginName=None):
    if pluginName == None :
        return render_template('plugins.html', dico=dico)
    else :
        newdico = dict(dico)
        newdico["currentPlugin"] = pluginName
        return render_template('plugins.html', dico=newdico)

if __name__ == "__main__":
    app.run(debug=True)