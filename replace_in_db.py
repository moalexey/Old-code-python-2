# -*- coding: UTF-8 -*-

'''Получаем файл с новой ссылкой, старой ссылкой и номером файла
'''


db_1 = open(
    r'/media/alexey/1BD50E1F264F6878/script/review3d/finde_broken_links/review_05_10_15.sql', 'r').read()
list_files_links_and_filenames_for_replace = open(
    r'/media/alexey/1BD50E1F264F6878/script/review3d/finde_broken_links/list_files_links_and_filenames_for_replace.txt', 'r')
db_2 = open(
    r'/media/alexey/1BD50E1F264F6878/script/review3d/finde_broken_links/review_re.sql', 'w')

for string in list_files_links_and_filenames_for_replace:
    string = string.strip()
    new_link, old_link, file_number = string.strip().split(' | ')
    db_1 = db_1.replace(old_link, new_link)

db_2.write(db_1)
