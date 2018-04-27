#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
# sys.path.append(os.path.split(os.path.split(os.path.abspath(''))[0])[0])
sys.path.append('..')

from Public.gt import GT
from Public.Maxim_monkey import Maxim
import Public.command as cmd


# 安装apk
cmd.install_apk('../apk/GTdemo.apk')

# 开始GT
GT().start_test('com.gtr.sdkdemo')

# 运行monkey
command = Maxim().command(package='com.gtr.sdkdemo', runtime=3, mode='uiautomatormix', throttle=100, options=' -v -v ', whitelist=True)
Maxim().run_monkey(command)

# 结束GT
GT().stop_test()

"""
请在完成测试后，手动打开GT导出js文件之后  
执行 get_report.bat 会打包报告到工程目录 附带上monkey日志monkeyerr.txt、monkeyout.txt'在报告中
"""
