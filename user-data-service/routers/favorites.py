from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from typing import Optional

from controllers.favorites import addTrack, removeTrack, getTracks

# Конфигурация для JWT
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user_id_from_token(token: str = Depends(oauth2_scheme)) -> int:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: Optional[int] = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        return user_id
    except jwt.PyJWTError:
        raise credentials_exception


router = APIRouter()


@router.post('/', tags=["Favorites"])
def add_to_favorites(track_id: int, user_id: int = Depends(get_user_id_from_token)):
    result = addTrack(track_id, user_id)
    return result


@router.delete('/', tags=["Favorites"])
def remove_from_favorites(track_id: int, user_id: int = Depends(get_user_id_from_token)):
    result = removeTrack(track_id, user_id)
    return result


@router.get('/', tags=["Favorites"])
def get_favorites(user_id: int = Depends(get_user_id_from_token)):
    result = getTracks(user_id)
    return result
