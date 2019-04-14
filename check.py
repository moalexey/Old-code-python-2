# -*- coding: UTF-8 -*-

'''Проверка на дубли ссылок
'''

list_files_and_links = open(
    r'/media/alexey/1BD50E1F264F6878/script/review3d/finde_broken_links/list_files_and_links.txt', 'r'
    ).readlines()
new_list_files_and_links = []

while list_files_and_links:
    link_and_file_number = list_files_and_links[0].strip()
    del list_files_and_links[0]
    if not link_and_file_number in new_list_files_and_links:
        new_list_files_and_links.append(link_and_file_number)

file_list_files_and_links = open(
    r'/media/alexey/1BD50E1F264F6878/script/review3d/finde_broken_links/list_files_and_links.txt', 'w')

for i in new_list_files_and_links:
    file_list_files_and_links.write(i+'\n')
