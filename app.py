
# ./app.py

from flask import Flask, render_template, request, jsonify
import pusher
import json

# create flask app
app = Flask(__name__)

# configure pusher object
pusher_client = pusher.Pusher(
  app_id='708261',
  key='a3dec96044e29552785b',
  secret='dde50ef9998c2821c7a0',
  cluster='eu',
  ssl=True
)

# index route, shows index.html view
@app.route('/')
def index():
  return render_template('index.html')

# endpoint for storing todo item
@app.route('/add-todo', methods = ['POST'])
def addTodo():
  data = json.loads(request.data.decode('utf-8')) # load JSON data from request
  pusher_client.trigger('todo', 'item-added', data) # trigger `item-added` event on `todo` channel
  return jsonify(data)

# endpoint for deleting todo item
@app.route('/remove-todo/<item_id>')
def removeTodo(item_id):
  data = {'id': item_id }
  pusher_client.trigger('todo', 'item-removed', data)
  return jsonify(data)

# endpoint for updating todo item
@app.route('/update-todo/<item_id>', methods = ['POST'])
def updateTodo(item_id):
  data = {
    'id': item_id,
    'completed': json.loads(request.data).get('completed', 0)
  }
  pusher_client.trigger('todo', 'item-updated', data)
  return jsonify(data)

# run Flask app in debug mode
# app.run(debug=True)
