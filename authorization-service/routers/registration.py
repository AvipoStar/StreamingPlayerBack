from fastapi import APIRouter

from controllers.login import register_user
from models.registration import RegistrationClass

router = APIRouter()


@router.post('/register', tags=["Auth"])
def auth(registrationData: RegistrationClass):
    user = register_user(registrationData)
    return user
