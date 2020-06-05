import os
from pathlib import Path
from datetime import datetime
import time

def get_siblings(path):
    parent = path
    for x in parent.iterdir():
        if x.is_dir() and x != path:
            yield x

def udt_git():
    for f in get_siblings(Path.cwd()):
        os.system('echo "'+(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + '->' + str(f))+'"')
        os.system('cd '+str(f)+' && ' + 'git pull')

def timer(n):
    while True:
        # print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        udt_git()
        time.sleep(n)

# 21600s
# timer(20)
timer(21600)
