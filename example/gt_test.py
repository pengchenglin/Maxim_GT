#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from Public.gt import GT
import time



# 开始GT
GT().start_test('com.gtr.sdkdemo')

time.sleep(30)

# 结束GT
GT().stop_test()



