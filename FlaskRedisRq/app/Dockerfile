FROM python:3.9-alpine

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip uninstall click -y && pip install click==7.1.2