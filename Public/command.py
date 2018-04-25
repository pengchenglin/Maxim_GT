#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from subprocess import list2cmdline


def adb_shell(*args):
    """
            Example:
                adb_shell('pwd')
                adb_shell('ls', '-l')
                adb_shell('ls -l')

            Returns:
                a UTF-8 encoded string for stdout merged with stderr, after the entire shell command is completed.
            """
    cmdline = args[0] if len(args) == 1 else list2cmdline(args)
    p = os.popen(' '.join(['adb shell ', cmdline]))
    return p.read()


def app_stop(pkg_name):
    """ Stop one application: am force-stop"""

    adb_shell('am', 'force-stop', pkg_name)


def app_stop_all(excludes=[]):
    """ Stop all applications
    Args:
        excludes (list): apps that do now want to kill

    Returns:
        a list of killed apps
    """
    # our_apps = ['com.github.uiautomator', 'com.github.uiautomator.test']
    pkgs = re.findall('package:([^\s]+)', adb_shell('pm', 'list', 'packages', '-3'))
    process_names = re.findall('([^\s]+)$', adb_shell('ps'), re.M)
    kill_pkgs = set(pkgs).intersection(process_names).difference(excludes)
    kill_pkgs = list(kill_pkgs)
    for pkg_name in kill_pkgs:
        app_stop(pkg_name)
    return kill_pkgs


def app_start(pkg_name, activity=None, extras={}, wait=True, stop=False, unlock=False):
    """ Launch application
    Args:
        pkg_name (str): package name
        activity (str): app activity
        stop (str): Stop app before starting the activity. (require activity)
    """
    # if unlock:
    #     self.unlock()

    if activity:
        # -D: enable debugging
        # -W: wait for launch to complete
        # -S: force stop the target app before starting the activity
        # --user <USER_ID> | current: Specify which user to run as; if not
        #    specified then run as the current user.
        # -e <EXTRA_KEY> <EXTRA_STRING_VALUE>
        # --ei <EXTRA_KEY> <EXTRA_INT_VALUE>
        # --ez <EXTRA_KEY> <EXTRA_BOOLEAN_VALUE>
        args = ['am', 'start']
        if wait:
            args.append('-W')
        if stop:
            args.append('-S')
        args += ['-n', '{}/{}'.format(pkg_name, activity)]
        # -e --ez
        extra_args = []
        for k, v in extras.items():
            if isinstance(v, bool):
                extra_args.extend(['--ez', k, 'true' if v else 'false'])
            elif isinstance(v, int):
                extra_args.extend(['--ei', k, str(v)])
            else:
                extra_args.extend(['-e', k, v])
        args += extra_args
        adb_shell(*args)  # 'am', 'start', '-W', '-n', '{}/{}'.format(pkg_name, activity))
    else:
        if stop:
            app_stop(pkg_name)
        adb_shell('monkey', '-p', pkg_name, '-c', 'android.intent.category.LAUNCHER', '1')


def pull(src, dst):
    dst = os.path.abspath(dst)
    # print(' '.join(['adb pull ', src, dst]))
    os.popen(' '.join(['adb pull ', src, dst]))


def push(src, dst):
    src = os.path.abspath(src)
    # print(' '.join(['adb push ', src, dst]))
    os.popen(' '.join(['adb push ', src, dst]))

if __name__ == '__main__':
    pull('/sdcard/monkey.jar','../')