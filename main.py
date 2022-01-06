from playsound import playsound
import time
import requests
from bs4 import BeautifulSoup
iteration=1
# isi indeks yang dah keluar
temp_indeks=0

while True:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
    URL = "Isi url"
    page = requests.get(URL, headers={"cookie":"isi cookie","user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
    # print(page)
    soup = BeautifulSoup(page.content, "html.parser")
    # #Isi Array matkul
    scrapper = soup.find_all("p",  {"class": ["small"]})
    kuota = scrapper[0].text.split(" ")[1]
    pendaftar = scrapper[1].text.split(" ")[1]
    print(scrapper[0].text)
    print(scrapper[1].text)
    if(int(pendaftar)<int(kuota)):
        playsound('./hawaii_aloha_oe.mp3')
    print("Banyak iterasi",iteration)
    iteration+=1
    time.sleep(1*60)

