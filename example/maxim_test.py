#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Public.Maxim_monkey import Maxim
import Public.command as cmd
import os

# cmd.install_apk('../apk/xiaoying_GTsdk.apk')
command = Maxim().command(package='com.quvideo.xiaoying', runtime=1, mode='uiautomatordfs', throttle=500,
                      options='-v -v  ', whitelist=True, off_line=False)
print(command)

# Maxim().run_monkey(cmd, actions=True)

Maxim().push_actions()
Maxim().push_white_list()
cmd.unlock_devices()
cmd.app_stop_all()

os.system('adb shell ' + command)
# cmd.adb_shell(command)

# # os.system('adb push ../Maxim/max.xpath.actions' '/sdcard/')
