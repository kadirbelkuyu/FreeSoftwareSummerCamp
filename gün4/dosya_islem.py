"""
dosya = open("kadir.txt","w")
dosya.write("Hello world")
dosya.close()

with open("Belkuyu.txt","w") as dosya2:
    dosya2.write("Test Metni") #Önerilen kullanım

    """

# og_no = input("Lütfen ögrenci numaranızı giriniz: ")
# vize = input("Lütfen vizenizzi giriniz: ")
# vize2 = input("Lütfen vize 2nizi giriniz: ")
# final = input("Lütfen finalinizzi giriniz: ")
#
# with open("ogr_info.txt","a") as ogrenci_info:
#    ogrenci_info.write("{ogrencinumarası} {vize} {vize2} {final}\n".format(
#        ogrencinumarası=og_no,
#        vize=vize,
#        vize2=vize2,
#        final=final
#    ))

def ogrencileri_ac(dosya):
    ogrenciler = {}
    with open(dosya,"r") as dosya2:
        satirlarimiz = dosya2.read().strip()
        for ogrenci in satirlarimiz.split("\n"):
            og_no,vize,vize2,final = ogrenci.split(" ")
            ogrenciler.update({og_no:{
                "vize1":vize,
                "vize2":vize2,
                "final":final
            }})
    return(ogrenciler)


# with open("gvr","r") as dosya3:
#     dosya3.seek(0)
#     print(dosya3.read(10))
#     print(dosya3.read(10))
#     dosya3.seek(0) # cursor yer belirtiyor
#     print(dosya3.tell()) # cursorun yerini söylüyor





#
# def menu():
#
#     print("""
#     Lütfen İşleminizi seçiniz
#
#     1- Öğrenci ekle
#     2- öğrenci listele
#     3- öğrenci ara
#     4- öğrenci sil
#     """)
#     secim = input("İşlem: ")
#     if secim.isnumeric() and int(secim) <5 and int(secim) > 0 :
#         return int(secim)
#     else:
#         print("İşlemde bir hata oluştu değeri kontrol et")
#         return menu()
#
# def ogrencigir(ogrenciler):
#     ogrenci_no = input("Ogrenci No:")
#     vize1 = input("Vize1: ")
#     vize2 = input("Vize2: ")
#     final = input("Final: ")
#     if ogrencilistemiz.get(ogrenci_no, None) is not None:
#         print("Girdiğiniz bilgi sistemde zaten var")
#     else:
#
#
# while True:
#     menu_no = menu()
#     ogrencilistemiz = ogrencileri_ac("ogr_info.txt")
#     if menu_no == 1:
#
#
#
#
# menu()


from pprint import pprint


def ogrencileri_ac(dosya):
    ogrenciler = {}
    with open(dosya, "r") as dosya2:
        satirlarimiz = dosya2.read().strip()
        for ogrenci in satirlarimiz.split("\n"):
            ogrencino, vize1, vize2, final = ogrenci.split(" ")
            ogrenciler.update({ogrencino: {"vize1": vize1, "vize2": vize2, "final": final}})
    return ogrenciler


def kaydet(ogrencilistesi,dosya_ismi):
    with open(dosya_ismi, "w") as dosya:
        for ogrenci in ogrencilistesi.items():
            ogrenci_bilgileri = ogrenci[1]
            ogr_no = ogrenci[0]
            vize1 = ogrenci_bilgileri.get('vize1')
            vize2 = ogrenci_bilgileri.get('vize2')
            final = ogrenci_bilgileri.get('final')

            dosya.write(
                "{ogrencino} {vize1} {vize2} {final}\n".format(ogrencino=ogr_no,
                                                               vize2=vize2,
                                                               vize1=vize1,
                                                               final=final))


def menu():
    print("""
Lütfen işleminizi seçiniz
    1- Öğrenci Ekle
    2- Öğrenci Listele
    3- Öğrenci Ara
    4- Öğrenci Sil
    """)
    secim = input("İşlem :")

    if secim.isnumeric() and int(secim) < 5 and int(secim) > 0:
        return int(secim)
    else:
        print("Hatalı seçim yaptınız")
        return menu()


def ogrencigir(ogrenciler):
    ogrenci_no = input('Ogrenci No:')
    vize1 = input('Vize 1:')
    vize2 = input('Vize 2:')
    final = input('Final :')
    if ogrenciler.get(ogrenci_no, None) is not None:
        print("Girdiğiniz bilgisi zaten sistemde var")
        return ogrencigir(ogrenciler)
    else:
        if vize1.isnumeric() and vize2.isnumeric() and final.isnumeric():

            yeni_ogrenci = {ogrenci_no: {"vize1": vize1, "vize2": vize2, "final": final}}
            print('Öğrencinizin Kaydı Yapıldı!!!!')
            return yeni_ogrenci


        else:
            print('Hatalı girdi yaptınız')
            return ogrencigir(ogrenciler)

def ogrenci_goster(ogrencino,veri):
    print("""
                No : {no}
                Vize 1: {vize1}
                Vize 2: {vize2}
                Final : {final}
                """.format(no=ogrencino, vize1=veri.get('vize1'), final=veri.get('final'),
                           vize2=veri.get('vize2')))

while True:
    menu_no = menu()
    ogrencilistemiz = ogrencileri_ac("ogr_info.txt")
    if menu_no == 1:
        yeni = ogrencigir(ogrencilistemiz)
        ogrencilistemiz.update(yeni)
        kaydet(ogrencilistemiz,"ogr_info.txt")
    elif menu_no == 2:
        for ogrenci in ogrencilistemiz.items():
            ogrenci_goster(ogrenci[0],ogrenci[1])

    elif menu_no == 3:
        ogrenci_no = input('Öğrenci Numarası Giriniz:')
        ogrenci = ogrencilistemiz.get(ogrenci_no,None)
        if ogrenci is not None:
            ogrenci_goster(ogrenci_no,ogrenci)
        else:
            print('Öğrenci Bulunamadı')
    elif menu_no == 4:
        ogrenci_no = input('Öğrenci Numarası Giriniz:')
        ogrenci = ogrencilistemiz.get(ogrenci_no, None)
        if ogrenci is not None:
            ogrencilistemiz.pop(ogrenci_no)
            kaydet(ogrencilistemiz, "ogr_info.txt")
        else:
            print('Öğrenci Bulunamadı')
