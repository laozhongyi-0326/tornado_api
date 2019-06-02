# coding=utf-8
# -*- coding: utf-8 -*-'
'''
@author: zhangjin
@license: (C) Copyright 2016-2020, Node Supply Chain Manager Corporation Limited.
redis_conent = redis.StrictRedis(host='39.105.6.15', port='30319', db=9)
@software: garner
@file: mp4_to_mp3.py
@time: 2019/5/10 3:42 PM
@desc:
'''

import json
import re
import urllib
import requests
import tornado.web
import tornado.ioloop
import tornado.httpserver
import redis
import uuid
import hashlib
import time

class VideoRecording(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):

        self.write('<!DOCTYPE html>\
                    <html lang="en">\
                    <head>\
                        <meta charset="UTF-8">\
                        <title>录屏</title>\
                    </head>\
                    <body>\
                        <form action="videorecording" method="post" enctype="multipart/form-data">\
                            <em>平台名字:</em>\
                            <input type="text" name="platform">\
                            <br/>\
                            <em>user_id:</em>\
                            <input type="text" name="user_id">\
                            <br/>\
                            <em>开始时间:</em>\
                            <input type="text" name="live_predicted_created_time">\
                            <br/>\
                            <em>结束时间:</em>\
                            <input type="text" name="live_predicted_finished_time">\
                            <br/>\
                            <em>项目名称:</em>\
                            <input type="text" name="project_name">\
                            <br/>\
                            <em>需求人员:</em>\
                            <input type="text" name="customer">\
                            <br/>\
                            <input type="submit" value="sumbit">\
                        </form>\
                    </body>\
                    </html>')

    def post(self, *args, **kwargs):
        try:
            platform = self.get_argument('platform', None)
            user_id = self.get_argument('user_id', None)
            live_predicted_created_time = self.get_argument('live_predicted_created_time', None)
            live_predicted_finished_time = self.get_argument('live_predicted_finished_time', None)
            project_name = self.get_argument('project_name', None)
            customer = self.get_argument('customer', None)
            print(platform, user_id, live_predicted_created_time, live_predicted_finished_time, project_name, customer)

            if platform and user_id and live_predicted_created_time and live_predicted_finished_time and project_name and customer:
                if live_predicted_created_time < live_predicted_finished_time:
                    if len(live_predicted_finished_time) == len(live_predicted_created_time):
                        redis_cli = redis.StrictRedis(host='47.104.190.237', port=6379, db=8)
                        md5 = hashlib.md5()
                        md5.update(unicode(uuid.uuid1()))
                        exclusive_key = md5.hexdigest()[:5]
                        task_key = '-'.join([platform, user_id, project_name, customer, exclusive_key])
                        redis_cli.hmset(task_key, {'platform': platform, 'user_id': user_id,
                                                   'live_predicted_created_time': live_predicted_created_time,
                                                   'live_predicted_finished_time': live_predicted_finished_time,
                                                   'project_name': project_name, 'customer': customer,
                                                   'task_crated_timestamp': int(time.time())})
                        redis_cli.hset('live_recorder_status', task_key, 'None')
                        message  = "成功"
                        self.write(message)
                        self.finish()
                    else:
                        message = "时间有问题"
                        self.write(message)
                        self.finish()
                else:
                    message = "时间有问题"
                    self.write(message)
                    self.finish()
            else:
                message = "参数不能为空"
                self.write(message)
                self.finish()
            # if link:
            #     url = "http://wexin.qianbaihe.wang/douyin/DouyinUrl"
            #     data_url = 'http://v.douyin.com/MnReAm/ '
            #     querystring = {"url": urllib.quote(link)}
            #     headers = {
            #         'Cookie': "Hm_lvt_dfe56523d6dac04aa163867242e3451a=1559366388; Hm_lpvt_dfe56523d6dac04aa163867242e3451a=1559366388",
            #         'Origin': "http://wexin.qianbaihe.wang",
            #         'Accept-Encoding': "gzip, deflate",
            #         'Accept-Language': "zh-CN,zh;q=0.9",
            #         'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            #         'Accept': "*/*",
            #         'Referer': "http://wexin.qianbaihe.wang/Douyin/Index",
            #         'X-Requested-With': "XMLHttpRequest",
            #         'Proxy-Connection': "keep-alive",
            #         'Content-Length': "0",
            #         'Cache-Control': "no-cache",
            #         'Postman-Token': "dbc8a21f-aeaa-4ece-aaf3-c1a1977cead7,3c66fcd2-35c5-48b4-b4b4-60f8b4889709",
            #         'Host': "wexin.qianbaihe.wang",
            #         'Connection': "keep-alive",
            #     }
            #     response = requests.request("POST", url, params=querystring)
            #
            #     json_dict = json.loads(response.content.decode('utf-8'))
            #     urls = json_dict['Model']['DownUrl']
            #     # print(urls)
            #     DownUrl = urllib.unquote(re.search('url=(.*)', urls).group(1))
            #     self.write(DownUrl)
            #     self.finish()
            #
            # else:
            #     self.write("链接不能为空")
            #     self.finish()

        except Exception as e:
            error_message = "位置错误:{}".format(e)
            self.write(error_message)
            self.finish()

