from flask import Flask
from models import function
from rq import Queue
import redis

app = Flask(__name__)
r = redis.Redis(host='redis-server', port=6379)
q = Queue(connection=r)

@app.route("/<inp>")
def process(inp):
    job = q.enqueue(function, inp)
    return f"Task queued {job.id}, {len(q)} number of tasks left in queue"

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0',port=5001)