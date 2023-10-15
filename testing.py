#MOGID KHAN
import string,random,os

def mktUA():
  brand=["SM-","GT-","RMX","CPH","MG","SC-","Redmi ","moto g","Nokia X"]
  model=f"{random.choice(brand)}{random.randint(50,100000)}{random.choice(string.ascii_letters)}"
  d1=f"Dalvik/2.1.0 (Linux; U; Android {random.randint(1,18)}; {model} Build/OPM4.579514.034) "
  u1= f"[FBAN/FB4A;FBAV/{random.randint(50,10000)}.0.0.808.96;[FBAN/FB4A;FBAV/{random.randint(50,10000)}.0.0.88.96;[FBAN/FB4A;FBAV/{random.randint(50,10000)}.0.0.88.96;FBBV/{random.randint(1000000,99999999999)};FBRV/0;FBPN/com.facebook.katana;FBLC/np_PK;FBMF/blueberry;FBBD/Sony;FBDV/{model};FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.0,width="+f"{random.randint(144,5000)},height={random.randint(760,8000)}"+"};FB_FW/1;]"
  x2=d1+u1[:30]+f"[FBAN/FB4A;FBAV/{random.randint(50,10000)}.0.0.88.96;[FBAN/FB4A;FBAV/{random.randint(50,10000)}.0.0.88.96;[FBAN/FB4A;FBAV/{random.randint(50,10000)}.0.0.88.96;FBBV/{random.randint(1000000,99999999999)};FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/{model};FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.0,width="+f"{random.randint(144,5000)},height={random.randint(760,8000)}"+"};FB_FW/1;]"
  return x2

def line():
  return "\x1b[1;94m"+"━"*40+"\x1b[0;1m"
os.system("clear")
print(f"""\x1b[1;94m

db    db  .d8b.  
88    88 d8' `8b 
88    88 88ooo88 
88    88 88~~~88 
88b  d88 88   88 
~Y8888P' YP   YP

{line()}
\x1b[0;1m""")

for i in range(10):
  print("\x1b[1;92m",mktUA(),"\x1b[0;1m")
  print(line())