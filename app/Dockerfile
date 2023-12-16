# Укажите базовый образ
FROM python:3.9

# Установите текущую рабочую директорию
WORKDIR /app

RUN groupadd -r sasha && useradd -r -g sasha sasha

USER sasha 

# Установите зависимости
RUN pip install Flask==2.1.3 && apt install -y curl

# Скопируйте файлы приложения в рабочую директорию
COPY . .

# Укажите порт, на котором запускается приложение
EXPOSE 5000

# Задайте команду, которая будет выполняться при запуске контейнера
CMD ["python", "app.py"]