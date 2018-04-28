#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
import Public.command as cmd
from logzero import logger
import time
import zipfile
import os


def pull_js(dst='../GT_Report/data/data.js'):
    '''将手机内的data.js复制到电脑'''
    if 'data' in cmd.adb_shell('ls /sdcard/GTRData/'):
        logger.info('Starting to pull data.js to %s ' % os.path.abspath(dst))
        cmd.pull('/sdcard/GTRData/data.js', dst)
        logger.info('Pull data.js success')
        return True
    else:
        logger.error('There is no data.js in /sdcard/GTRData/!  Please check out!')
        return False


def pull_monkeylog():
    if 'monkeyerr.txt' in cmd.adb_shell('ls /sdcard/') and 'monkeyout.txt' in cmd.adb_shell('ls /sdcard/'):
        cmd.pull('/sdcard/monkeyerr.txt', '../GT_Report/monkeyerr.txt')
        cmd.pull('/sdcard/monkeyout.txt', '../GT_Report/monkeyout.txt')
        logger.info('pull monkeyerr.txt  monkeyout.txt  ---> /GT_Report/')
        return True
    else:
        logger.error('There is monkeyelog file,Please check out!')
        return False


def zip_report(name):
    startdir = "../GT_Report"  # 要压缩的文件夹路径
    file_news = '../'+ name + '.zip'  # 压缩后文件夹的名字
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)  # 参数一：文件夹名
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')  # 这一句很重要，不replace的话，就从根目录开始复制
        fpath = fpath and fpath + os.sep or ''  # 这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
            # z.write(os.path.join(dirpath, filename))
    z.close()
    logger.info('generate_report success.\n %s' % os.path.abspath(file_news))


def generate_report():
    monkey_log = pull_monkeylog()
    js = pull_js()
    if monkey_log and js:
        try:
            report_name = 'GTReport ' + time.strftime("%Y-%m-%d %H.%M.%S", time.localtime())
            zip_report(report_name)
        except Exception as e:
            logger.error(e)


if __name__ == '__main__':
    generate_report()
