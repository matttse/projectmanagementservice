from flask import Flask
import redis
import os

myredis = redis.from_url(os.environ.get('REDIS_URL'))