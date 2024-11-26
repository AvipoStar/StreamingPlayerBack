import mysql.connector


def getConnection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="streamingplaer"
    )
    return db
