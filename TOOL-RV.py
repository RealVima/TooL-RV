#!/bin/python
#Don't CopyRight...
#Thanks For Sl Legends Family...
#Member Of Sl Legends Family...
import os
import sys

os.system("clear")

print ('\033[1;31m'"      _____ ___   ___  _          ______     __")
print ('\033[1;31m'"     |_   _/ _ \ / _ \| |        |  _ \ \   / / ")
print ('\033[1;31m'"       | || | | | | | | |   _____| |_) \ \ / / ")
print ('\033[1;31m'"       | || |_| | |_| | |__|_____|  _ < \ V / ")
print ('\033[1;31m'"       |_| \___/ \___/|_____|    |_| \_\ \_/ ")
print ("     ")
print ('\033[1;33m'"             TOOL BY VIMUKTHI HEWAGE")
print ("     ")
print ('\033[1;32m'"      [1] GRABCAM")
print ('\033[1;32m'"      [2] ZPHISHER")
print ('\033[1;32m'"      [3] ADVPHISHING")
print ('\033[1;32m'"      [4] PYPHISHER")
print ('\033[1;32m'"      [5] NEXPHISHER")
print ('\033[1;32m'"      [6] FREE FIRE")
print ('\033[1;32m'"      [7] CAMHACK")
print ('\033[1;32m'"      [8] YTDOWNLOADER")
print ("     ")
X = int(input('\033[1;34m'"Download Tool:"))
if (X == 1):
    os.system("cd /data/data/com.termux/files/home")
    os.system("git clone https://github.com/noob-hackers/grabcam.git && cd grabcam && bash grabcam.sh")
elif ( X == 2 ):
    os.system("cd /data/data/com.termux/files/home")
    os.system("apt update -y && apt upgrade -y && git clone https://github.com/htr-tech/zphisher.git && cd zphisher && bash zphisher.sh")
elif ( X ==3 ):
    os.system("cd /data/data/com.termux/files/home")
    os.system("apt update -y && apt upgrade -y && git clone https://github.com/Ignitetch/AdvPhishing.git && cd AdvPhishing/ && chmod 777 * && ./Android-Setup.sh && ./AdvPhishing.sh")
elif ( X ==4 ):
    os.system("cd /data/data/com.termux/files/home")
    os.system("pkg install git python -y && git clone https://github.com/KasRoudra/PyPhisher && cd PyPhisher && python3 pyphisher.py")
elif ( X ==5 ):
    os.system("cd /data/data/com.termux/files/home")
    os.system("apt update && apt install git -y && git clone git://github.com/htr-tech/nexphisher.git && cd nexphisher && bash setup && bash tmux_setup && bash nexphisher")
elif ( X ==6 ):
    os.system("cd /data/data/com.termux/files/home")
    os.system("pkg update -y && pkg upgrade -y &* pkg install git && git clone https://github.com/OnlineHacKing/FreeFire-Phishing.git && cd FreeFire-Phishing && chmod +x * && ./Android-Setup")
elif ( X ==7 ):
    os.system("cd /data/data/com.termux/files/home")
    os.system("apt update -y && apt upgrade -y && git clone https://github.com/Hack-The-World-With-Tech/Cam-Hack.git && cd Cam-Hack && ls && chmod +x * && ls && bash camhack.sh")
elif ( X ==8 ):
    os.system("cd /data/data/com.termux/files/home")
    os.system("git clone https://github.com/Isuruwaaa/tools.git && cd tools && pip install pafy && pip install youtube-dl && python YT2G.py")
