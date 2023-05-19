import traceback

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
    except Exception:
        return jsonify({
            'connect': traceback.print_exc()
        })

if __name__ == '__main__':
    app.run()
