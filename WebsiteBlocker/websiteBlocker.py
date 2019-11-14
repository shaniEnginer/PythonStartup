

#  path To host file 
import time
from datetime import datetime as dt
host_file=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
web_sites=['facebook.com' , 'www.facebook.com']


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,17) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print('Working hours ----')
        with open('hosts.txt' ,'r+') as h_file:
            content=h_file.read()
            for website in web_sites:
                if website in content:
                    pass
                else:
                    h_file.write(redirect+" "+website+"\n")



            
    else:
        with open('hosts.txt','r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in web_sites):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)



   