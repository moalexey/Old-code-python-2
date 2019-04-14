# -*- coding: UTF-8 -*-

import time
import urllib.request
import http.cookiejar

# login to rutracker and download torrents
login = 'my_login'
password = 'my_password'
login_page = 'http://login.rutracker.org/forum/login.php'
download_torrents_id_file = open(
	'download_this_torrents_1.txt', 'r', encoding='UTF-8')

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

for post_id in download_torrents_id_file:
	post_id = post_id.strip()
	url = 'http://dl.rutracker.org/forum/dl.php?t=' + post_id
	request = urllib.request.Request(url=url, data=data)
	response = urllib.request.urlopen(request)
	torrent = response.read()
	path = r'E:\parcer\torrents\%s.torrent' % (post_id,)
	open(path, 'wb').write(torrent)
	print(post_id)
	time.sleep(3)

# Далее скачать все картинки скрипт download_images.py
