__author__ = 'Administrator'
#!/usr/bin/python
# -*- coding:utf8 -*-

import os
allFileNum = 0


def print_path(path):

    global allFileNum
    '''
    打印一个目录下的所有文件夹和文件
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dir_list = []
    # 所有文件
    file_list = []

    all_files = []
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(path)

    for f in files:
        # print(f)
        if os.path.isdir(path + '/' + f):
            # 排除隐藏文件夹。因为隐藏文件夹过多
            if f[0] == '.':
                pass
            else:
                # print('!!!!!!'+f+'!!!!')
                # 添加非隐藏文件夹
                dir_list.append(f)
        if os.path.isfile(path + '/' + f):
            # 添加文件

            file_list.append(f)
    # 当一个标志使用，文件夹列表第一个级别不打印

    for dl in dir_list:
            # 打印至控制台，不是第一个的目录
            # print(path + '/', dl)
            # 打印目录下的所有文件夹和文件，目录级别+1
            # print(path + '/' + dl)
            all_files_temp = print_path(path + '/' + dl)
            for fl in all_files_temp:
                all_files.append(fl.strip())
    for fl in file_list:
        # 打印文件
        all_files.append(str(path.strip() + '/' + fl.strip()))
        # 随便计算一下有多少个文件
        allFileNum += 1
    return all_files

if __name__ == '__main__':
    all_files = print_path('G:/music')
    for file in all_files:
        print(file)
    print('总文件数 =', allFileNum)
