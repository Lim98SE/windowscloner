import os
import shutil

def clone():
    print("Where to clone Windows to?")
    path = input()
    print("Copying Windows to " + path + ".")
    shutil.copytree("C:/Windows", path)
    print("Finished.")
