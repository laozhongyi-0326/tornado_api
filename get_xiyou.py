# -*- coding: utf-8 -*-'
'''
@author: zhangjin
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
@license: (C) Copyright 2016-2020, Node Supply Chain Manager Corporation Limited.
redis_conent = redis.StrictRedis(host='39.105.6.15', port='30319', db=9)
@software: garner
@file: get_xiyou.py
@time: 2019/5/29 4:55 PM
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
import tornado.web
import tornado.ioloop
import tornado.httpserver
import os
from ffmpy import FFmpeg



class Xiyou(tornado.web.RequestHandler):
    #tornado.httputil.HTTPFile对象三个属性
    #1.filename文件名
    #2.body文件内部实际内容
    #3.type文件的类型
    def get(self, *args, **kwargs):
        self.write('''<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <title>Title</title>
                        </head>
                        <body>
                            <a href="http://www.zhuxinya.top:9500/home/zhangjin/xiyouji/01.mp3">01[第一讲]《西游记》的由来和孙悟空的出身</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/02.mp3">02[第二讲]四大部洲与孙悟空的颜值</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/03.mp3">03[第三讲]孙悟空的绝技绝在哪里，爹妈究竟是谁？</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/04.mp3">04[第四讲]孙悟空原型为何，历史上确有其人吗？</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/05.mp3">05[第五讲]孙悟空的师傅，菩提老祖有多牛？</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/06.mp3">06[第六讲]孙悟空的兵器，如意金箍棒是什么来头？</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/07.mp3">07[第七讲]太白金星与太上老君有关系吗？</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/08.mp3">08[第八讲]李天王与哪吒三太子确有其人吗？</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/09.mp3">09[第九讲]王母娘娘和她家的蟠桃会</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/10.mp3">10[第十讲]如来佛祖与观音菩萨</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/11.mp3">11[第十一讲]唐僧的父母爱情故事</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/12.mp3">12[第十二讲]唐玄奘的前世今生</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/13.mp3">13[第十三讲]唐僧缘何去取经？取经带了哪些法宝？</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/14.mp3">14[第十四讲]令人抓狂的唐玄奘</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/15.mp3">15[第十五讲]我的宝贝袈裟啊！金池长老的收藏癖</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/16.mp3">16[第十六讲]最可爱的妖怪：黑熊怪</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/17.mp3">17[第十七讲]猪八戒为什么错投了猪胎？</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/18.mp3">18[第十八讲]八戒的相貌和法宝</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/19.mp3">19[第十九讲]猪八戒是“相声鼻祖”？</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/20.mp3">20[第二十讲]谁才是《西游记》中的人气王？</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/21.mp3">21[第二十一讲]预测大师乌巢禅师</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/22.mp3">22[第二十二讲]老鼠精偷油的蝴蝶效应</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/23.mp3">23[第二十三讲]长相与原著出入最大的沙和尚</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/24.mp3">24[第二十四讲]被贬下界的沙和尚是卧底？</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/25.mp3">25[第二十五讲]沙和尚曾经吃过唐僧的九个前世？</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/26.mp3">26[第二十六讲]沙和尚的存在感到底有多少？</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/27.mp3">27[第二十七讲]镇元大仙的小九九和他的人参果</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/28.mp3">28[第二十八讲]白骨精怎么知道唐僧肉能长生不老？</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/29.mp3">29[第二十九讲]白骨精其实有背景</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/30.mp3">30[第三十讲]最痴情的妖怪，奎木狼</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/31.mp3">31[第三十一讲]金角银角大王为何认九尾狐做干娘</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/32.mp3">32[第三十二讲]红孩儿比孙悟空厉害？</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/33.mp3">33[第三十三讲]牛魔王与铁扇公主的爱情</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/34.mp3">34[第三十四讲]悄悄问圣僧，女儿美不美</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/35.mp3">35[第三十五讲]女儿国是否确有其国</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/36.mp3">36[第三十六讲]真假美猴王到底谁去取了真经</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/37.mp3">37[第三十七讲]荆棘岭木仙庵杏仙问禅</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/38.mp3">38[第三十八讲]和唐僧有前世缘的老鼠精</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/39.mp3">39[第三十九讲]雌雄莫辨的的玉兔精</a>
                            <br>
                            <a href="http://www.zhuxinya.top:9501/home/zhangjin/xiyouji/40.mp3">40[第四十讲]《西游记》里的真经</a>
                            <br>
                        </body>
                        </html>''')
