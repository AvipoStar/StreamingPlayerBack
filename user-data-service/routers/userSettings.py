from fastapi import APIRouter

from controllers.userSettings import editUserProfile
from models.userSettings import User

router = APIRouter()


@router.put('/', tags=["UserSettings"])
def change_user_settings(userData: User):
    result = editUserProfile(userData)
    return result
