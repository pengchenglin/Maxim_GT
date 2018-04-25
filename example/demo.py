#!/usr/bin/env python3
# -*- coding: utf-8 -*-

str ='CLASSPATH=/sdcard/monkey.jar:/sdcard/framework.jar exec app_process /system/bin tv.panda.test.monkey.Monkey -p com.github.android_app_bootstrap --running-minutes 1 --uiautomatormix --throttle 600 -v -v'
a='"'+str+'"'
print(a)