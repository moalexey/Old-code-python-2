# -*- coding: UTF-8 -*

import shelve

file_id_for_download = open('download_this_torrents_2.txt', 'w', encoding='UTF-8')
db = shelve.open('db.db')

for post_id in list(db.keys()):
	file_id_for_download.write(post_id+'\n')

db.close()

# Далее скачать все торренты (по сто штук), скрипт download_torrents.py
