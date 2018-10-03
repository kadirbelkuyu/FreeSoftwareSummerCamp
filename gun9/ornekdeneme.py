import calendar
import pprint
import time


def Year():

    try:
        while True:
            print("""
            Önce yılı girin sonra ayı
            çıkmak için q tuşuna basınız...
            """)
            islem = input("Devam etmek için bir tuşa basınız çıkmak içi q")
            if islem == "q" or islem == "Q":
                break
            else:
                pass
            year = int(input("Sene giriniz: : "))
            mon = int(input("Ayı giriniz: "))
            print(calendar.month(year,mon))



    except Exception as e:
        print("Kötüye kullanım denetleniyor...")
        time.sleep(2)
        pprint.pprint("Lütfen kötüye kullanmayalım kötü olduğunuz tespit edildi etik olmak iyidir kötüler kaybeder :-D !!!")


Year()