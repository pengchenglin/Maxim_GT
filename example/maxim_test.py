#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Public.Maxim_monkey import Maxim
import Public.command as cmd
import os


command = Maxim().command(package='com.gtr.sdkdemo', runtime=1, mode='uiautomatormix', throttle=100,
                          options='-v -v  ', off_line=False)
print(command)

# Maxim().run_monkey(command)
os.system('adb shell '+command)



