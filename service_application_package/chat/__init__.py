from flask import Flask
import redis
import os 
# myredis = redis.Redis(host='localhost',port=6379,db=0)
myredis = redis.from_url(os.environ.get("REDIS_URL"))
