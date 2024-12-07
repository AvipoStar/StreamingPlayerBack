# Используем официальный Python образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем необходимые инструменты для компиляции
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*


# Создаем виртуальное окружение
RUN python -m venv /app/venv

# Активируем виртуальное окружение
ENV PATH="/app/venv/bin:$PATH"


# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код
COPY . .

# Указываем порт, на котором будет работать приложение
EXPOSE 8000

# Запускаем приложение
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
