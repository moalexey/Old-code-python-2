# -*- coding: UTF-8 -*
# Удалить все ссылки на посты которые уже существуют на сайте библиотеки

all_files_on_unibytes = open(
	'all_files_on_unibytes.txt', 'r', encoding='UTF-8').readlines()
page_links = open(
	'page_links.txt', 'r', encoding='UTF-8').readlines()
post_links = open('post_links.txt', 'w', encoding='UTF-8')

for page_link in page_links:
	page_id = page_link.strip().split('viewtopic.php?t=')[1]
	for file_id_on_unibytes in all_files_on_unibytes:
		file_id_on_unibytes = file_id_on_unibytes.strip()
		if page_id == file_id_on_unibytes:
			x += 1
			break
	else:
		post_links.write(page_id+'\n')
