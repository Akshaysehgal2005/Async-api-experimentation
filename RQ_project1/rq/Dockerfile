FROM python:3.9-alpine

RUN pip install rq

CMD ["rq","worker","-u","redis://redis:6379","high","default","low"]
