# -*- coding: UTF-8 -*

import shelve
import urllib.request
import urllib.error
import time
import lxml.html

def download(link):
	img = ''
	if 'fastpic.ru' in link:
		if link[-2:] == 'pg':
			try:
				img = urllib.request.urlopen(link).read()
			except urllib.error.HTTPError:
				pass
		elif link[-2:] == 'ng':
			try:
				img = urllib.request.urlopen(link).read()
			except urllib.error.HTTPError:
				pass
		else:
			# Перейти на сайт
			try:
				page = urllib.request.urlopen(link).read()
				html = lxml.html.fromstring(page)
				link = html.xpath(".//*[@id='picContainer']//@href")
				if link:
					link = link[0]
					img = urllib.request.urlopen(link).read()			
			except (urllib.error.HTTPError):
				pass
	
	elif 'radikal.ru/F/' in link:
		if link[-2:] == 'pg':
			try:
				img = urllib.request.urlopen(link).read()
			except urllib.error.HTTPError:
				pass
		elif link[-2:] == 'ng':
			try:
				img = urllib.request.urlopen(link).read()
			except urllib.error.HTTPError:
				pass
		else:
			# Перейти на сайт
			try:
				link = 'http://' + link.split('/F/')[1][:-5]
				img = urllib.request.urlopen(link).read()			
			except (urllib.error.HTTPError):
				pass
	elif 'savepic.net' in link:
		if link[-2:] == 'pg':
			try:
				img = urllib.request.urlopen(link).read()
			except urllib.error.HTTPError:
				pass
		elif link[-2:] == 'ng':
			try:
				img = urllib.request.urlopen(link).read()
			except urllib.error.HTTPError:
				pass
		else:
			link = link[:-3] + 'jpg'
			img = urllib.request.urlopen(link).read()
	elif 'savepic.org' in link:
		if link[-2:] == 'pg':
			try:
				img = urllib.request.urlopen(link).read()
			except urllib.error.HTTPError:
				pass
		elif link[-2:] == 'ng':
			try:
				img = urllib.request.urlopen(link).read()
			except urllib.error.HTTPError:
				pass
		else:
			link = link[:-3] + 'jpg'
			img = urllib.request.urlopen(link).read()
	elif 'imageshack.us' in link:
		if link[-2:] == 'pg':
			try:
				img = urllib.request.urlopen(link).read()
			except urllib.error.HTTPError:
				pass
		elif link[-2:] == 'ng':
			try:
				img = urllib.request.urlopen(link).read()
			except urllib.error.HTTPError:
				pass
	elif 'imageban.ru' in link:
		if link[-2:] == 'pg':
			try:
				img = urllib.request.urlopen(link).read()
			except urllib.error.HTTPError:
				pass
		elif link[-2:] == 'ng':
			try:
				img = urllib.request.urlopen(link).read()
			except urllib.error.HTTPError:
				pass		
	return img


post_ids = open('post_links.txt', 'r',  encoding='UTF-8')

for post_id in post_ids:
	post_id = post_id.strip()
	print(post_id)
	db = shelve.open('db.db', 'r')
	data = db[post_id]
	db.close()
	if data['img']:
		# Берем ссылку на обложку
		cover_url = data['img'][0]
		# Скачиваем
		cover_file = download(cover_url)
		if cover_file:
			# Сохраняем
			path = r'E:\parcer\img\%s.jpg' % (post_id,)
			open(path, 'wb').write(cover_file)
			images = [post_id+'.jpg']
		else:
			images = []
		# Если есть еще ссылки пытаемся получить файлы и сохранить
		if len(data['img']) > 1:
			for number, img_url in enumerate(data['img'][1:]):
				img_file = download(img_url)
				if img_file:
					path = r'E:\parcer\img\%s_%s.jpg' % (post_id, number)
					open(path, 'wb').write(img_file)
					images.append('%s_%s.jpg' % (post_id, number))
		if images:
			pass
			# Записываем изменение имени в базу данных
			db = shelve.open('db.db')
			data = db[post_id]
			data['img'] = images
			db[post_id] = data
			db.close()
# Далее ресайз (resize_images.py)
