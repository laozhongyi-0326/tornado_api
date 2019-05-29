
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


class UpFileHandler(tornado.web.RequestHandler):
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
                        <form action="mp4_to_mp3" method="post" enctype="multipart/form-data">\
                            <input type="file" name="file">\
                            <input type="submit" value="shangchuan">\
                        </form>\
                    </body>\
                    </html>')

        #write里面内容是一个简单的完整页面，为了博客方便，放在了一起，建议分开
    def post(self, *args, **kwargs):
        try:
            #查看上传文件的完整格式，files以字典形式返回
            #print(self.request.files)
            #{'file1':
            #[{'filename': '新建文本文档.txt', 'body': b'61 60 -83\r\n-445 64 -259', 'content_type': 'text/plain'}],
            #'file2':
            filesDict=self.request.files
            for inputname in filesDict:
                #第一层循环取出最外层信息，即input标签传回的name值
                #用过filename键值对对应，取出对应的上传文件的真实属性
                http_file=filesDict[inputname]
                for fileObj in http_file:
                    #第二层循环取出完整的对象
                    #取得当前路径下的upfiles文件夹+上fileObj.filename属性(即真实文件名)
                    filePath=os.path.join(os.path.dirname(__file__),fileObj.filename)
                    with open(filePath,'wb') as f:
                         f.write(fileObj.body)
            changefile = filePath
            outputfile = changefile.replace('mp4','mp3')
            ff = FFmpeg(
                inputs={changefile: None},
                # outputs={outputfile: '-vn -ar 44100 -ac 2 -ab 192 -f wav'},
                outputs={outputfile: ' -f mp3'}
            )
            a = ff.cmd
            ff.run(a)

            b = outputfile.split('/home/zhangjin')[-1]
            self.write(outputfile)
            # self.write('http://127.0.0.1:9501{}'.format(str(b)))
            # self.write('http://47.104.190.237:9501{}'.format(str(b)))
            self.finish()
        except Exception as e:
            error_message = "{}".format(e)
            self.write(error_message)
            self.finish()



