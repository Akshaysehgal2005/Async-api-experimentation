
import time

def background_task(n):
    delay = 2
    print("Task running")
    time.sleep(delay)
    print("Task completed")
    print('output -> ',len(n))
    return len(n)