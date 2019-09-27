# -*- coding:utf-8 -*-


'''

数据库连接封装类

'''
import pymysql
import datetime

class Db():
    def __init__(self, host='localhost', port=3306, db='mybaby', user='mybaby', passwd='mybaby20170606', charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor = pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()


if __name__ == '__main__':
    with Db() as db:
        try:
            # 执行sql语句
            db.execute('SELECT * FROM bb_blog LIMIT 10')
            print(db)
            for i in db:
                print(i)
        except:
            # 如果发生错误则回滚
            db.rollback()
            print("数据插入未成功！")


