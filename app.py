from flask import Flask, json, jsonify
from dtb import db

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/testapi')
def testapi():
    return jsonify({
        'message': 'Hello World!'
    })

@app.route('/testdtb')
def testdtb():
    try:
        db.connect()
        return jsonify({
            'connect': True
        })
    except:
        return jsonify({
            'connect': False
        })

if __name__ == '__main__':
    app.run()
