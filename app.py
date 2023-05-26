from datetime import date

from flask import Flask, jsonify, request
from dtb import *

app = Flask(__name__)


def default(obj):
    if isinstance(obj, date):
        return obj.strftime('%d-%m-%Y')
    raise TypeError(f'Object of type {type(obj)} is not JSON serializable')


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
            'connect': False
        })

@app.route('/check_card', methods=['GET'])
#check thẻ đã được cắm vào hay chưa
#deploy chưa có thẻ nên làm tạm
def check_card():
    try:
        return jsonify({
            'status': 'OK',
            'data': select_user(1)
        })
    except Exception as e:
        return jsonify({
            'status': 'failed to check',
            'error': e.__str__()
        })

@app.route('/create_card', methods=['POST'])
# tạo thẻ
def create_card():
    try:
        data = request.get_json()
        name = data.get('Name')
        cmnd = data.get('CMND')
        gender = data.get('Gender')
        picture = data.get('Picture')
        dob = data.get('DoB')
        exp_date_ticket = data.get('Exp_date_ticket')
        balance = data.get('Balance')
        exp_date_card = data.get('Exp_date_card')
        types_of_ticket = data.get('Types_of_ticket')
        add_user(name, cmnd, gender, picture, dob, exp_date_ticket, balance, exp_date_card, types_of_ticket)
        return jsonify({
            'status': 'OK'
        })
    except Exception as e:
        return jsonify({
            'status': 'failed to create',
            'error': e.__str__()
        })


@app.route('/edit_card', methods=['POST'])
def edit_user():
    try:
        id = request.args.get('ID')
        data = request.get_json()
        name = data.get('Name')
        cmnd = data.get('CMND')
        gender = data.get('Gender')
        picture = data.get('Picture')
        dob = data.get('DoB')
        exp_date_ticket = data.get('Exp_date_ticket')
        balance = data.get('Balance')
        exp_date_card = data.get('Exp_date_card')
        types_of_ticket = data.get('Types_of_ticket')
        update_user(id, name, cmnd, gender, picture, dob, exp_date_ticket, balance, exp_date_card, types_of_ticket)
        return jsonify({
            'status': 'OK'
        })
    except Exception as e:
        return jsonify({
            'status': 'failed to edit',
            'error': e.__str__()
        })


@app.route('/delete_card', methods=['POST'])
def delete_card():
    try:
        id = request.args.get('ID')
        delete_user(id)
        return jsonify({
            'status': 'OK'
        })
    except Exception as e:
        return jsonify({
            'status': 'failed to delete',
            'error': e.__str__()
        })


if __name__ == '__main__':
    app.run()
