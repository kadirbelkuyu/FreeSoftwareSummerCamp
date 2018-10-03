def hosgeldin():
    print("********HOSGELDIN***********")
    print("1- Ekle")
    print("2- Cikar")
    print("3- Cüzdan")
    print("***************************")
    gel = input("islem seciniz: ")
    islem(gel)

def islem(menu):
    if menu == "1":
        print("***************************")
        gel = input("eklenecek: ")
        if gel.isnumeric():
            ekle(gel)
        else:
            print("gecerli değil")
    elif menu =="2":
        print("***************************")
        gel = input("cikacak: ")
        if gel.isnumeric():
            cikar(gel)
        else:
            print("gecerli değil")
    elif menu =="3":
        cuzdan()
    else:
        print("Hatalı islem")


def ekle(gel):
    with open("data","a") as table:
        table.write("+"+gel+"\n")
        print("Gelir Eklendi Ana Sayfaya Gidiyorsun")

def cikar(gel):
    with open("data","a") as table:
        table.write("-"+gel+"\n")
        print("Gider Eklendi Ana Sayfaya Gidiyorsun")
def cuzdan():
    gelir =[]
    gider =[]
    gelirt=0
    gidert=0
    with open("data", "r") as table:
        main = table.read().strip()

    for kayit in main.split("\n"):
        if kayit[:1] == "+":
            gelir.append(kayit[1:])
        else:
            gider.append(kayit[1:])

    for i in gelir:
        gelirt+=float(i)
    for i in gider:
        gidert+=float(i)
    print("*********cuzdan********")
    print(gelirt-gidert)
while True:
    hosgeldin()
