from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://192.168.59.101:32061'], methods=['POST', 'GET'])

todos = []

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task = request.get_json()
        todos.append(task['task'])
        return jsonify ({ 'todos' : todos })
    elif request.method == 'GET':
        return jsonify({'todos': todos})
    else:
        return jsonify(error='invalid request')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    