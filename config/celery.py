# coding:utf-8
# celery option
import os
env = os.getenv("lady_env")

# 默认开发环境
if env == "prod":
    class CeleryConfig(object):
        main = "tasks"
        broker_url = "amqp://rabbituser1:xjifajijiwx@139.199.206.110/"
        result_backend = "amqp://rabbituser1:xjifajijiwx@139.199.206.110/"
        include = ['tasks.tasks']
        result_expires = 3600
else:
    class CeleryConfig(object):
        main = "tasks"
        broker_url = "amqp://"
        result_backend = "amqp://"
        include = ['tasks.tasks']
        result_expires = 3600


# scan option
global_options = '-n -sT -sV -O --script=banner -p T:21-25,80-89,110,143,443,513,873,1080,1433,1521,1158,3306-3308,3389,3690,4848,5900,6379,7001,8000-9001,9418,27017-27019,50060,111,11211,2049,1099,1090,9200,2375,3128,6081,3500,53,5555,9230'
global_log_states = ['open']

