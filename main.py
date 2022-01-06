import time
import requests
from bs4 import BeautifulSoup
import os
iteration=1
from os import environ as env
from dotenv import load_dotenv
load_dotenv()

while True:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
    page = requests.get(env["URL_MK"], headers={"cookie":env["COOKIE"],"user-agent":env["USER_AGENT"]})
    soup = BeautifulSoup(page.content, "html.parser")
    kelas=int(env["KELAS"])-1
    scrapper = soup.find_all("p",  {"class": ["small"]})
    kuota = scrapper[kelas*2].text
    pendaftar = scrapper[kelas*2-1].text
    print(kuota)
    print(pendaftar)
    host_os=env["OS"]
    command="start"
    if (host_os=="MAC"):
        command="open"
    if(int(pendaftar.split(" ")[1])<int(kuota.split(" ")[1])):
        os.system("{} https://www.youtube.com/watch?v=dQw4w9WgXcQ".format(command))
    print("Banyak iterasi",iteration)
    iteration+=1
    #Lama Jeda dalam detik
    time.sleep(60)

