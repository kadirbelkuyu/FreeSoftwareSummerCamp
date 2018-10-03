x = "Kadir"
y = "Belkuyu"

if x != y:
    print(x,y)


    
sozluk = {"x":"y"}

if sozluk.get("y") is None:
    print("z var")
else:
    print("z yok")
    print(sozluk.get("z"))
    
print(sozluk.get("y",":)"))

"""
Loops
"""

for i in range(0,11):
    print("Deger",i)

liste = ["Kadir","furkan","Mr.Robot","Ayşe"]
sayaç = 0

while sayaç < len(liste):
    if liste[sayaç] != "Mr.Robot":
        isim = liste[sayaç]
        print("Hoşgeldin {}".format(isim))
    else:
        soru = input("İsim Gir")
        print("Sana da Merhaba {}".format(soru))
    sayaç += 1

