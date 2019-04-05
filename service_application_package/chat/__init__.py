from flask import Flask
import redis
import os


url = os.environ.get('REDISCLOUD_URL')
port = os.environ.get('REDIS_PORT')
password = os.environ.get('REDIS_PW')
REDIS_URL = os.environ.get('REDIS_URL')


# myredis = redis.Redis(host=url,port=port,password=password,ssl=True)
# myredis = redis.Redis(host='localhost',port=6379,db=0)
myredis = redis.from_url(REDIS_URL)