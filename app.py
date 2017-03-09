#!flask/bin/python
from flask import Flask, jsonify, render_template
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from flaskext.mysql import MySQL
import requests, json

app = Flask(__name__)

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'cep'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/cep')
def showMain():
    return render_template('index.html')

@app.route('/cep', methods=['POST'])
def cep():
    _cep = request.form['cep']
    r = requests.get('http://api.postmon.com.br/v1/cep/' + _cep)
    return app.response_class(r.content, content_type='application/json')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
