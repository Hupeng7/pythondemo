# coding=utf8
import requests
import json
import bs4
import re
import time
import sys
import csv
import os
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util import Retry

reload(sys)
sys.setdefaultencoding('utf8')

domain = 'http://222.76.242.144:8081/'
req = requests.session()
req.keep_alive = False
req.mount('http://', HTTPAdapter(max_retries=Retry(total=3,
                                                   method_whitelist=frozenset(['GET', 'POST']))))
requesttimeout = 30
header = {'Connection': 'close'}


def getIDandNamefromNumber(number):
    print('number:' + number)
    postdata = {'currentpage': '1', 'pagesize': '20',
                'searchtj': ' and YSXKZH like  ' + number}
    ret = req.post(domain + 'home/Getzslp',
                   data=postdata, timeout=requesttimeout, headers=header)
    ret.close()
    if ret.status_code == 200:
        obj = json.loads(ret.text)
        if obj['result'] == 1:
            body = json.loads(obj['Body'])
            data = body['bodylist']
            for item in data:
                print(item)
                if item['YSXKZH'] == number:
                    return item['TRANSACTION_ID'], item['XMMC']
        else:
            print('查询失败:' + ret.text)
            return
    else:
        print('http错误，代码' + str(ret.status_code))
        return
    print('未找到' + number + ret.text)
    return


def getLoupanfromIDandName(ID, name):
    payload = {'transactionid': ID, 'projectName': name}
    ret = req.get(domain + 'LP/Index', params=payload,
                  timeout=requesttimeout, headers=header)
    ret.close()
    if ret.status_code == 200:
        soup = bs4.BeautifulSoup(ret.text, features='lxml')
        sxmmcids = (soup.select('#sxmmc'))
        if (len(sxmmcids) < 0):
            print('未找到楼盘' + name)
            return
        else:
            loupanname = sxmmcids[0].text
            list = sxmmcids[0].parent
            loudonglist = []
            loupanobj = {}
            loupanobj['loupanname'] = loupanname
            loupanobj['loudonglist'] = []
            for item in list.select('li>ul>li>.folder'):
                loudonglist.append(item.text)
                loudongobj = {}
                loudongobj['name'] = item.text
                loudongobj['list'] = []
                for f in item.parent.select('.file'):
                    href = f.parent['href']
                    pattern = '^javascript:DispLp\\((-?[0-9]+),(-?[0-9]+),(-?[0-9]+)\\)$'
                    groups = re.match(pattern, href)
                    count = len(groups.groups())
                    if count != 3:
                        print('未找到楼栋' + item.text)
                        return
                    data = {'type': f.text, 'BuildID': groups.group(
                        1), 'NAID': groups.group(2), 'lotid': groups.group(3)}
                    loudongobj['list'].append(data)
                loupanobj['loudonglist'].append(loudongobj)
            return loupanobj
    else:
        print('http错误，代码' + str(ret.status_code))
        return


def getHousesofLoudong(house):
    t = int(round(time.time() * 1000))
    payload = {'BuildID': house['BuildID'],
               'NAID': house['NAID'], 'lotid': house['lotid'], 't': t}
    ret = req.post(domain + 'Lp/LPPartial',
                   data=payload, timeout=requesttimeout, headers=header)
    ret.close()
    if ret.status_code == 200:
        soup = bs4.BeautifulSoup(ret.text, features='lxml')
        floors = soup.select('.th_class')
        housesobj = []
        for floor in floors:
            floorobj = {}
            floorobj['name'] = floor.text.strip()
            floorobj['list'] = []
            for house in floor.parent.select('.hand'):
                id = house.get('id')
                zt = 0 if house.get('class') == 'fw_bksfw' else 1
                yyxx = house['tipmsg'] if house.has_attr(
                    'tipmsg') else 'undefined'
                zs = house['hzsstate'] if house.has_attr(
                    'hzsstate') else 'undefined'
                room = house.text
                floorobj['list'].append(
                    {'id': id, 'zt': zt, 'yyxx': yyxx, 'zs': zs, 'room': room.strip()})
            housesobj.append(floorobj)
        return housesobj
    else:
        print('http错误，代码' + str(ret.status_code))
        return


def getDetailofHouse(house):
    payload = {'HouseId': house['id'], 'zt': house['zt'],
               'yyxx': house['yyxx'], 'zs': house['zs']}
    ret = req.get(domain + 'LP/Fwztxx', params=payload,
                  timeout=requesttimeout, headers=header)
    ret.close()
    if ret.status_code == 200:
        soup = bs4.BeautifulSoup(ret.text, features='lxml')
        table = soup.table
        houseobj = {}
        for tr in table.select('tr'):
            tds = tr.select('td')
            if len(tds) != 2:
                print('详细信息有误')
                return
            else:
                houseobj[tds[0].text] = tds[1].text
        return houseobj
    else:
        print('http错误，代码' + str(ret.status_code))
        return


if __name__ == "__main__":
    basedir = os.path.dirname(os.path.abspath(sys.argv[0]))
    # if len(sys.argv) == 1:
    #     number = input('输入预售证号：')
    # else:
    #     number = sys.argv[1]
    # number.strip()
    # print('预售证号：' + number)
    number = str(20200001)
    transactionid, projectname = getIDandNamefromNumber(number)
    print('项目名称：' + projectname)
    loupanobj = getLoupanfromIDandName(transactionid, projectname)
    print('楼盘名称：' + loupanobj['loupanname'])
    filename = number + '_' + projectname + '.csv'
    # f = open(basedir + '/' + filename, 'w', encoding='utf-8-sig', newline='')
    f = open(basedir + '/' + filename, 'w')
    headers = ['坐落', '室号', '性质', '用途', '拟售价格',
               '', '面积', '', '销售状态', '权属状态', '楼栋', '']
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    for loudongobj in loupanobj['loudonglist']:
        print('加载楼栋：' + loudongobj['name'])
        for type in loudongobj['list']:
            print('\t加载' + type['type'])
            housesobj = getHousesofLoudong(type)
            for floor in housesobj:
                print('\t\t加载楼层：' + floor['name'])
                time.sleep(0.1)
                houses = floor['list']
                for house in houses:
                    print('\t\t\t加载室：' + house['room'])
                    detail = getDetailofHouse(house)
                    price, price_unit = str(detail['拟售价格']).split(
                        ' ') if '拟售价格' in detail else [None, None]
                    area, area_unit = str(detail['面积']).split(
                        ' ') if '面积' in detail else [None, None]
                    row = [detail.get('坐落'),
                           detail.get('室号'),
                           detail.get('性质'),
                           detail.get('用途'),
                           price,
                           price_unit,
                           area,
                           area_unit,
                           detail.get('销售状态'),
                           detail.get('权属状态'),
                           loudongobj['name'],
                           type['type']]
                    f_csv.writerow(row)
                    print('\t\t\t已加载室：' + house['room'])
                print('\t\t已加载楼层：' + floor['name'])
            print('\t已加载' + type['type'])
        print('已加载楼栋：' + loudongobj['name'])
    f.close()
    print(basedir + '/' + filename + ' 写入完成')
    if os.name == 'nt':
        os.system('pause')
    else:
        print('请按任意键继续. . .')
        os.system('read -n 1')
