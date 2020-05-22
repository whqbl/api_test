# -- coding:utf-8 --
"""
@author: wangh
@file:
@time: 
@desc:
"""

import pymysql
import sys
from config.config import *
sys.path.append('..') # 提升一级到项目更目录下

# 连接数据库
def get_db_conn():
    conn = pymysql.connect(host=db_host,
                           port=db_port,
                           user=db_user,
                           passwd=db_passwd,
                           db=db_name,
                           charset='utf8')
    return conn


# 封装查询操作
def query_db(sql):
    logging.debug(sql)
    conn = get_db_conn() # 连接数据库
    cur = conn.cursor() # 建立游标
    cur.execute(sql) # 执行sql
    conn.commit() # 提交事务
    result = cur.fetchall()
    logging.debug(result)
    cur.close() # 关闭游标
    conn.close() # 关闭连接
    return result

# 封装更改数据库操作
def change_db(sql):
    logging.debug(sql)
    conn = get_db_conn()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback() # 回滚
        logging.error(str(e))
    finally:
        cur.close()
        conn.close()


# 检查用户是否存在
def check_user(mobile):
    # 注意sql中''号嵌套的问题
    sql = "select * from general_user where mobile='{}'".format(mobile)
    result = query_db(sql)
    return True if result else False
