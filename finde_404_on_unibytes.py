# -*- coding: UTF-8 -*-

'''Запрос к unibytes о том какие файлы удалены
'''
import time
import urllib2

list_files_and_links = open(
    r'/media/alexey/1BD50E1F264F6878/script/review3d/finde_broken_links/list_files_and_links.txt', 'r'
    ).readlines()
deleted_files_list_file = open(
    r'/media/alexey/1BD50E1F264F6878/script/review3d/finde_broken_links/deleted_files_list.txt', 'w')

for link_and_file_number in list_files_and_links:
    url, file_number = link_and_file_number.strip().split(' | ')
    html = urllib2.urlopen(url).read()
    if 'Файл не существует:' in html:
        print('404: %s | %s' % (url, file_number))
        deleted_files_list_file.write('%s | %s\n' % (url, file_number))
    else:
        print('OK: %s | %s' % (url, file_number))
    #time.sleep(7)
