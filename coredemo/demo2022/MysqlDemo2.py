# coding=utf-8

import pandas as pd
from sqlalchemy import create_engine
import pymysql
import mysql.connector
import time

# 用于datat项目定期删除数据
# 用于批量删除记录  create_time <= '2022-06-30 23:59:59'
# log_factor2_mobileicd_cache
# log_inout_mobile
# log_mobile

# db = pymysql.connect(host="localhost",
#                      port=3306,
#                      user="root",
#                      password="root",
#                      db="world",
#                      charset="utf8")
db = pymysql.connect(host="rm-uf6j9il9bg6k996a1.mysql.rds.aliyuncs.com",
                     port=3306,
                     user="datat_qa_user",
                     password="ZE&NgYeq8$",
                     db="datat",
                     charset="utf8")

cursor = db.cursor()

###  先备份！！！
table_name = 'datat.`log_mobile`'
create_time = "'2023-06-30 23:59:59'"
delete_count = 5000
# explain delete from datat.log_mobile where create_time<= '2022-09-08 23:59:59' limit 5000;
# EXPLAIN select id from datat.log_mobile where create_time <= '2022-09-08 23:59:59' limit 1;
#
# 想要提升性能需要添加关于create_time的索引
# explain delete from datat.log_inout_mobile where create_time<= '2022-09-08 23:59:59' limit 5000;
# EXPLAIN select id from datat.log_inout_mobile where create_time <= '2022-09-08 23:59:59' limit 1;
#
# explain delete from datat.log_factor2_mobileicd_cache where create_time<= '2022-09-08 23:59:59' limit 5000;
# EXPLAIN select id from datat.log_factor2_mobileicd_cache where create_time <= '2022-09-08 23:59:59' limit 1;

delete_sql = "delete from %s where create_time<= %s limit %s" % (table_name,create_time,delete_count)
query_sql = "select id from %s where create_time <= %s limit 1 " % (table_name,create_time)


def delete_expired_data(delete_count):
    c = 1
    start = time.time()
    print("start: ", start)
    # print(query_sql)
    # print(delete_sql)
    try:
        df = cursor.execute(query_sql)
        db.commit()
        print("df1111: ", df)
        while True:
            print("df2222: ", df)
            if df is None or (df == 0):
                break
            ret = cursor.execute(delete_sql)
            print("ret: ", ret)
            print("done c : ", c)
            if ret == delete_count:
                print("已删除记录 : ", (ret * c))
            else:
                print("已删除记录 ： ", ((c - 1) * delete_count + ret))
            db.commit()
            c += 1

            df = cursor.execute(query_sql)
            db.commit()
            print("df3333: ", df)
        end = time.time()
        print("end: ", end)
        print("耗时：", (end - start))
    except RuntimeError as err:
        print("error:", err)
    finally:
        cursor.close()
        db.close()


delete_expired_data(delete_count)
