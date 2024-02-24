FROM ubuntu

RUN apt-get update && apt-get upgrade -y

ENV PYTHONDONTWRITEBYTECODE 1 PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app

RUN python3-pip
RUN libreoffice -y
RUN pip3 install --upgrade pip 
RUN pip3 install --no-cache-dir -r requirements.txt 
RUN python manage.py makemigrations

CMD sleep 10; python manage.py migrate; python manage.py runserver 0.0.0.0:8000