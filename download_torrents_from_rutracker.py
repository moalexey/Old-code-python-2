# -*- coding: UTF-8 -*-

'''Скачиваем все торренты с rutracker по списку
'''
import time
import urllib2

list_files_and_links = open(
    r'D:\script\review3d\finde_broken_links\list_files_exist_on_tracker', 'r'
    ).readlines()

for link_and_file_number in list_files_and_links:
    url, file_number = link_and_file_number.strip().split(' | ')
    req = urllib2.Request(
        'http://dl.rutracker.org/forum/dl.php?t='+file_number+'&guest=1',
        '',
        {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://rutracker.org/forum/viewtopic.php?t='+file_number,
        'Connection': 'keep-alive'})

    open(r'D:\script\review3d\finde_broken_links\torrents\%s%s' % (
        file_number, '.torrent'), 'wb').write(urllib2.urlopen(req).read())
    print('OK: %s | %s' % (url, file_number))
    #time.sleep(7)
