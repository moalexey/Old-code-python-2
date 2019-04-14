# -*- coding: UTF-8 -*-

import shelve

'''Добавляем в базу данных ссылки на файлообменник
'''

files_on_unibytes = open('files_on_unibytes.txt', 'r', encoding='UTF-8')
db = shelve.open('db.db')
keys = list(db.keys())
for string_in_file in files_on_unibytes:
    string_in_file = string_in_file.strip()
    id_file = string_in_file.split('Us4P3UgBB/')[1].split('.zip.html')[0]
    data = db[id_file]
    data['unibytes'] = string_in_file
    db[id_file] = data
db.close()
