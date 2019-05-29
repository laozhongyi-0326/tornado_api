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
# from pandas import Series, DataFrame
# import pandas as pd
# import numpy as np
# import random
import re
import redis
import time
import json
import requests
import os
from ffmpy import FFmpeg

filepath = "/Users/zhangjin/Movies/VideoDownLoad/kuaishou/3xc827fausssm44tue" #添加路径
# os.chdir(filepath)
filename= os.listdir(filepath) #得到文件夹下的所有文件名称

outputpath = "/Users/zhangjin/Movies/VideoDownLoad/kuaishou/3xc827fausssm44tue" #添加路径
# os.mkdir(outputpath)
os.chdir(outputpath)

for i in range(len(filename)):
    changefile = filepath+"/"+filename[i]
    if 'mp4' in changefile:
        outputfile = outputpath+"/"+filename[i].replace('mp4','mp3')
        print outputfile
        ff = FFmpeg(
                inputs={changefile: None},
                # outputs={outputfile: '-vn -ar 44100 -ac 2 -ab 192 -f wav'},
                outputs={outputfile: '-f mp3'}
                )
        # print ff.cmd
        a = ff.cmd
        print a
        ff.run(a)
