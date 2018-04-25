#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Public.command as cmd
from logzero import logger


def pull_js( dst='../GT_Report/data/data.js'):
    '''将手机内的data.js复制到电脑'''
    logger.info('Starting to pull data.js to %s ' % dst)
    cmd.pull('/sdcard/GTRData/data.js', dst)
    logger.info('Pull data.js success')

if __name__ == '__main__':
    pull_js()