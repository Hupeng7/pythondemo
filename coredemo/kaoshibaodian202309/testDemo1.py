

per_record = {
    "msg": "请求成功",
    "data": {
        "ReturnMessage": "取数据成功",
        "APPEName": "YLZP_HLX",
        "ImgAppEName": "YLZP_HLX",
        "GenDate": "Sat Sep 02 2023 12:54:50 GMT+0800 (China Standard Time)",
        "key": "adjqiweu1iu311jk1j23",
        "start_time": "2023-09-02 12:54:50:57",
        "end_time": "2023-09-02 12:54:50:57",
        "TestItems": [
            {
                "StyleID": 16,
                "Type": "ATEST",
                "Style": "A1型题",
                "SubType": "",
                "Score": 1,
                "AllTestID": 8433,
                "ChildTableID": -1,
                "SrcID": 1,
                "SbjID": 5,
                "CptID": 244,
                "Title": "d38d3961d5185987779d62fefebdafa691d05639bdf77ea9cf2f93dd4922714e80c7a94edc1d98e705a89c35022e5cbf067acde086b2d5bb1be691be06a11bed7add3f4dc3237c62",
                "Answer": "D",
                "Explain": "百白破混合剂应在第3个月注射，故不选A;麻疹疫苗第一次是在儿童8个月的时候，不选B;乙肝第二次在出生后第1个月，不选C;卡介苗出生后即注射，E也不选。正确答案为D。解题关键：按照我国卫生部的规定，婴儿须在出生后的第2、3、4个月分别注射脊髓灰质炎三价混合疫苗。",
                "TestPoint": "儿童计划免疫",
                "DealInfo": "",
                "OperateTime": "2023年5月05日",
                "pointData": [],
                "knowPoint": "",
                "material_content": "",
                "chapter_content": "",
                "isLNZT": 0,
                "IsFav": 0,
                "UserNoteContent": "",
                "SelectedItems": [
                    {
                        "HasImg": 1,
                        "ItemName": "A",
                        "Content": "百白破第一次"
                    },
                    {
                        "HasImg": 0,
                        "ItemName": "B",
                        "Content": "麻疹第一次"
                    },
                    {
                        "HasImg": 0,
                        "ItemName": "C",
                        "Content": "乙肝第二次"
                    },
                    {
                        "HasImg": 0,
                        "ItemName": "D",
                        "Content": "脊髓灰质炎第一次"
                    },
                    {
                        "HasImg": 0,
                        "ItemName": "E",
                        "Content": "卡介苗"
                    }
                ],
                "ReplyRate": 0.5584,
                "LevelRate": 0.4416
            }
        ],
        "climbing": {
            "forensics": False,
            "forAppID": False
        }
    },
    "status": 200
}

record = {'msg': '请求成功', 'data': {'data': [], 'msg': '无数据！', 'status': 201, 'climbing': {'forensics': False, 'forAppID': False}}, 'status': 200}

print(per_record['data']['ReturnMessage'])

# 获取 'ReturnMessage' 键的值，如果不存在则返回默认值 None
return_message = per_record['data']['TestItems'][0].get('SelectedItems')

# 检查是否成功获取了值
if return_message is not None:
    print(return_message)
else:
    print("键 'SelectedItems' 不存在或其值为 None")

#print(record['data']['ReturnMessage'] )


