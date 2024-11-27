from fastapi import FastAPI, HTTPException, status

from config.Database import getConnection
from mysql.connector import Error

from models.userSettings import User

app = FastAPI()


def editUserProfile(user: User):
    connection = getConnection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection error")

    cursor = connection.cursor()
    query = """
    UPDATE users
    SET email = %s, password = %s, name = %s, surname = %s, patronymic = %s, bornDate = %s, nickname = %s, created_at = %s
    WHERE id = %s
    """
    values = (
        user.email, user.password, user.name, user.surname, user.patronymic, user.bornDate, user.nickname,
        user.created_at,
        user.id)

    try:
        cursor.execute(query, values)
        connection.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
        print(f"User with ID {user.id} updated successfully")
        return user.id
    except Error as e:
        print(f"Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка обновления пользователя"
        )
    finally:
        cursor.close()
        connection.close()
