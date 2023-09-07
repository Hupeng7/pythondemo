#!/usr/bin/python3

"""
需求：将题库中的题目down下来，然后生成一个word文件。
1.首先需要获取对应章节的所有题目的【AllTestID】，

请求一：根据AllTestID请求题目详情
https://slb-exam.ksbao.com/api/exam/getChapterTestOne?_u=504166096&appID=16742&guid=FpBKd7WnmQGDSVT47WWBfPeKVVCzfzQ6504166096&idArray=[{"AllTestID":8433,"ChildTableID":-1}]&isDealTitle=1&cptID=244&inrTime=247212&testCounts=8&authority=https://slb-exam.ksbao.com&clientType=1&validate=undefined&client=pc&clientver=wide.ksbao.com&v=0.468491005885313026088957208728191&terminalType=4

返回值：
{
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
            "forensics": false,
            "forAppID": false
        }
    },
    "status": 200
}
数据库落库TestItems里面的内容，其中Title要解密

2.落库完成后，读取数据库里的内容，写入一个word文件。

"""

import binascii
import json
import random
import time

import pymysql
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


# 字符串转换与十六进制字符串互转
# 将普通字符串转换为十六进制字符串
# normal_string = "Hello, 你好世界！"
# hex_string = binascii.hexlify(normal_string.encode('utf-8')).decode('utf-8')
# print("普通字符串转换为十六进制字符串:", hex_string)
#
# 将十六进制字符串转换为普通字符串
# hex_string = "48656c6c6f2c20e4bda0e5a5bde4b896e4b8adefbc81"
# normal_string = binascii.unhexlify(hex_string).decode('utf-8')
# print("十六进制字符串转换为普通字符串:", normal_string)

def string2hex(normal_string):
    hex_string = binascii.hexlify(normal_string.encode('utf-8')).decode('utf-8')
    print("普通字符串转换为十六进制字符串：", hex_string)
    return hex_string


def hex2string(hex_string):
    normal_string = binascii.unhexlify(hex_string)
    print("十六进制字符串转换为普通字符串:", normal_string)
    return normal_string

# des加密
def encrypt_des(plaintext, key, iv, mode, padding):
    # 创建一个DES加密器对象
    cipher = DES.new(key, mode, iv)

    # 对明文进行填充
    plaintext = pad(plaintext.encode('utf-8'), DES.block_size)

    # 加密数据
    ciphertext = cipher.encrypt(plaintext)

    return ciphertext

# des解密
def decrypt_des(ciphertext, key, iv, mode, padding):
    # 创建一个DES加密器对象
    cipher = DES.new(key, mode, iv)

    # 解密数据
    plaintext = cipher.decrypt(ciphertext)

    # 去除填充
    plaintext = unpad(plaintext, DES.block_size)

    return plaintext.decode('utf-8')


# 专门解密title字段，解密为明文，iv取“daqjwiuei13u11kjj132”前8位 b"daqjwiue"
def decrypt_des_title(ciphertext):
    key = b"daqjwiue"
    iv = key  # 这里使用16字节的IV
    normal_string = hex2string(ciphertext)

    # 创建一个DES加密器对象 key和iv使用同一个，mode是CBC
    cipher = DES.new(key, DES.MODE_CBC, iv)

    # 解密数据
    plaintext = cipher.decrypt(normal_string)

    # 去除填充
    plaintext = unpad(plaintext, DES.block_size)

    return plaintext.decode('utf-8')


db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="root",
                     db="bigdata",
                     charset="utf8")
cursor = db.cursor()

table_name = 'bigdata.`test_record`'
create_time = "'2023-06-30 23:59:59'"
query_sql = "select * from %s where create_time >= %s limit 1" % (table_name, create_time)

# 定义要插入的数据
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

# 使用参数化查询来插入数据，这样可以防止SQL注入攻击
insert_query = "INSERT INTO bigdata.`test_record`  (`app_e_name`, `img_app_e_name`, `key_iv`, `test_items`, `style_id`, `type`, `style`, `sub_type`, `score`, `all_test_id`, `child_table_id`, `src_id`, `sbj_id`, `cpt_id`, `title`,`title_de`,`answer`, `test_explain`, `test_point`, `deal_info`, `operate_time`, `point_data`, `know_point`, `material_content`, `chapter_content`, `is_lnzt`, `is_fav`, `user_note_content`,`selected_items`) VALUES( %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "

data = per_record['data']
print("data:", data)
print("TestItems", data["TestItems"][0])
print("StyleID", data["TestItems"][0]["StyleID"])

# 将 ensure_ascii 参数设置为 False，确保非ASCII字符以原始形式存储
# json_data = json.dumps(data, ensure_ascii=False)

TestItems = json.dumps(data["TestItems"], ensure_ascii=False)
# TestItems = data["TestItems"]
pointData = json.dumps(data["TestItems"][0]["pointData"], ensure_ascii=False)
SelectedItems = json.dumps(data["TestItems"][0]["SelectedItems"], ensure_ascii=False)
Title = data["TestItems"][0]["Title"]
# print("title:",Title)
Title_de = decrypt_des_title(Title)

values = (data["APPEName"], data["ImgAppEName"], data["key"], TestItems,
          data["TestItems"][0]["StyleID"], data["TestItems"][0]["Type"],
          data["TestItems"][0]["Style"], data["TestItems"][0]["SubType"],
          data["TestItems"][0]["Score"], data["TestItems"][0]["AllTestID"],
          data["TestItems"][0]["ChildTableID"], data["TestItems"][0]["SrcID"],
          data["TestItems"][0]["SbjID"], data["TestItems"][0]["CptID"],
          data["TestItems"][0]["Title"], Title_de, data["TestItems"][0]["Answer"],
          data["TestItems"][0]["Explain"], data["TestItems"][0]["TestPoint"],
          data["TestItems"][0]["DealInfo"], data["TestItems"][0]["OperateTime"],

          pointData, data["TestItems"][0]["knowPoint"],
          data["TestItems"][0]["material_content"], data["TestItems"][0]["chapter_content"],
          data["TestItems"][0]["isLNZT"], data["TestItems"][0]["IsFav"],
          data["TestItems"][0]["UserNoteContent"], SelectedItems
          )

# 使用批量插入来插入多条数据，这可以减少与数据库的交互次数
# insert_query = "INSERT INTO your_table (name, age, city) VALUES (%s, %s, %s)"
# values = [(item["name"], item["age"], item["city"]) for item in data_to_insert]

# 7已跑
CptID_list = [
    # 7,8, 9, 10, 11, 12, 13, 14, 19,20, 21, 34, 38,
    38, 39, 40, 41, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
    95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
    117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 132, 133, 134, 135, 136, 137, 138,
    139, 140, 141, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160,
    161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181,
    182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202,
    203, 204, 205, 206, 207, 208, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 222, 223, 224, 225,
    226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246,
    247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267,
    268, 269, 270, 271, 272, 273, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 319, 320, 321,
    322, 323, 324, 325, 326, 327, 328, 332, 339, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352,
    353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363]

CptID_list1 = [19]
import httpDemo

# 生成一个随机的浮点数，范围在0.5到1.5之间
random_sleep_number = random.uniform(0, 2)

def save_test_record():
    count = 1
    start = time.time()
    print("start: ", start)
    try:
        cpt_len = len(CptID_list)
        for i in range(cpt_len):
            cur_CptID = CptID_list[i]
            print("CptID===>:", cur_CptID)
            count += 1
            print("已执行次数：", count)

            getchatpterExx_response = httpDemo.getchatpterExxRequest(cur_CptID)
            print("getchatpterExx_response:", getchatpterExx_response)

            id_arr_list = getchatpterExx_response['data']['IDArr']
            print("id_arr_list:", id_arr_list)
            id_arr_list_len = len(id_arr_list)
            # 现获取每一章节下的试题id:AllTestID
            for j in range(id_arr_list_len):
                start_per = time.time()
                print("start_per: ", start_per)

                item = id_arr_list[j]
                cur_AllTestID = item['AllTestID']
                getChapterTestOne_response = httpDemo.getChapterTestOneRequest(cur_AllTestID)

                if len(getChapterTestOne_response) > 0:
                    data = getChapterTestOne_response['data']

                    # 获取 'ReturnMessage' 键的值，如果不存在则返回默认值 None
                    return_message = data.get('ReturnMessage')

                    # 检查是否成功获取了值
                    if return_message is None:
                        print("键 'ReturnMessage' 不存在或其值为 None")
                        continue

                    # if data['ReturnMessage'] != '取数据成功':
                    #     continue

                    TestItems = json.dumps(data["TestItems"], ensure_ascii=False)
                    pointData = json.dumps(data["TestItems"][0]["pointData"], ensure_ascii=False)

                    SelectedItems = data['TestItems'][0].get('SelectedItems')
                    if SelectedItems is not None:
                        SelectedItems = json.dumps(data["TestItems"][0]["SelectedItems"], ensure_ascii=False)
                    else:
                        SelectedItems = ""

                    Title = data["TestItems"][0]["Title"]
                    Title_de = decrypt_des_title(Title)
                    insert_values = (data["APPEName"], data["ImgAppEName"], data["key"], TestItems,
                                     data["TestItems"][0]["StyleID"], data["TestItems"][0]["Type"],
                                     data["TestItems"][0]["Style"], data["TestItems"][0]["SubType"],
                                     data["TestItems"][0]["Score"], data["TestItems"][0]["AllTestID"],
                                     data["TestItems"][0]["ChildTableID"], data["TestItems"][0]["SrcID"],
                                     data["TestItems"][0]["SbjID"], data["TestItems"][0]["CptID"],
                                     data["TestItems"][0]["Title"], Title_de, data["TestItems"][0]["Answer"],
                                     data["TestItems"][0]["Explain"], data["TestItems"][0]["TestPoint"],
                                     data["TestItems"][0]["DealInfo"], data["TestItems"][0]["OperateTime"],

                                     pointData, data["TestItems"][0]["knowPoint"],
                                     data["TestItems"][0]["material_content"], data["TestItems"][0]["chapter_content"],
                                     data["TestItems"][0]["isLNZT"], data["TestItems"][0]["IsFav"],
                                     data["TestItems"][0]["UserNoteContent"], SelectedItems
                                     )
                    try:
                        # 执行插入操作
                        cursor.execute(insert_query, insert_values)

                        print("总章数：", cpt_len, "cur_CptID：", cur_CptID, "本章总试题数：", id_arr_list_len, "已插入数据：", j + 1)
                        time.sleep(1)

                        # 提交更改
                        db.commit()
                    except cursor.Error as error:
                        print(f"插入数据失败: {error}")
                        pass

                    end_per = time.time()
                    print("end_per: ", end_per)
                    print("每条耗时耗时：", (end_per - start_per))
                else:
                    print("getChapterTestOne_response为空")

        # 执行插入操作
        # cursor.execute(insert_query, values)

        # 执行批量插入操作
        # cursor.executemany(insert_query, values)

        # 查询
        # cursor.execute(query_sql)

        end = time.time()
        print("end: ", end)
        print("总耗时：", (end - start))

        # 获取查询结果（一条记录）
        # result = cursor.fetchone()
        #
        # if result:
        #     # 打印查询结果
        #     print("查询结果:")
        #     print(result)
        # else:
        #     print("未找到匹配的记录。")

    except RuntimeError as err:
        print("error:", err)
    finally:
        cursor.close()
        db.close()


# import random
# import numpy as np
# from decimal import Decimal, getcontext
#
# # 设置Decimal精度，保留小数点后23位
# getcontext().prec = 25  # 23位小数 + 2位整数部分
#
# # 使用random库生成一个随机浮点数
# random_float = random.uniform(0, 1)
#
# # 将随机浮点数转换为Decimal对象
# random_decimal = Decimal(str(random_float))
#
# # 使用NumPy生成一个高精度的随机浮点数，保留小数点后23位
# random_float128 = np.float128(np.random.rand())
#
# print("随机浮点数（random库）:", random_float)
# print("随机浮点数（NumPy库）:", random_float128)
# print("随机小数（decimal库）:", random_decimal)

if __name__ == "__main__":
    # 替换为你的8字节密钥和IV
    # key = b"mykey123"  # 这里使用8字节的密钥
    key = b"daqjwiue"  # 这里使用8字节的密钥  daqjwiuei13u11kjj132 前八位
    iv = key  # 这里使用16字节的IV

    # 明文
    plaintext = "新生儿2个月，按预防接种计划应接种的疫苗是。"

    # 加密
    # ciphertext = encrypt_des(plaintext, key, iv, DES.MODE_CBC, "PKCS7")
    # # 打印密文
    # print("Encrypted Data:", ciphertext)
    #
    # hex_str = "48656c6c6f20576f726c64"
    # byte_str = bytes.fromhex(hex_str)
    # str_result = byte_str.decode("utf-8")
    # print(str_result)  # 输出：Hello World
    #
    # b = binascii.unhexlify(ciphertext).decode('utf-8')
    # # 打印密文
    # print("Encrypted Data bbbbbb:", b)

    # 密文
    ciphertext = "d38d3961d5185987779d62fefebdafa691d05639bdf77ea9cf2f93dd4922714e80c7a94edc1d98e705a89c35022e5cbf067acde086b2d5bb1be691be06a11bed7add3f4dc3237c62"
    # ciphertext ="48656c6c6f2c20e4bda0e5a5bde4b896e4b8adefbc81"
    normal_string = binascii.unhexlify(ciphertext)
    # a = binascii.hexlify(ciphertext.encode('utf-8')).decode('utf-8')
    # 解密
    # decrypted_data = decrypt_des(normal_string, key, iv, DES.MODE_CBC, "PKCS7")

    # 打印解密后的数据
    # print("Decrypted Data:", decrypted_data)

    save_test_record()
