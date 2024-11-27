from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware
from routers.playlist import router as playlist_router
from routers.favorites import router as favorites_router


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
    router=playlist_router,
    prefix='/playlist'
)

app.include_router(
    router=favorites_router,
    prefix='/favorites'
)