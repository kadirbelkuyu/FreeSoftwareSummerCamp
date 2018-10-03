kisiler = []

while True:
    print("Bir işlem seçiniz")
    print("1- Yeni kişi ekle")
    print("2- kişiyi Düzenle")
    print("3- Kişiyi Sil")
    islem =  int(input("Lütfen seçinimizi yapınız:"))

    if islem == 1:
        ad = input("Ad : ")
        soyad = input("soyad : ")
        tel = input("tel : ")
        email = input("email : ")
        kisiler.append({"Ad": ad,"soyad":soyad, "tel:":tel,"email":email})
        input ("işleminiz gerçekleşti \n devam etmek için bir  tuşa basınız")
    elif islem == 2:
        aranacak = input("Aranacak Kelimeyi Giriniz:")
        temp_kisi = None
        for kisi in kisiler:
            for value in kisi.values():
                if aranacak.strip() == value:
                    temp_kisi = kisi

        if temp_kisi is not None:
            kisi_index = kisiler.index(temp_kisi)

        else:
            input("Aradığınız veriden bir eşleşme yok \n bir tışa basınız")
