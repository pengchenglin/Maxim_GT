#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# extention for http://gt.qq.com/
# reference doc http://gt.qq.com/docs/a/UseGtWithBroadcast.txt
# GT3.1 supported


import functools
from logzero import logger
import time
import Public.command as cmd



class GT(object):
    def __init__(self):
        self._broadcast = functools.partial(cmd.adb_shell, 'am', 'broadcast', '-a',)
        # self._package_name = None

    def start_test(self, package_name, cpu=True, net=True, pss=True, jif=False, pri=False, fps=False):
        # self._package_name = package_name
        broadcast = self._broadcast
        # 1. start app
        cmd.unlock_devices()
        logger.info('Stopping all running app')
        cmd.app_stop_all()

        self.clean_data()  # clean old data
        logger.info('Starting GT Test')
        cmd.app_start('com.tencent.wstt.gt')     # 'com.tencent.wstt.gt.activity.GTMainActivity')

        # 2. set test package name
        broadcast('com.tencent.wstt.gt.baseCommand.startTest', '--es', 'pkgName', package_name)
        # 3. set collect params
        if cpu:
            broadcast('com.tencent.wstt.gt.baseCommand.sampleData', '--ei', 'cpu', '1')
        if net:
            broadcast('com.tencent.wstt.gt.baseCommand.sampleData', '--ei', 'net', '1')
        if pss:
            broadcast('com.tencent.wstt.gt.baseCommand.sampleData', '--ei', 'pss', '1')
        if jif:
            broadcast('com.tencent.wstt.gt.baseCommand.sampleData', '--ei', 'jif', '1')
        if pri:
            broadcast('com.tencent.wstt.gt.baseCommand.sampleData', '--ei', 'pri', '1')
        if fps:
            broadcast('com.tencent.wstt.gt.baseCommand.sampleData', '--ei', 'fps', '1')

        # 4. switch back to app
        logger.info('GT Setup already, starting GT test......')
        time.sleep(3)
        # self.app_start(package_name)

    def stop_test(self):
        '''停止测试，备份测试数据、关闭GT、执行导出js的自动化脚本、执行Pull 将data.js 复制到电脑'''
        self._broadcast('com.tencent.wstt.gt.baseCommand.endTest')
        self.quit()
        self.backup_data()
        logger.info('GT testing finished>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        cmd.app_stop_all()
        logger.info('Please Export data.js manually')


    def backup_data(self):
        '''备份GTR文件到GTR_Backup'''
        # self._broadcast('com.tencent.wstt.gt.baseCommand.exportData', '--es', 'saveFolderName', '/sdcard/GTR_Backup/')
        cmd.adb_shell('cp -r sdcard/GTR/. sdcard/GTR_Backup/')
        logger.info('Backup /GTR/ to /GTR_Backup/ success')

    def clean_data(self):
        '''清除GTR文件'''
        # self._broadcast('com.tencent.wstt.gt.baseCommand.clearData')
        cmd.adb_shell('rm -r sdcard/GTR')
        cmd.adb_shell('rm -r sdcard/GTRData/data.js')
        logger.info('Clearing GTR file and data.js')

    def quit(self):
        '''结束GT并退出'''
        self._broadcast('com.tencent.wstt.gt.baseCommand.exitGT')
        cmd.app_stop('com.tencent.wstt.gt')
        logger.info('Exiting GT and stop GT App')





