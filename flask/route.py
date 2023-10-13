from flask import render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

def handle_list(client, shoppingList, application):
    try:
        client.admin.command('ismaster')
    except:
        return "Server not available"
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        shoppingList.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('list'))
    all_shoppingList = shoppingList.find()
    return render_template('index.html', shoppingList=all_shoppingList)

def handle_delete(client, shoppingList, application, id):
    shoppingList.delete_one({"_id": ObjectId(id)})
    print(application.url_map)
    return redirect(url_for('list'))