# -*- coding: UTF-8 -*-

'''Запрос к rutracker о том какие файлы удалены
'''
import time
import urllib2

list_files_and_links = open(
    r'D:\script\review3d\finde_broken_links\deleted_files_list.txt', 'r'
    ).readlines()
list_files_exist_on_tracker = open(
    r'D:\script\review3d\finde_broken_links\list_files_exist_on_tracker', 'w')
list_files_deleted_from_tracker = open(
    r'D:\script\review3d\finde_broken_links\list_files_deleted_from_tracker', 'w')


for link_and_file_number in list_files_and_links:
    url, file_number = link_and_file_number.strip().split(' | ')
    html = urllib2.urlopen(
        'http://rutracker.org/forum/viewtopic.php?t='+file_number).read()
    if file_number in html:
        # На будущее - разделить файл на функции: проверить; скачать
        list_files_exist_on_tracker.write('%s | %s\n' % (url, file_number))
        print('OK: %s | %s' % (url, file_number))
    else:
        list_files_deleted_from_tracker.write('%s | %s\n' % (url, file_number))
        print file_number + ' no'
