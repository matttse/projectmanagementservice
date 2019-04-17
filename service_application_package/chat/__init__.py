from flask import Flask
import redis
import os



REDIS_URL = os.environ.get('REDIS_URL')

myredis = redis.from_url(REDIS_URL)