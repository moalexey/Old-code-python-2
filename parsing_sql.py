# -*- coding: UTF-8 -*-

'''Из дампа sql извлекаем все номера файлов и ссылки на файлообменник
'''

sql_file = open(
    r'/media/alexey/1BD50E1F264F6878/script/review3d/finde_broken_links/review_re.sql', 'r'
    ).read()
open(
    r'/media/alexey/1BD50E1F264F6878/script/review3d/finde_broken_links/list_files_and_links.txt', 'w')

while True:
    try:
        sql_file = sql_file[sql_file.index('http://www.unibytes.com'):]
    except ValueError:
        break
    html = sql_file[:sql_file.index('.zip</a>')]
    if len(html) < 150 and '\\" target=\\"_blank\\">' in html:
        link, file_number = html.split('\\" target=\\"_blank\\">')
        print link, file_number
        open(r'/media/alexey/1BD50E1F264F6878/script/review3d/finde_broken_links/list_files_and_links.txt', 'a'
            ).write('%s | %s\n' % (link, file_number))
    sql_file = sql_file[sql_file.index('.zip</a>'):]
