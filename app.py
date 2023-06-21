from datetime import date
from flask import Flask, jsonify, request
from flask_cors import CORS
from dtb import *

app = Flask(__name__)
CORS(app)


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
            'data': get_random_record()
        })
    except Exception as e:
        return jsonify({
            'status': 'failed to check',
            'error': e.__str__()
        })


@app.route('/get_by_id')
def get_by_id():
    try:
        id = request.args.get('ID')
        return jsonify({
            'status': 'OK',
            'data': select_user(id)
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


@app.route('/lock_card', methods=['POST'])
def lock_card():
    try:
        id = request.args.get('ID')
        lock_user(id)
        return jsonify({
            'status': 'OK'
        })
    except Exception as e:
        return jsonify({
            'status': 'failed to lock',
            'error': e.__str__()
        })


@app.route('/unlock_card', methods=['POST'])
def unlock_card():
    try:
        id = request.args.get('ID')
        unlock_user(id)
        return jsonify({
            'status': 'OK'
        })
    except Exception as e:
        return jsonify({
            'status': 'failed to unlock',
            'error': e.__str__()
        })


@app.route('/check_pin', methods=['POST'])
def check_pin():
    data = request.get_json()
    pin_code = data.get('pin_code')
    if pin_code == '123456': # mã pin mặc định = 123456
        return jsonify({
            'connect': True,
            'data': get_random_record() # chưa có thẻ nên trả về một bản ghi bất kỳ
        })
    else:
        return jsonify({
            'connect': False
        })


@app.route('/send_apdu')
def send_apdu():
    return jsonify({
        'data': 'AA BB CC DD EE FF',
        'sw1': '90',
        'sw2': '00'
    })


@app.route('/change_pin', methods=['POST'])
def change_pin():
    data = request.get_json()
    id = data.get('ID')
    old_pin = data.get('old_pin')
    new_pin = data.get('new_pin')
    if old_pin != '123456':
        return jsonify({
            'status': False,
            'message': 'wrong pin code'
       })
    else:
        if new_pin == '123456':
            return jsonify({
                'status': False,
                'message': 'new pin = old pin'
            })
        else:
            return jsonify({
                'status': True
            })


if __name__ == '__main__':
    app.run()
