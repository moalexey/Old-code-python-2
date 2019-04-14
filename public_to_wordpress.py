# -*- coding: UTF-8 -*-

import os
import shelve
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

'''Создаем пост для публикации (title, size, html, img, unibytes)
'''

user = 'admin'
password ='gt4h61NahS!2EC2)YyB&uOq*'


wp = Client('http://review3d.ru/xmlrpc.php', user, password)

files_ids = open('file_zip_done.txt', 'r', encoding='UTF-8')
tmp = open('tmp.txt', 'w', encoding='UTF-8')

db = shelve.open('db.db')

for file_id in files_ids:
    file_id = file_id.strip()
    data = db[file_id]
    title = data['title']
    text = data['html'][data['html'].find('Год'):data['html'].find('римеры страниц')-1]
    imgs = data['img']
    link = data['unibytes']
    post = ''
    if imgs:
        path = r'E:\parcer\img_3\%s' % (imgs[0],)
        if os.path.exists(path):
            cover_img = 'http://review3d.ru/wp-content/uploads/img_3/'+imgs[0]
            cover = '<img class="alignright size-full wp-image-1341" title="%s" src="%s" alt="%s" height="300" />' % (
                title, cover_img, title)
        else:
            cover = ''
        if cover:
            post += cover + '\n' + text + '\n'
        else:
            post += text + '\n'
        if len(imgs) > 1:
            imgs = imgs[1:]
            for number, img in enumerate(imgs):
                path = r'E:\parcer\img_3\%s' % (img,)
                if os.path.exists(path):
                    full_img = 'http://review3d.ru/wp-content/uploads/img_3/' + img
                    tumb_img = 'http://review3d.ru/wp-content/uploads/img_3/tumb_' + img
                    html = '<a href="%s" target="_blank"><img class="alignnone size-thumbnail wp-image-1343" title="%s" src="%s" alt="%s" /></a>' % (
                        full_img, title+' '+str(number), tumb_img, title+' '+str(number))
                    post += html
    else:
        post += text
    unibytes = '\nСкачать бесплатно %s можно по ссылке:\n<p style="text-align: center;"><a href="%s" target="_blank">%s.zip</a></p>' % (
        title, link, file_id)
    post += unibytes
    wp_post = WordPressPost()
    wp_post.title = title
    wp_post.content = post
    wp_post.terms_names = {'post_tag': ['Точные науки'],'category': ['Точные науки']}
    wp.call(NewPost(wp_post))

db.close()
