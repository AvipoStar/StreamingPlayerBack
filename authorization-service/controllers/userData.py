from fastapi import FastAPI, HTTPException, status

from config.Database import getConnection

app = FastAPI()


def getUserDetails(user_id: int):
    db = getConnection()
    cursor = db.cursor()

    try:
        # Запрос к базе данных для получения данных пользователя по user_id
        cursor.execute("SELECT surname, name, patronymic, bornDate, email FROM users WHERE id = %s", (user_id,))
        result = cursor.fetchone()

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Пользователь не найден"
            )

        surname, name, patronymic, bornDate, email = result

        return {
            "userId": user_id,
            "surname": surname,
            "name": name,
            "patronymic": patronymic,
            "bornDate": bornDate,
            "email": email
        }

    finally:
        cursor.close()
        db.close()
