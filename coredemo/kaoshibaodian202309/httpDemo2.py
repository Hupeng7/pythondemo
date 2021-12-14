#!/usr/bin/python3

import json

# 定义请求URL  根据AllTestID获取试题详情
url = "https://slb-exam.ksbao.com/api/exam/getChapterTestOne"

# 定义请求参数
params = {
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

list = [1, 5, 100]

for i in range(4):
    cur = params['idArray']
    print("cur-1:", cur)  # [{"AllTestID":23408,"ChildTableID":-1}]

    # 字符串转py对象
    idArray = json.loads(cur)[0]
    print("idArray:", idArray)  # idArray: {'AllTestID': 23408, 'ChildTableID': -1}

    AllTestID = idArray["AllTestID"]
    print("AllTestID-1:", AllTestID)  # 23408

    print("list[i]:", list[i])  # 5

    # 重新赋值
    idArray["AllTestID"] = list[i]
    print("AllTestID-2:", idArray["AllTestID"])

    print("idArray-2:", idArray)

    # py对象转字符串 并赋值
    params['idArray'] = json.dumps([idArray])
    print("cur-2:", cur)

    print("params:", params)

# 发送POST请求
# response = requests.post(url, data=params)
#
# # 处理响应
# if response.status_code == 200:
#     print("请求成功！")
#     print(response.text)
# else:
#     print(f"请求失败，状态码：{response.status_code}")
#     print(response.text)
