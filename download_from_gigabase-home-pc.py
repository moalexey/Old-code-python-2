# -*- coding: UTF-8 -*-

import os
import time
import urllib.request

ping_url = 'ya.ru'
connection_name = 'fttx'
ligin = 'login'
password = 'password'

def reconnect():
    '''Reconnect for Windows.
    
    # Disconnecting
    os.system('rasdial fttx /disconnect')
    # Sleep 20 sec.
    time.sleep(20)
    # Conntcting
    os.system('rasdial fttx 'login' 'password')
    # Test connection
    time.sleep(5)
    while os.system('ping -n 1 %s' % (ping_url,)):
        os.system('rasdial %s %s %s' % (
            connection_name,
            ligin,
            password))
        time.sleep(25)
    '''
               
def test_connection(url='http://google.com'):
    '''Reconnect if ping_url unavailable
    (http://google.com, http://ya.ru or other).
    '''
    try:
        urllib.request.urlopen(url).read()
    except urllib.error.URLError:
        print('Connection lost, reconnect')
        reconnect()

domen = 'http://www.gigabase.com'
in_html_left = '</style><a href="'
in_html_right = '" class="nothx1">'
in_html_left_2 = 'id="dldAreaLink"><a href="'
in_html_right_2 = '.zip?referer=&hj=1"'
urls = open('urls.txt')

for url in urls:
    # Get filename from url
    file_name = url.split('BB/')[1]
    file_name = file_name.split('.html')[0]
    test_connection()
    # Get page 1
    with urllib.request.urlopen(url) as response:
    # Get html
        html = str(response.read())
    # Get link 1
    try:
        if html.index(file_name):
            link_1 = '%s%s' % (
                domen,
                html[html.index(in_html_left)+len(in_html_left):html.index(in_html_right)])
    except ValueError:
        print('File %s deleted, %s' % (file_name, url))
        continue
    print(link_1)
    # Get link 2
    test_connection()
    with urllib.request.urlopen(link_1) as response:
        # Get html
        html = str(response.read())
        # Get link 2
        try:
            if html.index(in_html_left_2):
                link_2 = html[html.index('id="dldAreaLink"><a href="')+26:html.index('.zip?referer=&hj=1"')+18]
        except ValueError:
            print('Error on step 2, file %s, link %s sleep 160 sec...' % (file_name, link_1))

            open('tmp.html', 'w').write(html)
            break
        else:
            print(link_2)
    # Download file
    test_connection()
    with urllib.request.urlopen(link_2) as response:
        print('Dowloading file: %s' % (file_name,))
        try:
            open(file_name, 'wb').write(response.read())
        except:
            print('Error on step #3, continue...')
            continue
        print('Done! %s sleep 160 sec...' % (time.ctime(),))
        time.sleep(160)
