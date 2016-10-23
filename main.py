#!/usr/bin/env python
import glob, os, random, time

folder = "/home/youruserhere/path/to/the/pictures/folder"
# WARNING: don't put non-picture files in this folder!

while True:
    files = []
    os.chdir(folder)
    for file in glob.glob("./*"):
        files.append(file)
        print(files)
    background = random.choice(files)
    print("\n\n" + background)
    os.system("gsettings set org.gnome.desktop.background picture-uri 'file://%s/%s'" % (folder,background))

    time.sleep(60*10)
