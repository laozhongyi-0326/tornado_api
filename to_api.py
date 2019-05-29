# -*- coding: utf-8 -*-'
'''
@author: zhangjin
@license: (C) Copyright 2016-2020, Node Supply Chain Manager Corporation Limited.
redis_conent = redis.StrictRedis(host='39.105.6.15', port='30319', db=9)
@software: garner
@file: to_api.py
@time: 2019/5/9 5:05 PM
@desc:
'''
# from pandas import Series, DataFrame
# import pandas as pd
# import numpy as np
# import random
import re
import redis
import time
import json
import requests
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from test import ScreenCaptureHandler
from upload_file import UpFileHandler
from post_qingqiu import FileHandler
from get_xiyou import Xiyou



class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/test', ScreenCaptureHandler),
            (r'/xiyou', Xiyou),
            ((r'/mp4_to_mp3',UpFileHandler)),
            ((r'/post_method',FileHandler)),
            # ((r'/fileup',UpFileHandler)),
        ]
        tornado.web.Application.__init__(self, handlers)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(9001)
    tornado.ioloop.IOLoop.instance().start()
