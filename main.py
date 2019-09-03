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


def main():
    if which('nyancat') is None:
        print('Please install \'nyancat\'! Exiting.')
        sys.exit()
    url = 'https://android.googlesource.com/platform/manifest/+refs'
    term = 'deepin-terminal'
    matching = []

    while len(matching) is 0:
        print('\n[*] Checking!')
        tag_list = []
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for li in soup.findAll('li', {'class': 'RefList-item'}):
            tag = li.findChildren('a', recursive=False)[0]['href'].split('/')[-1]
            tag_list.append(tag)
        matching = [s for s in tag_list if 'android-10' in s or 'android10' in s]
        if len(matching) > 0:
            print('[!] ANDROID 10 IS HERE!!!')
            print('[!] Result: {}'.format(matching))
        else:
            print('[*] No Android 10 (yet) 😕')
            print('[*] Sleep time! 😴')
            time.sleep(10 * 60)  # Wait for 10 minutes

    subprocess.Popen([term, '-e', 'nyancat'])


if __name__ == '__main__':
    main()