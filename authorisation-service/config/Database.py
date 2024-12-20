import mysql.connector
import os
from sshtunnel import SSHTunnelForwarder

def getConnection():
    mode = os.getenv('MODE', 'prod')
    if mode == 'dev':
       
        remote_bind_address = ('localhost', 33060)

        with SSHTunnelForwarder(
            ('79.104.192.137', 2222),
            ssh_username='jane',
            ssh_password='1251',
            remote_bind_address=remote_bind_address
        ) as tunnel:
            db = mysql.connector.connect(
                host='127.0.0.1',
                port=tunnel.local_bind_port,
                user='root',
                password='MySQL_Password01!',
                database='test'
            )
            return db
    else:
        # Локальное подключение для продакшн-режима
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='MySQL_Password01!',
            database='test'
        )
        return db
