
class Deneme():
    def __getattribute__(self, item):
        print(item,"çekildi")
    def __setattr__(self, key, value):
        print(key,"veritutucusuna",value,"değeri atandı")


dene = Deneme()
dene.boy = 1.83
boyu = dene.boy
print(dene.__dict__)

