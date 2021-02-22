import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ia7n8a8p7a3p0h0s1i5h8s0a'
    