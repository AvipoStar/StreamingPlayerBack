import hashlib

import jwt
from fastapi import FastAPI, HTTPException, status

from config.Database import getConnection
from models.registration import RegistrationClass

app = FastAPI()

SECRET_KEY = "stream"
ALGORITHM = "HS256"


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(registration_data: RegistrationClass):
    db = getConnection()
    cursor = db.cursor()

    try:
        # Проверка на существование пользователя с таким же email
        cursor.execute("SELECT id FROM users WHERE email = %s", (registration_data.email,))
        result = cursor.fetchone()
        if result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Пользователь с таким email уже существует"
            )

        # Хэширование пароля на Python стороне
        hashed_password = hash_password(registration_data.password)

        # Добавление нового пользователя
        cursor.execute(
            """
            INSERT INTO users (email, password, surname, name, patronymic, bornDate)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                registration_data.email,
                hashed_password,
                registration_data.surname,
                registration_data.name,
                registration_data.patronymic,
                registration_data.bornDate
            )
        )
        db.commit()
        user_id = cursor.lastrowid

    finally:
        cursor.close()
        db.close()

    # Создание access_token для нового пользователя
    access_token = createAccessToken(
        data={"sub": registration_data.email, "id": user_id}
    )

    return {
        "user_id": user_id,
        "access_token": access_token
    }


def createAccessToken(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
