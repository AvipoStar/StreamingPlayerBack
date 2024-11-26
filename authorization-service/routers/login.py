from fastapi import APIRouter

from controllers.login import login, loginToken
from models.login import LoginClass
from models.token import Token

router = APIRouter()


@router.post('/login', tags=["Auth"])
def auth(loginData: LoginClass):
    user = login(loginData.email, loginData.password)
    return user


@router.post('/loginToken', tags=["Auth"])
def auth_token(token: Token):
    user = loginToken(token.value)
    return user
