#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import requests

url = 'https://pvp.qq.com/web201605/js/herolist.json'
herolist = requests.get(url)

herolist_json = herolist.json()
hero_name = list(map(lambda x: x['cname'], herolist.json()))
hero_number = list(map(lambda x: x['ename'], herolist.json()))


# down picture
def downloadPic():
    i = 0
    for j in hero_number:
        #
        os.mkdir("D:\\mypic\\wzry\\" + hero_name[i])
        #
        os.chdir("D:\\mypic\\wzry\\" + hero_name[i])
        out = hero_name[i]
        print out
        i += 1
        for k in range(10):
            #
            onehero_link = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(j) + '/' + str(
                j) + '-bigskin-' + str(k) + '.jpg'
            im = requests.get(onehero_link)
            if im.status_code == 200:
                open(str(k) + '.jpg', 'wb').write(im.content)


downloadPic()
