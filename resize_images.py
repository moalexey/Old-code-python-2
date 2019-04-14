# -*- coding: UTF-8 -*

import os
from PIL import Image

post_ids = open('post_links.txt', 'r',  encoding='UTF-8')

all_files_in_dir = os.listdir(r'E:\parcer\img')
for file_name in all_files_in_dir:
	if '_' in file_name:
		try:
			im = Image.open(r'E:\parcer\img\%s' % (file_name,))
			im.thumbnail((150, 150))
			im.save(r'E:\parcer\tmp_img\tumb_%s' % (file_name,))
		except IOError:
			im = Image.open(r'E:\parcer\img\%s' % (file_name,)).convert('RGB')
			im.thumbnail((150, 150))
			im.save(r'E:\parcer\tmp_img\tumb_%s' % (file_name,))
