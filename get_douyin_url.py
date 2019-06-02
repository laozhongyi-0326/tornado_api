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


class DownUrl(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):

        self.write('<!DOCTYPE html>\
                    <html lang="en">\
                    <head>\
                        <meta charset="UTF-8">\
                        <title>Title</title>\
                    </head>\
                    <body>\
                        <form action="DownUrl" method="post" enctype="multipart/form-data">\
                            <em>原始链接:</em>\
                            <input type="text" name="link">\
                            <br/>\
                            <input type="submit" value="sumbit">\
                        </form>\
                    </body>\
                    </html>')

    def post(self, *args, **kwargs):
        try:
            link = self.get_argument('link', None)
            if link:
                url = "http://wexin.qianbaihe.wang/douyin/DouyinUrl"
                data_url = 'http://v.douyin.com/MnReAm/ '
                querystring = {"url": urllib.quote(link)}
                headers = {
                    'Cookie': "Hm_lvt_dfe56523d6dac04aa163867242e3451a=1559366388; Hm_lpvt_dfe56523d6dac04aa163867242e3451a=1559366388",
                    'Origin': "http://wexin.qianbaihe.wang",
                    'Accept-Encoding': "gzip, deflate",
                    'Accept-Language': "zh-CN,zh;q=0.9",
                    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                    'Accept': "*/*",
                    'Referer': "http://wexin.qianbaihe.wang/Douyin/Index",
                    'X-Requested-With': "XMLHttpRequest",
                    'Proxy-Connection': "keep-alive",
                    'Content-Length': "0",
                    'Cache-Control': "no-cache",
                    'Postman-Token': "dbc8a21f-aeaa-4ece-aaf3-c1a1977cead7,3c66fcd2-35c5-48b4-b4b4-60f8b4889709",
                    'Host': "wexin.qianbaihe.wang",
                    'Connection': "keep-alive",
                }
                response = requests.request("POST", url, params=querystring)

                json_dict = json.loads(response.content.decode('utf-8'))
                urls = json_dict['Model']['DownUrl']
                # print(urls)
                DownUrl = urllib.unquote(re.search('url=(.*)', urls).group(1))
                self.write(DownUrl)
                self.finish()

            else:
                self.write("链接不能为空")
                self.finish()

        except Exception as e:
            error_message = "位置错误:{}".format(e)
            self.write(error_message)
            self.finish()




    #
    # url = "http://wexin.qianbaihe.wang/douyin/DouyinUrl"
    # data_url = 'http://v.douyin.com/MnReAm/ '
    # querystring = {"url": urllib.quote(data_url)}
    #
    # headers = {
    #     'Cookie': "Hm_lvt_dfe56523d6dac04aa163867242e3451a=1559366388; Hm_lpvt_dfe56523d6dac04aa163867242e3451a=1559366388",
    #     'Origin': "http://wexin.qianbaihe.wang",
    #     'Accept-Encoding': "gzip, deflate",
    #     'Accept-Language': "zh-CN,zh;q=0.9",
    #     'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    #     'Accept': "*/*",
    #     'Referer': "http://wexin.qianbaihe.wang/Douyin/Index",
    #     'X-Requested-With': "XMLHttpRequest",
    #     'Proxy-Connection': "keep-alive",
    #     'Content-Length': "0",
    #     'Cache-Control': "no-cache",
    #     'Postman-Token': "dbc8a21f-aeaa-4ece-aaf3-c1a1977cead7,3c66fcd2-35c5-48b4-b4b4-60f8b4889709",
    #     'Host': "wexin.qianbaihe.wang",
    #     'Connection': "keep-alive",
    #     }
    #
    # # response = requests.request("POST", url, headers=headers, params=querystring)
    # response = requests.request("POST", url, params=querystring)
    #
    # json_dict = json.loads(response.content.decode('utf-8'))
    # urls = json_dict['Model']['DownUrl']
    # # print(urls)
    # DownUrl = urllib.unquote(re.search('url=(.*)', urls).group(1))
    # print(DownUrl)


