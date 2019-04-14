# -*- coding: UTF-8 -*-

import os
import time
import urllib.request

ping_url = 'ya.ru'
connection_name = 'fttx'
ligin = 'my_login'
password = 'my_password'

def reconnect():
    '''Reconnect for Windows.
    '''
    # Disconnecting
    print('reconnect - no way')
    '''
    os.system('rasdial fttx /disconnect')
    # Sleep 20 sec.
    time.sleep(20)
    # Conntcting
    os.system('rasdial fttx my_login my_password')
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

domen = 'http://www.unibytes.com'
in_html_left = '</style><a href="'
in_html_right = '" class="nothx1">'
in_html_left_2 = 'id="dldAreaLink"><a href="'
in_html_right_2 = '.zip?referer=&hj=1"'
urls = open('urls.txt')

for url in urls:
    # Get filename from url
    file_name = url.split('BB/')[1]
    file_name = file_name.split('.html')[0]
    if not os.path.exists(file_name):
        #test_connection()
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
            open('log.txt', 'a').write('Error on step 1, file %s, link %s\n' % (file_name, url))
            continue
        # Get link 2
        #test_connection()
        with urllib.request.urlopen(link_1) as response:
            # Get html
            html = str(response.read())
            # Get link 2
            try:
                if html.index(in_html_left_2):
                    link_2 = html[html.index('id="dldAreaLink"><a href="')+26:html.index('.zip?referer=&hj=1')+17]
            except ValueError:
                print('Error on step 2, file %s, link %s sleep 160 sec...' % (file_name, link_1))
                open('log.txt', 'a').write('Error on step 2, file %s, link %s\n' % (file_name, link_1))
                continue

        # Download file
        #test_connection()
        with urllib.request.urlopen(link_2) as response:
            print('Dowloading file: %s' % (file_name,))
            try:
                open(file_name, 'wb').write(response.read())
            except:
                print('Error on step #3, continue...')
                open('log.txt', 'a').write('Error on step #3, reconnect...\n')
                #test_connection()
                open(file_name, 'wb').write(response.read())
                open('log.txt', 'a').write('%s | %s\n' % (file_name, time.ctime()))
                continue
            else:
                open('log.txt', 'a').write('%s | %s\n' % (file_name, time.ctime()))
            print('Done! %s sleep 160 sec...' % (time.ctime(),))
            time.sleep(160)
    else:
        open('log.txt', 'a').write('Exist: %s | %s\n' % (file_name, time.ctime()))
        print('Exist: %s | %s' % (file_name, time.ctime()))
