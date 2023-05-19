from peewee import *

db = PostgresqlDatabase(
    'dtb_name',
    user='dtb_name_user',
    password='TYl0xeFfLoxdsn10HhA2qIcP9H65nGOR',
    host='dpg-chjf1qrhp8u4bdv9gfh0-a',
    port=5432
)

# class Customer(Model):
#     ID = IntegerField()
#     Name = BlobField()
#     DoB = DateField()
#     monthly_ticket = DateField()
#     class Meta:
#         database = db


if __name__ == '__main__':
    db.connect()
    print('Connected to database')