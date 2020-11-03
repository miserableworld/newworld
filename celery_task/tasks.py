# -*- coding: utf-8 -*- 
# @Time : 20-10-16 下午1:44 
# @Author : lgh 
# @File : tasks.py

# task：任务
# broker（中间人）：存储任务的队列
# worker：真正执行任务的工作者
# backend：用来存储任务执行后的结果

import time

from celery import Celery
from celery.schedules import crontab

celery_app = Celery("celery_task",broker="redis://localhost:6379/0",backend="redis://localhost:6379/1")

# 异步任务
@celery_app.task
def send_email():
    print('邮件开始发送。。。。')
    time.sleep(10)
    print('邮件发送完成。。。。')

# 定时任务
@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender,**kwargs):
    # 每10秒执行一次
    sender.add_periodic_task(10.0,periodic_task.s("hello"),name='add every 10')

    # 每30秒执行一次
    sender.add_periodic_task(30.0,periodic_task.s("world"))

    # 每天的早上定时执行

    sender.add_periodic_task(crontab(
        hour=7,minute=30,day_of_week=1
    ))

@celery_app.task
def periodic_task(arg):
    print(arg)
