#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 1:50 PM
# @Author  : w8ay
# @File    : redis.py
import redis  # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

from config import NODE_NAME
from config import REDIS_HOST
from lib.common import lstrsub


def redis_concet():
    host, port = REDIS_HOST.split(":")
    pool = redis.ConnectionPool(host=host, port=port,
                                decode_responses=True)  # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
    redis_con = redis.Redis(connection_pool=pool)
    return redis_con


def add_redis_log(log):
    '''
    添加任务log到redis队列，并对redis队列进行清理，如果超过500则弹出老的
    :param log:
    :return:
    '''
    node_name = "w12_log_{}".format(lstrsub(NODE_NAME, "w12_node_"))
    redis_con.lpush(node_name, str(log))
    while redis_con.llen(node_name) > 500:
        redis_con.rpop(node_name)


redis_con = redis_concet()
