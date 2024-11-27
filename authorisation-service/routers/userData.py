from fastapi import APIRouter

from controllers.userData import getUserDetails

router = APIRouter()


@router.get('/getUserData/{userId}', tags=["Auth"])
def auth(userId: int):
    userData = getUserDetails(userId)
    return userData
