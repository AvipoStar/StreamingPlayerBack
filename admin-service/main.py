from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware
from routers.login import router as auth_router
from routers.registration import router as reg_router
from routers.userData import router as user_router

app = FastAPI()

# Добавляем middleware для обработки CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Здесь можно указать список допустимых источников запросов
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все HTTP методы
    allow_headers=["*"],  # Разрешаем все заголовки
)

app.include_router(
    router=auth_router,
    prefix='/auth'
)
app.include_router(
    router=reg_router,
    prefix='/reg'
)
app.include_router(
    router=user_router,
    prefix='/user'
)
