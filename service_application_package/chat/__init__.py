from flask import Flask
import redis
myredis = redis.StrictRedis(host='pmschat.rpwclh.ng.0001.use1.cache.amazonaws.com',port=6379,db=0)