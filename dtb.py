from peewee import *
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
        'Types_of_ticket': customer['Types_of_ticket']
    }


def add_user(name, cmnd, gender, picture, dob, exp_date_ticket, balance, exp_date_card, types_of_ticket):
    record = NoEncryptedCustomer(Name=name, CMND=cmnd, Gender=gender, Picture=picture, DoB=dob, Exp_date_ticket=exp_date_ticket, Balance=balance, Exp_date_card=exp_date_card, Types_of_ticket=types_of_ticket)
    record.save()


def edit_user(id, name, cmnd, gender, picture, dob, exp_date_ticket, balance, exp_date_card, types_of_ticket):
    record = NoEncryptedCustomer.get_by_id(id)
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


def delete_user(id):
    record = NoEncryptedCustomer.get_by_id(id)
    record.delete_instance()


if __name__ == '__main__':
    try:
        db.connect()
        print('Connected to database')
    except Exception:
        print('Failed to connect to the database')