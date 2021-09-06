#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:14:04 2019

@author: Kshitij Gupta <kshitijgm@gmail.com>
"""

from bs4 import BeautifulSoup
from shutil import which
import requests
import time
import subprocess
import sys


def check_app(name):
    ret = which(name) is not None
    if not ret:
        print('[*] command not found: {}'.format(name))
    return ret


def main():
    if not check_app('nyancat'):
        print('Please install \'nyancat\'! Exiting.')
        sys.exit()
    term = input('Enter your terminal cmd (Eg. deepin-terminal, konsole): ')
    if not check_app(term):
        sys.exit()

    url = 'https://android.googlesource.com/platform/manifest/+refs'
    matching = []

    while len(matching) == 0:
        print('\n[*] Checking!')
        tag_list = []
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for li in soup.findAll('li', {'class': 'RefList-item'}):
            tag = li.findChildren('a', recursive=False)[0]['href'].split('/')[-1]
            tag_list.append(tag)
        matching = [s for s in tag_list if 'android-12' in s or 'android12' in s]
        if len(matching) > 0:
            print('[!] ANDROID 12 IS HERE!')
            print('[!] Result: {}'.format(matching))
        else:
            print('[*] No Android 12 (yet) 😕')
            print('[*] Sleep time! 😴')
            time.sleep(10 * 60)  # Wait for 10 minutes
    try:
        from subprocess import DEVNULL
    except ImportError:
        import os
        DEVNULL = open(os.devnull, 'wb')
    subprocess.Popen([term, '-e', 'nyancat'], stdout=DEVNULL, stderr=subprocess.STDOUT)


if __name__ == '__main__':
    main()
