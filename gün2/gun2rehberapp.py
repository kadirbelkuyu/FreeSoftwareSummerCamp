import time
print(( "*" * 55))
print("KOSE TEKONOLOJİ İLEİŞİTİM HOŞGELDİNİZ")

kayıt_durum = input("Başvurunuzu yapmak için 1'e \n*************************************************** \n ÇIKMAK İSTİYORSANIZ QYA BASIN  ")

bilgiler = []

while True:
        if (kayıt_durum == "q") or (kayıt_durum == "Q"):
            print("Çıkış yapıyorsunuz")
            break

        elif (kayıt_durum == "1"):
            adınız = input("Adınızı giriniz: ")
            soyadınız = input("Soyadınızı giriniz: ")
            gsm = int(input("Numaranızı giriniz"))
            bilgiler.append({"ad":adınız,"soyad": soyadınız,"gsm" :gsm})
            break


istek_islem = input("Arama yapmak için 1'e basın \n Mesaj yazmak için 2'ye basın \n Hesabınızı Silme işlemleri için 3'e basınız. ")
if istek_islem == "1":
        karsi_no = input("Arayacağınız numarayı giriniz.")
        print("{} numarası aranıyor uygulamadan ayrılıyorsunuz.".format(karsi_no))
        time.sleep(1.5)
        print(" İyi günler dileriz")
if istek_islem == "2":
        karsi_no = input("Mesaj atacağınız numarayı giriniz.")
        mesaj = input("Mesajınızı giriniz:")
        print (mesaj)
        onay = input("Onaylamak için 1'e basın")
        if (onay == "1"):
            print("Mesajınız gönderiliyor...")
            time.sleep(1.5)
            print("Mesajınız gönderildi. Gönderilen Numara {} ; mesajınız {}".format(karsi_no,mesaj))

if istek_islem ==  "3":
    eminlik = input("Hesabınızı silmek ister misiniz? Onaylamak için e tuşuna basınız.")
    if eminlik == "E " or eminlik == "e":
        bilgiler.remove(bilgiler[0])
        print("Hesabınız silindi.")
    else:
        input("Yanlış tuşa bastınız")