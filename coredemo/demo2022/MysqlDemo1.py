import mysql.connector

# 组装数据库连接参数
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="world"
)

print(mydb)

mycursor = mydb.cursor()
print("show databases============>")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

print("show tables============>")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

print("查询数据============>")
mycursor.execute("select * from log_mobile_a limit 5")

print("查询数据 取第一条============>")
myresult = mycursor.fetchone()
print(myresult)

print("查询数据 取所有============>")
# 只会取到4条  有一条上面已经取出
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# 为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义查询的条件
sql = "select * from log_mobile_a where create_time >= %s limit 5"
param = ("2022-04-05",)

print("查询数据 取所有 加参数============>")
mycursor.execute(sql,param)
myresult1 = mycursor.fetchall()
for x in myresult1:
    print(x)

print("删除数据 ============>")
sql1 = "delete from log_mobile_a where id = %s"
param1 = ("3925148",)
mycursor.execute(sql1,param1)
mydb.commit()
print(mycursor.rowcount," 条记录删除")
