#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
import requests, json

app = Flask(__name__)

@app.route('/cepws/api/v1.0/tasks/<string:task_id>', methods=['GET'])
def get_task(task_id):
    r = requests.get('http://api.postmon.com.br/v1/cep/' + task_id)
    return app.response_class(r.content, content_type='application/json')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
