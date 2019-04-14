# -*- coding: UTF-8 -*

import shelve
import urllib.request
import http.cookiejar
import lxml.html
import time

# Получить все тексты и записать их в базу данных

post_links = open('download_this_torrents.txt', 'r',  encoding='UTF-8')
#post_links = open('post_links.txt', 'r',  encoding='UTF-8')
#post_links = ('3738371', '5097311', '4986177', '2119069', '3128748')

# login to rutracker
login = 'my_login'
password = 'my_password'
login_page = 'http://login.rutracker.org/forum/login.php'

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

opener.addheaders = [('User-agent', 'Mozilla/5.0')]
opener.addheaders = [('Referer', 'http://rutracker.org/forum/viewtopic.php?t=385615')]

urllib.request.install_opener(opener)

payload = {
'login_username' : login,
'login_password' : password,
'cookie'   : '1',
'login' : 'вход'
}

data = urllib.parse.urlencode(payload).encode('ascii')
request = urllib.request.Request(url=login_page, data=data)
response = urllib.request.urlopen(request)
html = response.read().decode('windows-1251')

for post_id in post_links:
	post_id = post_id.strip()
	url = 'http://rutracker.org/forum/viewtopic.php?t=' + post_id
	request = urllib.request.Request(url=url, data=data)
	response = urllib.request.urlopen(request)
	page = response.read()
	html = lxml.html.fromstring(page)
	size = html.xpath(".//*[@id='tor-size-humn']/text()")
	if size:
		# Если размер файла меньше 500 мб - собираем текст и ссылки на картинки
		# Дописать год >2012 скачан >300 раз
		size = str(size[0]).split(' ')
		if float(size[0]) < float(500) and size[1] != 'GB':
			# Сбор текста без очистки от html кода
			page = page[page.find('<div class="post_body"'.encode('windows-1251')):]
			page = page[:page.find('<div class="clear"></div>'.encode('windows-1251'))]
			# Сбор ссылок на картинки
			try:
				img_cover = html.xpath(".//*[@class='postImg postImgAligned img-right']/@title")[0]
				img_cover_link = str(img_cover)
				if not 'rutracker' in img_cover_link:
					img_links = [img_cover_link]
				else:
					img_links = []
			except IndexError:
				img_links = []

			img_pages = html.xpath(".//*[@class='postLink']/@href")[:3]
			# Удаляем ссылки на рутрекер если попались с картинками
			for i in img_pages:
				if not 'rutracker' in i:
					img_links.append(str(i))
			# Сохраняем в базу данных
			db = shelve.open('db.db')
			db[post_id] = {'title': str(html.xpath(".//title/text()")[0]),
				'size': size,
				'html': str(page.decode('windows-1251')),
				'img': img_links
				}
			db.close()
			print(post_id)
			open('log.txt', 'a',  encoding='UTF-8').write(post_id+'\n')

	time.sleep(3)
'''
db = shelve.open('db.db')

for post_id in list(db.keys()):
	data = db[post_id]
	#print(data['html'].encode('windows-1251'))
	open('tmp.txt', 'a', encoding='UTF-8').write(data['html'])

db.close()
'''
# Далее удалить все дубли в файле log (скрипт remove_duplicates_in_txt.py)
