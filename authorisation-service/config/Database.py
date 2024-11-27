import mysql.connector
import os
from sshtunnel import SSHTunnelForwarder

def getConnection():
    mode = os.getenv('MODE', 'prod')
    if mode == 'dev':
        # SSH-туннель для режима разработки
        ssh_host = os.getenv('SSH_HOST')
        ssh_user = os.getenv('SSH_USER')
        ssh_password = os.getenv('SSH_PASSWORD')
        remote_bind_address = ('localhost', 3306)

        with SSHTunnelForwarder(
            (ssh_host, 22),
            ssh_username=ssh_user,
            ssh_password=ssh_password,
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
