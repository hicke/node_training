import redis
import time

r = redis.StrictRedis(host='localhost', port=6379, db=1)

for data in range(100):
    r.set(data, 'dataID: ' + str(data))
