#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Public.Maxim_monkey import Maxim



cmd = Maxim().command(package='com.github.android_app_bootstrap',  runtime=1, mode='uiautomatormix', throttle=600, options='-v -v')
print(cmd)

Maxim().run_monkey(cmd, actions=True)


# # os.system('adb push ../Maxim/max.xpath.actions' '/sdcard/')

