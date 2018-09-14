from random import randrange as r
from time import sleep as ts
import os
 
ascii_art = ""
 
c = 0
colors = ['\033[97m','\033[96m','\033[95m','\033[94m','\033[93m','\033[92m','\033[91m']
while 1:
    print("\033[1m"+colors[c]+ascii_art)
    c += 1
    if c == len(colors):
        c = 0
    ts(0.1)
    os.system('clear')
