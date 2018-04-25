#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from Public.gt import GT
from Public.Maxim_monkey import Maxim



# 开始GT
GT().start_test('com.quvideo.xiaoying')
# os.system('adb shell monkey --throttle 1000 -s 53 --pct-anyevent 0 --pct-nav 0 --pct-touch 44 -p com.quvideo.xiaoying --pct-motion 30 --pct-trackball 8 --pct-syskeys 8 --pct-majornav 0 --pct-appswitch 10 --pct-flip 0 --monitor-native-crashes -v -v 10000')
# monkey_shell ='CLASSPATH=/sdcard/monkey.jar:/sdcard/framework.jar exec app_process /system/bin tv.panda.test.monkey.Monkey -p com.quvideo.xiaoying --running-minutes 20 --uiautomatormix --throttle 100 -v -v >/sdcard/monkeyout.txt 2>/sdcard/monkeyerr.txt &'
# 运行monkey

command = Maxim().command(package='com.quvideo.xiaoying', runtime=50, mode='uiautomatormix', whitelist=True, throttle=500)
print(command)
Maxim().run_monkey(command)

# 结束GT
GT().stop_test()



