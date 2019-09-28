# -*- coding:utf-8 -*-
'''

查询日志，身高，体重

'''

import argparse
import time

import datetime


from DbHelp import *



def caltime(date1,date2):
    '''
    返回两个日期之间的间隔天数
    :param date1:
    :param date2:
    :return:
    '''
    #%Y-%m-%d为日期格式，其中的-可以用其他代替或者不写，但是要统一，同理后面的时分秒也一样；可以只计算日期，不计算时间。
    #date1=time.strptime(date1,"%Y-%m-%d %H:%M:%S")
    #date2=time.strptime(date2,"%Y-%m-%d %H:%M:%S")
    date1=time.strptime(date1,"%Y-%m-%d")
    date2=time.strptime(date2,"%Y-%m-%d")
    #根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
    #date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
    #date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
    date1=datetime.datetime(date1[0],date1[1],date1[2])
    date2=datetime.datetime(date2[0],date2[1],date2[2])
    #返回两个变量相差的值，就是相差天数
    # print((date2-date1).days)#将天数转成int型
    return(date2-date1).days


def rtday(day):
    '''
    给出一个日期，计算经历了多上天
    :param day: datetime
    :return: srt
    '''
    baby = selectBaby()

    print(str(day))
    dl = str(day).split()

    time1 = str(baby['brithday'])
    time2 = dl[0]
    return caltime(time1,time2)

def selectBaby(id=1):
    '''
    返回baby的数据
    :param id:
    :return:
    '''
    sql = "SELECT * FROM bb_baby WHERE id={0}".format(id)
    # print(sql)
    with Db() as db:
        db.execute(sql)
        for i in db :
            # print(i['count(*)'])
            return i

def selectCount():
    '''

    :return: int 记录总条数
    '''
    sql = "select count(*) from bb_blog"
    # print(sql)
    with Db() as db:
        db.execute(sql)
        for i in db :
            # print(i['count(*)'])
            return i['count(*)']

def olddays():
    '''
    那年今天的历史数据打印
    :return:
    '''
    y = datetime.datetime.now().strftime("%Y")#现在的年份
    m = datetime.datetime.now().strftime("%m")#现在的月份
    d = datetime.datetime.now().strftime("%d")#现在的日期
    sql = "SELECT * from bb_blog WHERE month(create_time) ='{0}' and day(create_time) = '{1}' and year(create_time) != '{2}' " \
          "ORDER BY create_time;".format(m,d,y)

    # print(sql)
    print("那年今天>>>>")
    with Db() as db:
        m = db.execute(sql)
        if m :
            for i in db :
                print(i['id'],i['first'],i['language'],i['cognitive'],i['blog'],"宝贝已经出生"+str(rtday(i['create_time']))+"天")
        else:
            print("那年今天没有数据，不如今天为孩子添加一条数据吧：）")

def bloglist(k):
    '''
    日志列表


    :return:
    '''
    sql = ""
    if k <= 999:
        sql ="SELECT * FROM bb_blog ORDER by create_time DESC LIMIT {0}".format(k)
    else:
        sql = "SELECT * FROM bb_blog ORDER by create_time DESC"
    # print(sql)
    with Db() as db:
        db.execute(sql)
        for i in db :
            print(i['id'], i['first'], i['language'], i['cognitive'], i['blog'],
                  "宝贝已经出生" + str(rtday(i['create_time'])) + "天")
            print("")

def selectlist(k):
    '''

    搜索
    :return:
    '''
    sql = "SELECT * FROM bb_blog WHERE first like CONCAT('%{0}%') OR language like CONCAT('%{0}%')" \
          " or cognitive like CONCAT('%{0}%') or blog like CONCAT('%{0}%') ORDER BY create_time DESC".format(k)
    # print(sql)
    with Db() as db:
        db.execute(sql)
        for i in db :
            print(i['id'], i['first'], i['language'], i['cognitive'], i['blog'],
                  "宝贝已经出生" + str(rtday(i['create_time'])) + "天")
            print("")



def selecthw():
    '''
    身高体重数据
    :return:
    '''
    sql="select * from bb_healthy"

    with Db() as db:
        db.execute(sql)
        for i in db :
            print("{0}厘米  {1}公斤  宝贝已经出生{2}天".format(i['height'],i['weight'],rtday(i['create_time'])))

def home():
    baby = selectBaby()
    name = baby["name"]
    year = int(baby['brithday'].isocalendar()[0])  # 生日
    time1 = str(baby['brithday'])
    time2 = (str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day))

    age = int(datetime.datetime.now().strftime("%Y")) - year

    print("Name:{0}".format(name))
    print("出生于:{0}，年龄:{1}，您的孩子已经出生：{2}天了。 系统中共有{3}条关于杨瑞曦的记录。"
          .format(baby['brithday'], age, caltime(time1, time2), selectCount()))
    print("------------------------------------------")

    olddays()

def main():

    parser = argparse.ArgumentParser(prog="Select", description="查询babyblog数据，查询身高体重数据。")
    parser.add_argument("-l", "--list", help="请输入要查询数据的返回的条数。",type=int )
    parser.add_argument("-k", "--key", help="请输入要查询blog的关键字", default='')
    parser.add_argument("-hw", "--heightweight", help="返回孩子的身体数据",action="store_true")


    args = parser.parse_args()

    if args.key:
        selectlist(args.key)

    elif args.list:
        bloglist(args.list)
    elif args.heightweight:
        selecthw()

    else:
       home()







if __name__ == '__main__':
    main()