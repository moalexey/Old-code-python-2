# -*- coding: UTF-8 -*

first_file_path = 'log.txt'
second_file_path = 'download_this_torrents.txt'

first_file = open(first_file_path, 'r', encoding='utf-8').readlines()
second_file = open(first_file_path, 'w', encoding='utf-8')
# Удалить все повторы строк
first_file = list(set(first_file))
# Записать в файл
print(first_file)
for string_in_file in first_file:
	second_file.write(string_in_file)

# Далее скачать все торренты (по сто штук), скрипт download_torrents.py
