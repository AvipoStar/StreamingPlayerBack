prod mode:
  Остановка и удаление старых контейнеров: sudo docker-compose -f docker-compose.prod.yml down
  Перестройка образов: sudo docker-compose -f docker-compose.prod.yml build --no-cache
  Запуск контейнеров заново: sudo docker-compose -f docker-compose.prod.yml up -d
  Проверка логов: sudo docker-compose -f docker-compose.prod.yml logs

dev mode:
  Остановка и удаление старых контейнеров: sudo docker-compose -f docker-compose.dev.yml down
  Перестройка образов: sudo docker-compose -f docker-compose.dev.yml build --no-cache
  Запуск контейнеров заново: sudo docker-compose -f docker-compose.dev.yml up -d
  Проверка логов: sudo docker-compose -f docker-compose.dev.yml logs