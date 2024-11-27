import datetime

from fastapi import FastAPI, HTTPException, status

from config.Database import getConnection
from models.playlist import Playlist, createPlaylist
from mysql.connector import Error

app = FastAPI()


def addTrack(track_id: int, user_id: int):
    connection = getConnection()
    if connection is None:
        return

    cursor = connection.cursor()
    query = "INSERT INTO favorites (media_item_id, user_id, created_at) VALUES (%s, %s, %s)"
    values = (track_id, user_id, datetime.datetime)

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


def removeTrack(track_id: int, user_id: int):
    connection = getConnection()
    if connection is None:
        return

    cursor = connection.cursor()
    query = "DELETE FROM favorites WHERE media_item_id = %s AND user_id = %s"
    values = (track_id, user_id)

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


def getTracks(user_id: int):
    connection = getConnection()
    if connection is None:
        return

    cursor = connection.cursor()
    query = """SELECT f.user_id, mi.id, mi.title, mi.description, mi.cover_url, u.nickname from favorites f
                join media_items mi on mi.id = f.media_item_id 
                join authors a on a.id = f.user_id 
                join users u on u.id = a.user_id 
                WHERE f.user_id = %s"""
    values = user_id

    try:
        cursor.execute(query, values)
        tracks = cursor.fetchall()
        return tracks
    except Error as e:
        print(f"Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ошибка получения трэков"
        )
    finally:
        cursor.close()
        connection.close()
