from pydantic import BaseModel
from MySQLdb.times import Date

class RegistrationClass(BaseModel):
    email: str
    password: str
    surname: str
    name: str
    patronymic: str
    bornDate: Date
