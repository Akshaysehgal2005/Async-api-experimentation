FROM python:3.9-alpine

COPY ./app /app
WORKDIR /app

RUN apk add git
RUN pip install flask
RUN pip install redis
RUN pip install rq
#RUN pip install git+https://github.com/jace/rq-dashboard.git@master

CMD ["python","app_rq.py"]

#docker build -t app_flask -f Dockerfile .
#docker run -d -p 5001:5001 app_flask
#docker run -p 5001:5001 app_flask
