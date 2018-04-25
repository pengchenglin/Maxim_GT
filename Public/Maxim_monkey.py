#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from logzero import logger
import time
import Public.command as cmd
import os


# 参考网站：
# Maxim-高速 Android Monkey 工具使用记录： https://testerhome.com/topics/11884
# 基于 Android Monkey 二次开发，实现高速点击的 Android Monkey 自动化工具 fastmonkey ：https://testerhome.com/topics/11719

class Maxim(object):
    def run_monkey(self, monkey_shell, actions=False, widget_black=False):
        '''
        清理旧的配置文件并运行monkey，等待运行时间后pull log文件到电脑
        :param GT: u2.connect()
        :param monkey_shell: shell命令 uiautomatortroy 时 max.xpath.selector文件需要配置正确
        :param actions: 特殊事件序列 max.xpath.actions文件需要配置正确
        :param widget_black: 黑控件 黑区域屏蔽 max.widget.black文件需要配置正确
        :return:
        '''
        self.clear_env()
        self.push_jar()
        if 'awl.strings' in monkey_shell:
            self.push_white_list()
        if 'uiautomatortroy' in monkey_shell:
            self.push_selector()
        if actions:
            self.push_actions()
        if widget_black:
            self.push_widget_black()
        self.set_AdbIME()

        runtime = monkey_shell.split('running-minutes ')[1].split(' ')[0]
        logger.info('starting run monkey')
        logger.info('It will be take about %s minutes,please be patient ...........................' % runtime)
        cmd.adb_shell(monkey_shell)
        time.sleep(int(runtime) * 60 + 30)
        self.pull_monkeylog()

    def command(self, package, runtime, mode=None, whitelist=False, throttle=None, options=None):
        '''
        monkey命令封装
        :param package:被测app的包名
        :param runtime: 运行时间 minutes分钟
        :param mode: 运行模式
            uiautomatormix(混合模式,70%控件解析随机点击，其余30%按原Monkey事件概率分布)、
            pct-uiautomatormix n ：可自定义混合模式中控件解析事件概率 n=1-100
            uiautomatordfs：DFS深度遍历算法（优化版）（注 Android5不支持dfs）(u2和dsf冲突 无法使用）
            uiautomatortroy：TROY模式（支持特殊事件、黑控件等） 配置 max.xpath.selector troy控件选择子来定制自有的控件选择优先级
            不填写则默认原生monkey
        :param whitelist: activity白名单  需要将awl.strings 配置正确
        :param throttle: 在事件之间插入固定的时间（毫秒）延迟
        :param options: 其他参数及用法同原始Monkey
        :return: shell命令
        '''
        classpath = 'CLASSPATH=/sdcard/monkey.jar:/sdcard/framework.jar exec app_process /system/bin tv.panda.test.monkey.Monkey'
        package = ' -p ' + package
        runtime = ' --running-minutes ' + str(runtime)
        if mode:
            mode = ' --' + mode
        else:
            mode = ''
        if throttle:
            throttle = ' --throttle ' + str(throttle)
        else:
            throttle = ''
        if options:
            options = ' ' + options
        else:
            options = ''
        if whitelist:
            whitelist = ' --act-whitelist-file /sdcard/awl.strings'
        else:
            whitelist = ''

        off_line = ' -v -v >/sdcard/monkeyout.txt 2>/sdcard/monkeyerr.txt &'

        monkey_shell = '"'+(''.join([classpath, package, runtime, mode, whitelist, throttle, options, off_line]))+'"'
        # print(monkey_shell)
        return monkey_shell

    #  Maxim 文件夹说明：
    # awl.strings：存放activity白名单
    # max.xpath.actions：特殊事件序列
    # max.xpath.selector：TROY模式（支持特殊事件、黑控件等） 配置 max.xpath.selector troy控件选择子来定制自有的控件选择优先级
    # max.widget.black：黑控件 黑区域屏蔽
    # max.strings 随机输入字符，内容可自定义配置

    def push_jar(self):
        cmd.push('../Maxim/monkey.jar', '/sdcard/')
        cmd.push('../Maxim/framework.jar', '/sdcard/')
        logger.info('push jar file--->monkey.jar framework.jar')

    def push_white_list(self):
        cmd.push('../Maxim/awl.strings', '/sdcard/')
        logger.info('push white_list file---> awl.strings ')

    def push_actions(sedl):
        cmd.push('../Maxim/max.xpath.actions', '/sdcard/')
        logger.info('push actions file---> max.xpath.actions ')

    def push_selector(self):
        cmd.push('../Maxim/max.xpath.selector', '/sdcard/')
        logger.info('push selector file---> max.xpath.selector ')

    def push_widget_black(self):
        cmd.push('../Maxim/max.widget.black', '/sdcard/')
        logger.info('push widget_black file---> max.widget.black ')

    def push_string(self):
        cmd.push('../Maxim/max.strings', '/sdcard/')
        logger.info('push string file---> max.strings ')

    def pull_monkeylog(self):
        cmd.pull('/sdcard/monkeyerr.txt', '../GT_Report/monkeyerr.txt')
        cmd.pull('/sdcard/monkeyout.txt', '../GT_Report/monkeyout.txt')
        logger.info('pull monkeylog file---> monkeyerr.txt  monkeyout.txt ')

    def clear_env(self):
        cmd.adb_shell('rm -r /sdcard/monkeyerr.txt')
        cmd.adb_shell('rm -r /sdcard/monkeyout.txt')
        cmd.adb_shell('rm -r /sdcard/max.widget.black')
        cmd.adb_shell('rm -r /sdcard/max.xpath.selector')
        cmd.adb_shell('rm -r /sdcard/max.xpath.actions')
        cmd.adb_shell('rm -r /sdcard/awl.strings')
        cmd.adb_shell('rm -r /sdcard/monkey.jar')
        cmd.adb_shell('rm -r /sdcard/framework.jar')
        cmd.adb_shell('rm -r /sdcard/max.strings')
        logger.info('Clear monkey env success')

    def set_AdbIME(self):
        ime = cmd.adb_shell('ime list -s')
        if 'adbkeyboard' in ime:
            cmd.adb_shell('ime set com.android.adbkeyboard/.AdbIME')
            self.push_string()
            logger.info('set adbkeyboard as default')
        else:
            logger.error('Have not inatall adbkeyboard yet!')



if __name__ == '__main__':
    Maxim().pull_monkeylog()