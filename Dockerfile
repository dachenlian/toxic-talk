FROM python:3.7.3
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system
WORKDIR /app/web
