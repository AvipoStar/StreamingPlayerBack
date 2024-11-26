from fastapi import APIRouter

from controllers.login import getUserDetails

router = APIRouter()


@router.get('/getUserData/{userId}', tags=["Auth"])
def auth(userId: int):
    userData = getUserDetails(userId)
    return userData
