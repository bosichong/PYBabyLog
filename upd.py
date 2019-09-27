# -*- coding:utf-8 -*-

'''

终端更新数据数据

'''

import argparse

from DbHelp import *


def selectBlog(id):
    '''
    根据ID查询blog
    :param id: int
    :return: 一条记录
    '''
    sql = "SELECT * FROM bb_blog WHERE id = {0}".format(id)

    # print(sql)
    with Db() as db:
        db.execute(sql)
        return db


def updBlog(id,first='',language='',cognitive='',blog='',):
    '''
    更新日记
    :param id: int 日记ID
    :return: bool
    '''

    for i in selectBlog(id):
        rt = i
    f = first
    l = language
    c = cognitive
    b = blog
    update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if f == '':
        f = rt['first']
    if l == '':
        l = rt['language']
    if c == '':
        c = rt['cognitive']
    if b =='':
        b = rt['blog']

    sql = "UPDATE bb_blog SET first = '{0}',language = '{1}',cognitive = '{2}',blog = '{3}',update_time='{4}' WHERE id = {5}"\
        .format(f,l,c,b,update_time,id)
    print(sql)
    with Db() as db:
        try:
            # 执行sql语句
            db.execute(sql)
            print("数据更新成功！")
        except:
            print("数据更新失败！！")



# def selectHealthy(id):
#     '''
#     根据ID查询Healthy
#     :param id: int
#     :return: 一条记录
#     '''
#     sql = "SELECT * FROM bb_Healthy WHERE id = {0}".format(id)
#
#     # print(sql)
#     with Db() as db:
#         db.execute(sql)
#         return db
#
# def updtHealthy(id,height=0,weight=0):
#     '''
#
#     :param id:
#     :param height:
#     :param weight:
#     :return:
#     '''
#     for i in selectBlog(id):
#         rt = i
#     h = height
#     w = weight
#     if h == 0 :
#         h = rt['height']
#     if w == 0:
#         w = rt['weight']
#     sql = "UPDATE bb_healthy SET height={0}, weight={1}, WHERE id = {2}" \
#         .format(h,w, id)
#     print(sql)




def main():

    parser = argparse.ArgumentParser(prog="Update", description="更新babyblog数据，更新身高体重数据。")
    parser.add_argument("-bid", "--blogid", help="请输入需要更新blog的ID", )
    parser.add_argument("-f", "--first", help="请输入first数据", default='')
    parser.add_argument("-l", "--language", help="请输入language数据", default='')
    parser.add_argument("-c", "--cognitive", help="请输入cognitive数据", default='')
    parser.add_argument("-b", "--blog", help="请输入blog数据,此数据必填！",default='' )
    # parser.add_argument("-hid", "--healthyid", help="请输入healthy的ID",type=int )
    # parser.add_argument("-ht", "--height", help="填写身高厘米,身高体重必须同时填写。",type=int,)
    # parser.add_argument("-wt", "--weight", help="填写体重公斤，支持小数点后一位，身高体重必须同时填写。", type=float,)
    args = parser.parse_args()

    if args.blog or args.first or args.language or args.cognitive:
        # 更新孩子日记
        updBlog(args.blogid,first=args.first,language=args.language,cognitive=args.cognitive,blog=args.blog)

    else:
        print(parser.print_help())  # 默认打印帮助



if __name__ == '__main__':
    main()