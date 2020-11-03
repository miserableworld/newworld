# -*- coding: utf-8 -*- 
# @Time : 20-10-16 下午2:22 
# @Author : lgh 
# @File : create_task.py

from flask import Blueprint

from celery_task.tasks import send_email

task = Blueprint('celery_task',__name__)

@task.route('/add_task',methods=['GET'])
def add_task():
    """
    添加任务
    :return:
    """
    send_email.delay()
    return '添加成功 ！！！'

