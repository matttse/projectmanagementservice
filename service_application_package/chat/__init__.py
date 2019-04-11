from flask import Flask
import redis
myredis = redis.Redis(host='localhost',port=6379,db=0)