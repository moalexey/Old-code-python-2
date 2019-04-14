# -*- coding: UTF-8 -*-

import shelve
from html.parser import HTMLParser
''' Удалить все html теги из текста
'''

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

db = shelve.open('db.db')
keys = list(db.keys())
for key in keys:
    data = db[key]
    html = data['html']
    text = strip_tags(html)
    data['html'] = text
    db[key] = data
db.close()
