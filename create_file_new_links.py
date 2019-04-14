# -*- coding: UTF-8 -*-

'''Получаем файл с новой ссылкой, старой ссылкой и номером файла
'''


file_zip_done = open(
    r'/media/alexey/1BD50E1F264F6878/script/review3d/file_zip_done.txt', 'r').readlines()
link_and_file_number = open(
    r'/media/alexey/1BD50E1F264F6878/script/review3d/finde_broken_links/list_files_links_and_filenames_file_end.txt', 'r')
list_files_links_and_filenames_for_replace = open(
    r'/media/alexey/1BD50E1F264F6878/script/review3d/finde_broken_links/list_files_links_and_filenames_for_replace.txt', 'w')
links_on_borncash = open(
    r'/media/alexey/1BD50E1F264F6878/script/review3d/finde_broken_links/links_on_borncash.txt', 'r').readlines()

for string in links_on_borncash:
    string = string.strip()
    new_link, new_file_number = string.split('BB/')
    new_link += 'BB/'
    file_number = new_file_number.split('.zip.html')[0]
    for string_in_zip in file_zip_done:
        old_link, old_file_number, old_file_name = string_in_zip.strip().split(' | ')
        if file_number == old_file_number:
            list_files_links_and_filenames_for_replace.write('%s | %s | %s\n' % (
                new_link, old_link, file_number))
