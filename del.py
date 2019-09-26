# -*- coding:utf-8 -*-

'''

终端删除数据

'''

import argparse

from DbHelp import *

def delBlog(id):
    '''
    删除日记
    :param id: int 日记ID
    :return: bool
    '''

    sql = "delete FROM bb_blog WHERE id = {0}".format(id)
    # print(sql)
    with Db() as db:
        try:
            # 执行sql语句
            db.execute(sql)
            # 提交到数据库执行
            print("数据删除成功！")
        except:
            # 如果发生错误则回滚
            db.rollback()
            print("数据删除失败！！")


def selectBlog(id):
    '''
    根据ID查询blog
    :param id: int
    :return: str
    '''
    sql = "SELECT * FROM bb_blog WHERE id = {0}".format(id)

    # print(sql)
    with Db() as db:
        db.execute(sql)
        for i in db :
            print(i)




def delHealthy(id):
    '''
    删除日记
    :param id: int 日记ID
    :return:
    '''

    sql = "DELETE FROM bb_healthy WHERE id = {0}".format(id)
    # print(sql)
    with Db() as db:
        try:
            # 执行sql语句
            db.execute(sql)
            # 提交到数据库执行
            print("数据删除成功！")
        except:
            # 如果发生错误则回滚
            db.rollback()
            print("数据删除失败！！")


def selectHealthy(id):
    '''
    根据ID查询Healthy
    :param id: int
    :return: str
    '''
    sql = "SELECT * FROM bb_Healthy WHERE id = {0}".format(id)

    # print(sql)
    with Db() as db:
        db.execute(sql)
        for i in db :
            print(i)

def main():

    parser = argparse.ArgumentParser(prog="Insert", description="添加babyblog数据，添加身高体重数据。")
    parser.add_argument("-bid", "--blogid", help="请输入需要删除blog的ID",type=int )
    parser.add_argument("-hid", "--healthyid", help="请输入healthy的ID",type=int )
    args = parser.parse_args()

    if args.blogid:
        selectBlog(args.blogid)
        kk = input("确认删除上边的数据，请再次输入blog的ID:")

        if int(kk) == args.blogid:
            # 删除孩子日记
            delBlog(args.blogid)
        else:
            print("ID填写错误，请重新操作。")
    elif args.healthyid:
        selectHealthy(args.healthyid)
        kk = input("确认删除上边的数据，请再次输入healthy的ID:")

        if int(kk) == args.healthyid:
            # 删除孩子日记
            delHealthy(args.healthyid)
        else:
            print("ID填写错误，请重新操作。")

    else:
        print(parser.print_help())  # 默认打印帮助


if __name__ == '__main__':
    main()