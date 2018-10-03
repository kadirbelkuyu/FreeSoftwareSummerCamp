"""
print(( "*" *35))
print("Hoşgeldiniz Flim kayıt programına")
print("")
print(( "*" * 35))
filim = {}
while True:
    print("Bir işlem seçiniz")
    print("1- Yeni filim ekle")
    print("2- filim sil")
    print("3- görüntüle")

    islem = int(input("Lütfen seçinimizi yapınız:"))
    print("")

    if islem == "q" or islem == "Q":
        break
    elif islem == 1:
        ad = input("Filmin adını giriniz: ")
        if type(ad) == type(int):
            print("Lütfen str değer giriniz!!!")
            break
        tar = input("Filmin Tarihini giriniz: ")
        oyuncu = []
        oyuncu_say = int(input("Oyuncu sayısını giriniz: "))
        for i in range(oyuncu_say):
            oyuncu.append(input("Oyuncu isimlerini giriniz"))
        filim.update({"Filim adı": ad, "filimin tarihi ": tar,"filimin oyuncuları":oyuncu})
        print(filim)
        print("")

    elif islem == 2:
        print("işleminiz gerçekleştiriliyor...")
        filim.clear()
        print("")
        print("filimler silindi...")
        print("")
    elif islem == 3:
        print("data getiriliyor...")
        print("")
        print(filim)
        print("")

"""""

# Fonksiyonlar


