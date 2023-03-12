from decouple import config

import pymysql

def get_connection():
    return pymysql.connect(
        host=config('MYSQL_HOST'),
        database=config('MYSQL_DB'),
        user=config('MYSQL_USER'),
        password=config('MYSQL_PASSWORD')
    )

def get_connection2():
    return pymysql.connect(
    host="127.0.0.1", port=3307, user="root",
    passwd="Jonny25250509", db="idgs803")
