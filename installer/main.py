#!/usr/bin/env python3
# entry point boostrap-installer

import sys
import os
import platform
#import pkg_resources
#sstém na převedení obsahu podporovane.txt do listu
supported_list = []
with open("installer/podporovane.txt", "r") as f:
    for line in f:
        if line.strip() =="":
            continue
        supported_list.append(line.strip())

print(supported_list)

def OsCheck():
    os_name = sys.platform #název OS
    print(os_name)
    os_version = platform.release() #verze OS
    print(os_version)
#později možnost vylepšit přes platform.release() 

#OsCheck()