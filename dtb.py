from peewee import *

db = MySQLDatabase('sql12617601', host='sql12.freesqldatabase.com', port=3306, user='sql12617601', password='WgNvzqpavt')

if __name__ == '__main__':
    try:
        db.connect()
        print('Connected to database')
    except:
        print('Failed to connect to database')