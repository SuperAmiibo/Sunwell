import os
import sys
import subprocess
import threading
import time


def compose(file):
    cmd = "pngquant\\pngquant.exe --force --ext=.png --speed=1 --verbose --quality=45-85 " + file
    print(cmd)
    ret = subprocess.Popen(cmd, shell=True)
def compose1(file):
    cmd = "pngquant\\pngquant.exe --force --ext=.png --speed=1 --verbose --quality=45-85 " + file
    print(cmd)
    ret = subprocess.Popen(cmd, shell=True)

def compose2(file):
    cmd = "pngquant\\pngquant.exe --force --ext=.png --speed=1 --verbose --quality=45-85 " + file
    print(cmd)
    ret = subprocess.Popen(cmd, shell=True)

def compose3(file):
    cmd = "pngquant\\pngquant.exe --force --ext=.png --speed=1 --verbose --quality=45-85 " + file
    print(cmd)
    ret = subprocess.Popen(cmd, shell=True)

def compose4(file):
    cmd = "pngquant\\pngquant.exe --force --ext=.png --speed=1 --verbose --quality=45-85 " + file
    print(cmd)
    ret = subprocess.Popen(cmd, shell=True)
    ret.wait()

def main():
    path = "d:\\Desktop\\Sunwell\\scripts\\tiles"
    files = os.listdir(path)
    allfile = {}
    i = 0
    for file in files :
        allfile[i] = file
        i = i + 1
    for index in allfile :
        size = os.path.getsize(path + "\\" + allfile[index])
        if (size > 10000):
            if (index % 5 == 0):
                compose(path + "\\" + allfile[index])
            elif (index % 5 == 1):
                compose1(path + "\\" + allfile[index])
            elif (index % 5 == 2):
                compose2(path + "\\" + allfile[index])
            elif (index % 5 == 3):
                compose3(path + "\\" + allfile[index])
            elif (index % 5 == 4):
                compose4(path + "\\" + allfile[index])
        else:
            print("skip size small: " + allfile[index] + ": " + str(size))

if __name__ == "__main__":
    
    main()
    

    print ("all over")
