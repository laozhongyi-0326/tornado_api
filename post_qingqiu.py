
# -*- coding: utf-8 -*-'
'''
@author: zhangjin
@license: (C) Copyright 2016-2020, Node Supply Chain Manager Corporation Limited.
redis_conent = redis.StrictRedis(host='39.105.6.15', port='30319', db=9)
@software: garner
@file: upload_file.py
@time: 2019/5/9 5:36 PM
@desc:
'''
# from pandas import Series, DataFrame
# import pandas as pd
# import numpy as np
# import random
import tornado.web
import tornado.ioloop
import tornado.httpserver
import os
from ffmpy import FFmpeg
class FileHandler(tornado.web.RequestHandler):
    #tornado.httputil.HTTPFile对象三个属性
    #1.filename文件名
    #2.body文件内部实际内容
    #3.type文件的类型
    def get(self, *args, **kwargs):

        self.write('<!DOCTYPE html>\
                    <html lang="en">\
                    <head>\
                        <meta charset="UTF-8">\
                        <title>Title</title>\
                    </head>\
                    <body>\
                        <form action="post_method" method="post" enctype="multipart/form-data">\
                            <input type="file" name="file">\
                            <br/>\
                            <em>开始时间:</em>\
                            <input type="text" name="start_time">\
                            <br/>\
                            <em>截取时间长度:</em>\
                            <input type="text" name="long_time">\
                            <br/>\
                            <input type="submit" value="sumbit">\
                        </form>\
                    </body>\
                    </html>')

    def post(self, *args, **kwargs):
        try:
            filesDict=self.request.files
            start_time = self.get_argument('start_time', None)
            long_time = self.get_argument('long_time', None)
            # self.write('{}::{}'.format(start_time, long_time))
            for inputname in filesDict:
                #第一层循环取出最外层信息，即input标签传回的name值
                #用过filename键值对对应，取出对应的上传文件的真实属性
                http_file=filesDict[inputname]
                for fileObj in http_file:
                    print fileObj.filename
                    #第二层循环取出完整的对象
                    #取得当前路径下的upfiles文件夹+上fileObj.filename属性(即真实文件名)
                    # filePath=os.path.join(os.path.dirname(__file__),fileObj.filename)
                    filePath = 'data/{}'.format(fileObj.filename)
                    with open(filePath,'wb') as f:
                         f.write(fileObj.body)
            changefile = filePath
            outputfile = changefile.replace('mp4','mp3')
            ff = FFmpeg(
                inputs={changefile: None},
                # outputs={outputfile: '-vn -ar 44100 -ac 2 -ab 192 -f wav'},
                outputs={outputfile: ' -f mp3'}
            )
            print outputfile
            a = ff.cmd
            ff.run(a)
            outputfile_s = outputfile.replace('.mp3','_a.mp3')
            f = FFmpeg(
                inputs={changefile: None},
                # outputs={outputfile: '-vn -ar 44100 -ac 2 -ab 192 -f wav'},
                outputs={outputfile_s: ' -ss {} -t {}'.format(start_time, long_time)}
            )
            c = f.cmd
            f.run(c)

            # b = outputfile.split('/home/zhangjin')[-1]
            self.write(outputfile_s)
            # self.write('http://127.0.0.1:9501{}'.format(str(b)))
            # self.write('http://47.104.190.237:9501{}'.format(str(b)))
            self.finish()
        except Exception as e:
            error_message = "{}".format(e)
            self.write(error_message)
            self.finish()



