from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, \
    login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user



def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string





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
@login_required
def getPlugins(pluginName=None):
    if pluginName == None :
        return render_template('plugins.html',
                           title='Plugins',
                           dico=dico,
                           user=g.user)
    else :
        newdico = dict(dico)
        newdico["currentPlugin"] = pluginName
        return render_template('plugins.html',
                           title='Plugins',
                           dico=newdico,
                           user=g.user)