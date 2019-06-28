FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

#EXPOSE 8000
#
#CMD ["uwsgi", "--ini", "app/uwsgi.ini"]