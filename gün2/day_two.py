# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 09:50:33 2018

@author: kadirbelkuyu
"""
"""
class Toplama():

    def __init__(self):


#%%

def yearcenturty(year):
    """
    # year to centurty
    """

    str_year = str(year)

    if(len(str_year)<3):
        return 1
    elif(len(str_year) == 3):
        if(str_year[1:3] == "00"):
            return int(str_year[0])
        else:
            return int(str_year[0])+1
    else:
        if(str_year[2:4] == "0"):
            return int(str_year[:2])
        else:
            return int(str_year[:2])+1


#%%


def uclu_carpma(a=0,b=0,c=0):
    return a *b * c
print(uclu_carpma(c=1,a=2))

#%%

def value_to_key(dict_object,value):
    for i in dict_object.items():
        if i[1] == value:
            return i[0]

abc = value_to_key({"Ahmet":"İhsan","Yontar":"Kadir}, "İhsan")
print(abc)

#%%

sozluk = {"vize":85,"final":50}

for i in sozluk.items():
    print(i)



def value_to_key(dict_objesi,value):
    for obje in dict_objesi.items():
        if obje[1] == value:
            return obje[0]

print(value_to_key(sozluk,40))



#%%
import time


işlem = input("Lütfen yapacağınız işlemi giriniz: ")
reh = []

while True:


    if işlem == "q" or işlem == "Q":
        print("Gene Bekleriz")
        time.sleep(2)
        break

    elif işlem == "1":
        print("Yeni Kayıt için hoş geldiniz: ")
        num = int(input("Numaranızı Giriniz: "))
        ad = input("Adınızı Giriniz: ")
        soyad = input("Soyadı giriniz: ")
        reh = ({"num":num,"ad":ad,"soyad":soyad})
        print(reh)

    elif işlem == "2":
        sil = int(input("Kaydı sileceğiniz kişinin numarasını giriniz: "))
        emin = input("Numarayı silmek istediğinize eminmisiniz: ")
        if emin == "e":
            print("Siliniyor...")
            time.sleep(2)
            print("silindi :/")
            break
    else:
        print("Büyük ihtimalle Hata var İşlem gerçekleştirilemiyor!!!")

istek_islem = input("Aramak için 1 - Mesaj için 2 çıkmak için n tuşlarına basınız: ")
while True:


    if istek_islem == "1":
        ara = int(input("Aramak istediğiniz numarayı giriniz: "))
        print("Çalıyor...")
        time.sleep(4)
        print("numaraya ulaşılamıyor...")
        break
    else:
        print("service not Connect")
        break


#%%



class Kisi:
    def __init__(self,tcno, adi,soyadi,sehir, meslek, tel, adres):
        self.tcno = tcno
        self.adi = adi
        self.soyadi = soyadi
        self.sehir = sehir
        self.meslek = meslek
        self.tel = tel
        self.adres = adres


    def rapor(self):
        print "Adi    :", self.adi
        print "Soyadi :", self.soyadi
        print "TC No  :", self.tcno
        print "Sehir  :", self.sehir
        print "Meslek :", self.meslek
        print "Telefon:", self.tel
        print "Adres  :", self.adres

    def csv(self, ayirac = ";"):
        a = ayirac
        b = self.adi + a
        b += self.soyadi + a
        b += self.tcno + a
        b += self.sehir + a
        b += self.meslek + a
        b += self.tel + a
        b += self.adres
        return b

class Rehber:
    def __init__(self, adi):
        self.adi = adi
        self.kisiler = {}

    def ekle(self, kisi):
        self.kisiler[kisi.tcno] = kisi


    def rapor(self):
        print ("-" * 50)
        print self.adi, "  Rehberi"
        print "-" * 50
        for tcno, kisi in self.kisiler.items():
            kisi.rapor()
            print "-" * 50

    def csv(self):
        print ("adi;soyadi;tcno;sehir;meslek;tel;adres")
        for tcno, kisi in self.kisiler.items():
            print kisi.csv()



if __name__ == "__main__":
    r = Rehber("Ev Telefon")
    a = Kisi("1", "Nurullah", "Caliskan", "Mugla","Ogrenci","0000","Mugla/Milas")
    b = Kisi("2", "Abdullah", "Caliskan", "Mugla","Ogrenci","0100","Mugla/Milas")
    c = Kisi("3", "Ilker", "Manap", "Stokholm","Muhendis","00230","Stokholm/Alvsjo")
    r.ekle(a)
    r.ekle(b)
    r.ekle(c)
    r.csv()
r.rapor()

"""




#%%

kişiler = []

while True:
    
    print("""
    Bir işlem seçiniz
    1- yenş kişi ekle
    2- kişiyi düzenle
    3- kişiyi sil
    """)
    islem = input("Lütfen seçiminizi yapınız: ")
    if islem.isnumeric():
        islem = int(islem)
    if islem == 1:
        ad = input("ad: ")
        soyd = input("soyad: ")
        tel = input("tel: ")
        email = input("email: ")
        kişiler.append({"ad":ad,
                        "soyad": soyd,
                        "tel": tel,
                        "email": email
                        })
        input("işleminiz gerçekleşti devam etmek için bir tuşa basınız: ")
    elif islem == 2:
        aranaccak = input("Aranacak Kişiyi giriniz: ")
        temp_kisi = None
        for kisi in kişiler:
            for value in kisi.values():
                if aranaccak.split() == value:
                    temp_kisi = kisi

        if temp_kisi is not None:
            kisi.index = kişiler.index(temp_kisi)

        else:
            input("Aradığınız veride bir eşleşme yok devam etmek için klavyeden bir tuşa basınız: ")


















































