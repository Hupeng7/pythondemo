#!/usr/bin/python3

import requests
import json
import random
from decimal import Decimal, getcontext
import time

# 测试不对 生成精度超过23位的数据
def random_decimal():
    # 设置Decimal精度，保留小数点后23位
    getcontext().prec = 25  # 23位小数 + 2位整数部分
    # 生成0到1之间的随机小数
    random_decimal = Decimal(random.random())
    print("随机小数:", random_decimal)
    return random_decimal


def random_number():
    # 生成1000到9999之间的随机数
    random_number = random.randint(5000, 9999)
    print("随机数:", random_number)
    return random_number


# 目标API的URL
# url = 'https://example.com/api'  # 替换成实际的API URL
getchatpterExx_url = 'https://slb-exam.ksbao.com/api/exam/getChapterExx?_u=504166096'

# 要发送的参数（以字典形式）
getchatpterExx_request_data = {
    'appID': 16742,
    'guid': 'dm8qMrnVae8Evu2v9mq3EjXec2A9blJq504166096',
    'queryTestInfo': 1,
    'cptID': 249,
    'isCheckShare': 1,
    'siginName': 1,
    'isDealTitle': 1,
    'authority': 'https://slb-exam.ksbao.com',
    'clientType': 1,
    'validate': 'undefined',
    'client': 'pc',
    'clientver': 'wide.ksbao.com',
    'v': 0.27641767787929911768432,
    'terminalType': 4
}

getChapterTestOne_url = 'https://slb-exam.ksbao.com/api/exam/getChapterTestOne'

# 定义请求参数
getChapterTestOne_request_params = {
    "_u": "504166096",
    "appID": "16742",
    "guid": "dm8qMrnVae8Evu2v9mq3EjXec2A9blJq504166096",
    "idArray": '[{"AllTestID":23408,"ChildTableID":-1}]',
    "isDealTitle": "1",
    "cptID": "19",
    "inrTime": "5423",
    "testCounts": "2",
    "authority": "https://slb-exam.ksbao.com",
    "clientType": "1",
    "validate": "undefined",
    "client": "pc",
    "clientver": "wide.ksbao.com",
    "v": "0.83687784782493285938937",
    "terminalType": "4"
}

# 发送POST请求
getchatpterExx_response = requests.post(getchatpterExx_url, json=getchatpterExx_request_data)

def getchatpterExxRequest(cptID):
    getchatpterExx_request_data['cptID'] = cptID
    getchatpterExx_response = requests.post(getchatpterExx_url, json=getchatpterExx_request_data)

    try:
        if getchatpterExx_response.status_code == 200:
            # 解析JSON响应
            getchatpterExx_response = getchatpterExx_response.json()
            print("响应数据：", getchatpterExx_response)
            return getchatpterExx_response
        else:
            print("请求失败，状态码：", getchatpterExx_response.status_code)
            return ""
    except requests.HTTPError as error:
        print(f"失败: {error}")
        return ""


def getChapterTestOneRequest(AllTestID):
    # 字符串转py对象
    idArray = json.loads(getChapterTestOne_request_params['idArray'])[0]

    # 重新赋值
    idArray["AllTestID"] = AllTestID

    # py对象转字符串
    getChapterTestOne_request_params['idArray'] = json.dumps([idArray])

    getChapterTestOne_request_params['inrTime'] = random_number()

    # getChapterTestOne_request_data['v'] = random_decimal()
    print("getChapterTestOne_request_data-2:", getChapterTestOne_request_params)
    getChapterTestOne_response = requests.post(getChapterTestOne_url, data=getChapterTestOne_request_params)
    if getChapterTestOne_response.status_code == 200:
        # 解析JSON响应
        getChapterTestOne_response = getChapterTestOne_response.json()
        print("getChapterTestOne_response响应数据：", getChapterTestOne_response)
        return getChapterTestOne_response
    else:
        print("请求失败，状态码：", getChapterTestOne_response.status_code)
        return ""


# 检查响应是否成功
# if getchatpterExx_response.status_code == 200:
#     all_test_id_list = []
#
#     # 解析JSON响应
#     getchatpterExx_response = getchatpterExx_response.json()
#     print("响应数据：", getchatpterExx_response)
#
#     id_arr_list = getchatpterExx_response['data']['IDArr']
#     print("id_arr_list:", id_arr_list)
#
#     # 现获取每一章节下的试题id:AllTestID
#     for i in range(len(id_arr_list)):
#         print("getChapterTestOne_request_data-1:", getChapterTestOne_request_params)
#
#         item = id_arr_list[i]
#         cur_AllTestID = item['AllTestID']
#         print("cur_AllTestID:", cur_AllTestID)
#
#         # 字符串转py对象
#         idArray = json.loads(getChapterTestOne_request_params['idArray'])[0]
#         AllTestID = idArray["AllTestID"]
#
#         # 重新赋值
#         idArray["AllTestID"] = cur_AllTestID
#         # py对象转字符串
#         getChapterTestOne_request_params['idArray'] = json.dumps([idArray])
#
#         getChapterTestOne_request_params['inrTime'] = random_number()
#
#         # getChapterTestOne_request_data['v'] = random_decimal()
#         print("getChapterTestOne_request_data-2:", getChapterTestOne_request_params)
#         getChapterTestOne_response = requests.post(getChapterTestOne_url, data=getChapterTestOne_request_params)
#         if getChapterTestOne_response.status_code == 200:
#             # 解析JSON响应
#             getChapterTestOne_response = getChapterTestOne_response.json()
#             print("getChapterTestOne_response响应数据：", getChapterTestOne_response)
#         else:
#             print("请求失败，状态码：", getChapterTestOne_response.status_code)
#         time.sleep(1)
#
#         # all_test_id_list.append(cur_AllTestID)
#     print("all_test_id_list length:", len(all_test_id_list))
#     print("all_test_id_list:", all_test_id_list)
# else:
#     print("请求失败，状态码：", getchatpterExx_response.status_code)
