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
    URL = "https://akademik.itb.ac.id/app/mahasiswa:<NIM>/statusmhs"
    page = requests.get(URL, headers={"cookie":"<isi cookie>","user-agent":"<isi agent>"})
    soup = BeautifulSoup(page.content, "html.parser")
    #Isi Array matkul
    matkuls = ["RPL","Lasti","AKE","IMK","Sismul","TST"]
    scrapper=soup.find_all("td",  {"class": ["text-center"]})
    count=0
    indeks_keluar=0
    matkul_baru=""
    for i in range (len(scrapper)):
        if(i % 3 == 2 ):
            print("{matkul},{indeks}".format(matkul=matkuls[count], indeks=scrapper[i].text))
            if (scrapper[i].text !=""):
                indeks_keluar+=1
                matkul_baru=matkuls[count]
            count+=1
    if indeks_keluar>temp_indeks :
        temp_indeks+=1
        playsound('./hawaii_aloha_oe.mp3')
    print("Persentase indeks",indeks_keluar/len(matkuls)*100,"%")
    print("Banyak iterasi",iteration)
    iteration+=1
    time.sleep(5*60)

