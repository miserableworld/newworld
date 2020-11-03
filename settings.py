# -*- coding: utf-8 -*- 
# @Time : 20-10-16 下午1:30 
# @Author : lgh
# @File : settings.py
import os

class Config(object):
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    TESTING = False


class ProjectConfig(Config):
    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/1"

