FROM python:latest

# Установка обновления pip
RUN pip install --upgrade pip

# Копируем requirements в контейнер
COPY ./requirements.txt ./
# Установка всех зависимостей 
RUN pip install -r requirements.txt

# Копирование корневой дирректории в контейнер
COPY ./mysite /app

# Объявление рабочей дерриктории
WORKDIR /app

# Копирование скрипта запуска
COPY ./entrypoint.sh /

# Запуск
ENTRYPOINT ["sh", "/entrypoint.sh"]