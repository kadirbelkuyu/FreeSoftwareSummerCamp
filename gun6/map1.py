
eski_map = map
eski_filter = filter

def map(func,liste):
    sonuc = []
    for i in liste:
        sonuc.append(func(i))
    return  sonuc

def filter(func,liste):
    sonuc = []

    for i in filter:
        if func(i):
            sonuc.append(i)
    return sonuc

def twist(programmer):
    if programmer == "Kadir ":
        return True
    else:
        return False

kisiler = ["Kadir","Ahmet","Drya","Ayse"]

print(list(filter(twist,kisiler)))


# sayilar = ["1","2","3","4"]
# print(list(map(int,sayilar)))