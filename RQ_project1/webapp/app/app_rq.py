#Install docker and run docker

#Create new env and activate 
#> conda create -n mlops python=3.9
#> conda activate mlops

#Install flask, redis, rq, rq-dashboard
#conda install flask
#conda install -c anaconda redis
#conda install -c conda-forge rq
#pip install git+https://github.com/jace/rq-dashboard.git@master

from flask import Flask, request
import redis
from rq import Queue
from model import background_task

app = Flask(__name__)

#https://stackoverflow.com/questions/54965291/error-99-connecting-to-localhost6379-cannot-assign-requested-address
r = redis.Redis(host='redis', port=6379, decode_responses=True)
q = Queue(connection=r)

@app.route("/task/<inp>")
def add_task(inp):
    job = q.enqueue(background_task, inp)
    return f"Task {job.id} added to queue at {job.enqueued_at}. {len(q)} tasks in queue"

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)

#TO RUN
#docker run --name redis01 -p 6379:6379 redis
### docker ps -a  ###check list of containers
### docker start -i redis01 ###Restart existing container

#Run this in multiple tabs for multiple workers & from app directory
#rq worker ### OR ### rq worker high default low

#run the flask api with relevant env
#rq-dashboard

