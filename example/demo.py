#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
# sys.path.append(os.path.split(os.path.split(os.path.abspath(''))[0])[0])
sys.path.append('..')

from Public.gt import GT
from Public.Maxim_monkey import Maxim

# 开始GT
# cmd.install_apk('../apk/xiaoying_GTsdk.apk')
GT().start_test('com.quvideo.xiaoying')

# 运行monkey
command = Maxim().command(package='com.quvideo.xiaoying', runtime=5, mode='uiautomatormix', throttle=800)
print(command)
Maxim().run_monkey(command)
#
# # 结束GT
GT().stop_test()

# 手动打开GT导出js文件之后  执行 pubilc下的get_report
