# -*- coding: UTF-8 -*-

'''Получаем название папок и файлов из файла торрента
'''

import os
import zipfile
from zipfile import ZipFile

def trimPath(dirPath):
    parentDir, dirToZip = os.path.split(dirPath)
    archivePath = path.replace(parentDir, "", 1)
    if parentDir:
        archivePath = archivePath.replace(os.path.sep, "", 1)
    if not True:
        archivePath = archivePath.replace(dirToZip + os.path.sep, "", 1)
    return os.path.normcase(archivePath)

def zipdir(dirPath=None, zipFilePath=None, includeDirInZip=True):

    if not zipFilePath:
        zipFilePath = dirPath + ".zip"
    if not os.path.isdir(dirPath):
        raise OSError("dirPath argument must point to a directory. "
            "'%s' does not." % dirPath)

    parentDir, dirToZip = os.path.split(dirPath)
    #Little nested function to prepare the proper archive path
    def trimPath(path):
        archivePath = path.replace(parentDir, "", 1)
        if parentDir:
            archivePath = archivePath.replace(os.path.sep, "", 1)
        if not includeDirInZip:
            archivePath = archivePath.replace(dirToZip + os.path.sep, "", 1)
        return os.path.normcase(archivePath)

    outFile = zipfile.ZipFile(zipFilePath, "w",
        compression=zipfile.ZIP_DEFLATED)
    for (archiveDirPath, dirNames, fileNames) in os.walk(dirPath):
        for fileName in fileNames:
            filePath = os.path.join(archiveDirPath, fileName)
            outFile.write(filePath, trimPath(filePath))
        #Make sure we get empty directories as well
        if not fileNames and not dirNames:
            zipInfo = zipfile.ZipInfo(trimPath(archiveDirPath) + "/")
            #some web sites suggest doing
            #zipInfo.external_attr = 16
            #or
            #zipInfo.external_attr = 48
            #Here to allow for inserting an empty directory.  Still TBD/TODO.
            outFile.writestr(zipInfo, "")
    outFile.close()

file_names_file = open(
    r'/media/alexey/1BD50E1F264F6878/script/review3d/file_zip_error_copy.txt', 'r')
file_zip_done = open(
    r'/media/alexey/1BD50E1F264F6878/script/review3d/file_zip_done.txt', 'w')
file_zip_error = open(
    r'/media/alexey/1BD50E1F264F6878/script/review3d/file_zip_error.txt', 'w')

for number, i in enumerate(file_names_file):
    url, file_number, file_name = i.strip().split(' | ')
    path = r'/media/alexey/1BD50E1F264F6878/script/review3d/download_books_from_torrent_tracker/%s' % (file_name,)
    print number
    if os.path.exists(path):
        print("Zipping %s file" % (file_number,))
        # Создание архива
        if os.path.isdir(path):
            zipdir(path, zipdir(path, r'/media/alexey/1BD50E1F264F6878/script/review3d/finde_broken_links/new_zip/%s.zip' % (file_number,)))
            print 'folder'
            file_zip_done.write('%s | %s | %s\n' %  (url, file_number, file_name))
        else:
            z = ZipFile(r'/media/alexey/1BD50E1F264F6878/script/review3d/finde_broken_links/new_zip/%s.zip' % (file_number,), 'w')
            # Добавление файла в архив
            z.write(trimPath(path))
            z.close()
            file_zip_done.write('%s | %s | %s\n' %  (url, file_number, file_name))
    elif not os.path.exists(path):
        path = r'/media/alexey/1BD50E1F264F6878/script/review3d/download_books_from_torrent_tracker/%s' % (file_name.decode('UTF-8'),)
        if  os.path.exists(path):
            print("Zipping %s file" % (file_number,))
        # Создание архива
            if os.path.isdir(path):
                print 'folder'
                zipdir(path, r'/media/alexey/1BD50E1F264F6878/script/review3d/finde_broken_links/new_zip/%s.zip' % (file_number,))
                file_zip_done.write('%s | %s | %s\n' %  (url, file_number, file_name))
            else:
                z = ZipFile(r'/%s.zip' % (file_number,), 'w')
                # Добавление файла в архив
                z.write(trimPath(path))
                z.close()
                file_zip_done.write('%s | %s | %s\n' %  (url, file_number, file_name))
        else:
            file_zip_error.write(
                '%s | %s | %s\n' %  (url, file_number, file_name))
    else:
        file_zip_error.write(
            '%s | %s | %s\n' %  (url, file_number, file_name))
        '''
        print("path %s d'not exist" % (path,))
        '''
