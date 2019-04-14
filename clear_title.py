# -*- coding: UTF-8 -*-

import shelve

''' Удалить мусор из заголовка
'''

tmp = open('tmp.txt', 'w', encoding='UTF-8')
db = shelve.open('db.db')
keys = list(db.keys())
for key in keys:
    data = db[key]
    try:
        title = '%s %s' % (
            db[key]['title'].split(' [')[0].split(' - ')[1],
            db[key]['title'].split(' [')[0].split(' - ')[0])
    except IndexError:
        title = db[key]['title'].split(' [')[0].split(' - ')[0]
    data['title'] = title
    db[key] = data
    tmp.write(title+'\n')
db.close()
