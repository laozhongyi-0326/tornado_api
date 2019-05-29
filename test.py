# -*- coding: utf-8 -*-'
'''
@author: zhangjin
@license: (C) Copyright 2016-2020, Node Supply Chain Manager Corporation Limited.
redis_conent = redis.StrictRedis(host='39.105.6.15', port='30319', db=9)
@software: garner
@file: test.py
@time: 2019/5/9 5:05 PM
@desc:
'''
# from pandas import Series, DataFrame
# import pandas as pd
# import numpy as np
# import random
from __future__ import unicode_literals
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.gen
from selenium import webdriver
from datetime import datetime
import signal
import time
import os
import yaml
import urllib
import json
import requests
from multiprocessing import Process
import logging.config
from PIL import Image




class ScreenCaptureHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        order_id = self.get_argument('order_id', None)
        self.write(order_id)
        self.finish()
