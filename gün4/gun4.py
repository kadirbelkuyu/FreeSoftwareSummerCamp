
def system_info():
    import sys
    print("Sistemde path olan python ana sürüm numarası", sys.version_info.major)
    print("Sistemde  path olan python alt sürüm numarası",sys.version_info.minor)

    print("işletim sistemi adı", sys.platform)

#system_info()

def hesap_makinesi():
    print("""
    Hesap makinesi
    1 toplama
    2 çıkarma
    3 çarpma
    4 bölme
    5 mod alma
    
    çıkmak için  q tuşuna basınız
    """)
    while True:
        işlem = input("Lütfen işlem numarasın gir: ")
        if işlem == "q" or işlem == "Q":
            print("Programdan çıkılıyor...")
            break
        a = (input("İlk sayıyı gir: "))
        b = (input("İkinci sayıyı gir: "))
        if işlem == "1":
            if type(eval("a,b") == int):
                print("Toplama işlemi")
                islem = int(a) + int(b)
                print("{} ile {} toplamı = {}".format(a, b, islem))
            else:
                print("Kullanıcıdan kaynaklanan bir hata meydana geldi...")
                break


        elif işlem == "2":
            print("Çıkarma işlemi")
            islem = a - b
            print("{} ile {} farkı = {}".format(a,b,islem))
        elif işlem == "3":
            print("çarpma işlemi")
            islem = a * b
            print("{} ile {} çarpımı = {}".format(a,b,islem))
        elif işlem == "4":
            print("Bölme işlemi")
            islem = a // b
            print("{} ile {} bölümü = {}".format(a,b,islem))
        elif işlem == "5":
            print("Kalan Hesaplama işlemi")
            islem = a % b
            print("{} ile {} bölündüğünde kalanı = {}".format(a,b,islem))
        else:
            print("Bir yanlışlık oldu sonra tekrar deneyin!!!")
            break


hesap_makinesi()

def fonk():
    x = range(int(input("Bir sayı gir: ")))
    return x
#print("fonksiyonun içindeki X sayısı:", fonk())

y = []
print("y nin ilk hali:", y)
def fonk1():
    print("eleman ekle")
    y.append(input("ekle"))
    return y
#print(y)
#fonk1()