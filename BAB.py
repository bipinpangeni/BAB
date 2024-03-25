import os,platform
os.system('git pull')
os.system("clear")
bab=platform.architecture()[0]
if bab=="32bit":
    __import__("p32")
elif bab=="64bit":
    __import__("p64")
