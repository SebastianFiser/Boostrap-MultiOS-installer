#!/usr/bin/env python3
# entry point boostrap-installer

import sys
import os
import platform
#import pkg_resources
#sstém na převedení obsahu podporovane.txt do listu
supported_python = (3, 10)
supported_list = []
current_dir = os.path.dirname(__file__)
path = os.path.join(current_dir, "podporovane.txt")
with open(path, "r") as f:
    for line in f:
        if line.strip() =="":
            continue
        supported_list.append(line.strip())

packages_list = []

#print(supported_list)

def OsCheck():
    os_name = sys.platform #název OS
    #print(os_name)
    os_version = platform.release() #verze OS
    #print(os_version)
    os_system = (os_name + os_version)
    print(os_system)

#kontrola zda je systém v podporovaném seznamu
    if os_system in supported_list:
        print("Váš systém je podporován, může se pokračovat v instalaci.")
    else:
        print("Váš systém není podporován, instalace bude ukončena.")
        sys.exit()

    if sys.version_info >= (supported_python):
        print("Vaše verze Pythonu je podporována, může se pokračovat v instalaci.")
    else:
        print("Vaše verze Pythonu není podporována, instalace bude ukončena.")
        sys.exit()




OsCheck()