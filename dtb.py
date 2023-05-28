from peewee import *
import random
# from AES_cryption import data_decrypt, data_encrypt

db = PostgresqlDatabase(
    'dtb_name',
    user='dtb_name_user',
    password='TYl0xeFfLoxdsn10HhA2qIcP9H65nGOR',
    host='dpg-chjf1qrhp8u4bdv9gfh0-a',
    port=5432
)


class NoEncryptedCustomer(Model):
    ID = AutoField()
    Name = TextField()
    CMND = TextField()
    Gender = BooleanField()
    Picture = TextField()
    DoB = TextField()
    Exp_date_ticket = TextField()
    Balance = IntegerField()
    Exp_date_card = TextField()
    Types_of_ticket = IntegerField()
    Is_locked = BooleanField()

    class Meta:
        table_name = 'No_Encrypted_Customer'
        database = db


def select_user(id):
    data = NoEncryptedCustomer.select().where(NoEncryptedCustomer.ID == id)
    cus = [item.__dict__['__data__'] for item in data]
    customer = cus[0]
    return {
        'ID': customer['ID'],
        'Name': customer['Name'],
        'CMND': customer['CMND'],
        'Gender': customer['Gender'],
        'Picture': customer['Picture'],
        'DoB': customer['DoB'],
        'Exp_date_ticket': customer['Exp_date_ticket'],
        'Balance': customer['Balance'],
        'Exp_date_card': customer['Exp_date_card'],
        'Types_of_ticket': customer['Types_of_ticket'],
        'Is_locked': customer['Is_locked']
    }


def get_random_record():
    # Lấy tất cả các ID từ bảng
    all_ids = [record.ID for record in NoEncryptedCustomer.select()]

    # Lấy ngẫu nhiên một ID từ danh sách các ID
    random_id = random.choice(all_ids)

    # Sử dụng hàm select_record(id) để lấy bản ghi theo ID
    random_record = select_user(random_id)

    # Kiểm tra kết quả
    if random_record:
        return random_record
    else:
        raise Exception("Don't have any record in the database")


def add_user(name, cmnd, gender, picture, dob, exp_date_ticket, balance, exp_date_card, types_of_ticket):
    record = NoEncryptedCustomer(Name=name, CMND=cmnd, Gender=gender, Picture=picture, DoB=dob, Exp_date_ticket=exp_date_ticket, Balance=balance, Exp_date_card=exp_date_card, Types_of_ticket=types_of_ticket)
    record.save()


def update_user(id, name, cmnd, gender, picture, dob, exp_date_ticket, balance, exp_date_card, types_of_ticket):
    record = NoEncryptedCustomer.get_by_id(id)
    if not record.Is_locked:
        record.Name = name
        record.CMND = cmnd
        record.Gender = gender
        record.Picture = picture
        record.DoB = dob
        record.Exp_date_ticket = exp_date_ticket
        record.Balance = balance
        record.Exp_date_card = exp_date_card
        record.Types_of_ticket = types_of_ticket
        record.save()
    else:
        raise Exception('Locked user')


def delete_user(id):
    record = NoEncryptedCustomer.get_by_id(id)
    if not record.Is_locked:
        record.delete_instance()
    else:
        raise Exception('Locked user')


def lock_user(id):
    record = NoEncryptedCustomer.get_by_id(id)
    if not record.Is_locked:
        record.Is_locked = True
        record.save()
    else:
        raise Exception('User is already locked')


def unlock_user(id):
    record = NoEncryptedCustomer.get_by_id(id)
    if not record.Is_locked:
        raise Exception('User is not locked')
    else:
        record.Is_locked = False


if __name__ == '__main__':
    try:
        db.connect()
        print('Connected to database')
    except Exception:
        print('Failed to connect to the database')