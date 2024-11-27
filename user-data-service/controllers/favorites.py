import datetime

from fastapi import FastAPI, HTTPException, status

from config.Database import getConnection
from models.playlist import Playlist, createPlaylist
from mysql.connector import Error

app = FastAPI()


def addTrack(track_id: int, playlist_id: int):
    connection = getConnection()
    if connection is None:
        return

    cursor = connection.cursor()
    query = "INSERT INTO favorites (media_item_id, user_id, created_at) VALUES (%s, %s, %s)"
    values = (playlist_id, track_id, datetime.datetime)

    try:
        cursor.execute(query, values)
        connection.commit()
        return True
    except Error as e:
        print(f"Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка добавление трэка"
        )
    finally:
        cursor.close()
        connection.close()


def removeTrack(track_id: int):
    connection = getConnection()
    if connection is None:
        return

    cursor = connection.cursor()
    query = "DELETE FROM favorites WHERE media_item_id = %s"
    values = track_id

    try:
        cursor.execute(query, values)
        connection.commit()
        return True
    except Error as e:
        print(f"Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка удаления трэка"
        )
    finally:
        cursor.close()
        connection.close()
