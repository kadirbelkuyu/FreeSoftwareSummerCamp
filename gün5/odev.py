
def tablo_ac(dosya):

    gelir_gider = {}
    with open(dosya,"r") as dosya2:
        satir = dosya2.read().split()
        for gel in satir.split("\n"):
            gel_tarih,gelir,gider,kalan = gel.split(" ")
            gelir_gider.update({gel_tarih: {"gelir":gelir,"giden":gider, "kalan":kalan}})
            return gelir_gider

def tut(gelirlistesi,dosya_ismi):
    with open(dosya_ismi, "w") as dosya:
        for gelir in gelirlistesi.items():
            gelir_bilgileri = gelir[1]

            gelirtarih = gelir[0]

            gelir = gelir_bilgileri.get('gelir')
            gider = gelir_bilgileri.get('gider')
            kalan = gelir_bilgileri.get('kalan')

            dosya.write(
                "{gelirtarihi} {gelir} {gider} {kalan}\n".format(
                   gelirtarihi=gelirtarih,
                    gelir=gelir,
                    gider=gider,
                    kalan=kalan

                )
            )

def menu():

    print("""
    
    Lütfen işlem numarasını seçiniz...
    1- gelirlerini gir...
    2- Giderleri gir...
    3- Kalan parayı gör...
    
    """)

    secim = input("Lütfen gerçekletirmek istediğiniz işlemin numarasını giriniz...")

    if secim.isnumeric() and int(secim) <= 3 and secim > 0:
        return secim
    else:

        print("\nHatalı işlem lütfen tekrar deneyin...")
        return menu()

def gelirgider_gir(geliir):

    gelir_tarihi = input("Gelirin Tarihi: ")
    gelir = input("Gelirini gir: ")
    gider = input("Giderleri gir: ")
    if geliir.get(gelir_tarihi,None) is not None:
        print("Bu ay zaten girilmiş")
        return gelirgider_gir(geliir)
    else:
        if gelir_tarihi.isnumeric() and gelir.isnumeric() and gider.isnumeric():
            yeni_gelir = {gelir_tarihi: {"gelir":gelir,"gider":gider}}
            print("Gelir kaydı başarılı...")
            return yeni_gelir
        else:
            print("Hatalı Girdi...")
            return gelirgider_gir()

def tablo_goster(gelir_tarihi,data):
    print("""
    
    gelir_tarihi {gelir_tarihi}
    gelir {gelir}
    gider {gider}
    kalan {kalan}
    
    """.format(
        tarih=gelir_tarihi,
        gelirt=data.gelir('gelir'),
        gidert=data.gider('gider'),
        kalan=data.kalan('kalan')

    ))


while True:

        tablo = menu()
        tablolistemizz = tablo_ac("tablo.txt")

        if tablo == 1:
            yeni = tut(gelirlistesi)
            tablolistemizz.update(yeni)






