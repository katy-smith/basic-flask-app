#!/usr/bin/env python
import os
import webbrowser
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from route import handle_list, handle_delete

application = Flask(__name__, template_folder='templates')

uri = os.environ.get('CONNECTION_STRING')


if os.environ.get('DOCKER_ENV') == 'true':
    client = MongoClient(uri, server_api=ServerApi('1'))
else: 
    client = MongoClient(uri, server_api=ServerApi('1'))
    
db = client.flaskdb
shoppingList = db.shoppingList

@application.route('/', methods=('GET', 'POST'))
def list():
    return handle_list(client, shoppingList, application)

@application.post('/<id>/delete/')
def delete(id):
    return handle_delete(client, shoppingList, application, id)

if __name__ == "__main__":
    url='http://localhost:8080'
    webbrowser.open(url) 
    application.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 8080), debug=True)
