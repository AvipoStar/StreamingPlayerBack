from fastapi import FastAPI, HTTPException, status

from config.Database import getConnection
from models.playlist import Playlist, createPlaylist
from mysql.connector import Error

app = FastAPI()


def createPlaylist(playlist: createPlaylist):
    connection = getConnection()
    if connection is None:
        return None

    cursor = connection.cursor()
    query = "INSERT INTO playlists (name, description) VALUES (%s, %s)"
    values = (playlist.name, playlist.description)

    try:
        cursor.execute(query, values)
        connection.commit()
        playlist_id = cursor.lastrowid
        return playlist_id
    except Error as e:
        print(f"Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка создания плейлиста"
        )
    finally:
        cursor.close()
        connection.close()


def deletePlaylist(playlist_id: int):
    connection = getConnection()
    if connection is None:
        return

    cursor = connection.cursor()
    query = "DELETE FROM playlists WHERE id = %s"
    values = (playlist_id,)

    try:
        cursor.execute(query, values)
        connection.commit()
        return True
    except Error as e:
        print(f"Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка удаления плейлиста"
        )
    finally:
        cursor.close()
        connection.close()


def changeName(playlist: createPlaylist):
    connection = getConnection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection error")

    cursor = connection.cursor()
    query = "UPDATE playlists SET name = %s, WHERE id = %s"
    values = (playlist.name, playlist.id)

    try:
        cursor.execute(query, values)
        connection.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Playlist not found")
        else:
            return True
    except Error as e:
        print(f"Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка обновления плейлиста"
        )
    finally:
        cursor.close()
        connection.close()


def addTrack(track_id: int, playlist_id: int):
    connection = getConnection()
    if connection is None:
        return

    cursor = connection.cursor()
    query = "INSERT INTO playlist_items (playlist_id, track_id) VALUES (%s, %s)"
    values = (playlist_id, track_id)

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


def removeTrack(track_id: int, playlist_id: int):
    connection = getConnection()
    if connection is None:
        return

    cursor = connection.cursor()
    query = "DELETE FROM playlist_items WHERE playlist_id = %s AND track_id = %s"
    values = (playlist_id, track_id)

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
