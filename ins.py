# -*- coding:utf-8 -*-
'''

终端插入日志记录，身高，体重

'''


import argparse

from DbHelp import *


def insertBlog(first='', language='', cognitive='', blog=''):
    '''
    添加日志等数据
    blog 为必填项，其他可以为空

    :param first: 第一次
    :param language: 学会的语言
    :param cognitive: 认知
    :param blog: 日志
    :return: bool
    '''
    create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    baby_id = 1
    user_id = 1
    sql = "insert into bb_blog(first,language,cognitive,blog,create_time,update_time,baby_id,user_id) values('{0}','{1}','{2}','{3}','{4}','{5}',{6},{7})" \
        .format(first, language, cognitive, blog, create_time, update_time, baby_id, user_id)
    # print(sql)
    with Db() as db:
        try:
            # 执行sql语句
            db.execute(sql)
            # 提交到数据库执行
            print("数据添加成功！")
        except:
            # 如果发生错误则回滚
            # db.rollback()
            print("数据添加失败！！")


def insertHeightWeight(height,weight):
    '''
    添加孩子身高体重数据
    :param height: int 身高厘米
    :param weight: float 体重 公斤，保存小数点后一位即可
    :return: bool
    '''
    create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    baby_id = 1
    sql = "insert into bb_healthy(height, weight, create_time, baby_id) values('{0}','{1}','{2}','{3}')" \
        .format(height, weight, create_time, baby_id)
    # print(sql)
    with Db() as db:
        try:
            # 执行sql语句
            db.execute(sql)
            # 提交到数据库执行
            print("数据添加成功！")
        except:
            # 如果发生错误则回滚
            # db.rollback()
            print("数据添加失败！！")


def main():

    parser = argparse.ArgumentParser(prog="Insert", description="添加babyblog数据，添加身高体重数据。")
    parser.add_argument("-f", "--first", help="请输入first数据", default='')
    parser.add_argument("-l", "--language", help="请输入language数据", default='')
    parser.add_argument("-c", "--cognitive", help="请输入cognitive数据", default='')
    parser.add_argument("-b", "--blog", help="请输入blog数据,此数据必填！", )
    parser.add_argument("-ht", "--height", help="填写身高厘米,身高体重必须同时填写。",type=int)
    parser.add_argument("-wt", "--weight", help="填写体重公斤，支持小数点后一位，身高体重必须同时填写。", type=float)
    args = parser.parse_args()

    if args.blog:
        # 添加孩子日记
        insertBlog(first=args.first,language=args.language,cognitive=args.cognitive,blog=args.blog)
    elif args.height and args.weight:
        # 添加升高体重
        insertHeightWeight(args.height,args.weight)

    else:
        print(parser.print_help())  # 默认打印帮助


if __name__ == '__main__':
    main()
