import hashlib

import jwt
from fastapi import FastAPI, HTTPException, status

from config.Database import getConnection

app = FastAPI()

SECRET_KEY = "stream"
ALGORITHM = "HS256"


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def createAccessToken(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def login(email: str, password: str):
    db = getConnection()
    cursor = db.cursor()
    try:
        # Проверка пользователя с таким email
        cursor.execute("SELECT id, password, surname, name FROM users WHERE email = %s", (email,))
        result = cursor.fetchone()

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Пользователь не найден"
            )

        user_id, db_password, surname, name = result

        # Хэширование введённого пароля и проверка
        hashed_password = hash_password(password)
        if db_password != hashed_password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Неверный пароль"
            )

    finally:
        cursor.close()
        db.close()

    # Создание токена
    access_token = createAccessToken(
        data={"sub": email, "id": user_id}
    )

    return {
        "user_id": user_id,
        "access_token": access_token
    }


def loginToken(token: str):
    try:
        # Декодирование токена
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("id")

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Неверный токен"
            )

        # Если токен действителен, возвращаем подтверждение
        return {"message": "Токен действителен", "user_id": user_id}

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Срок действия токена истек"
        )
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный токен"
        )
