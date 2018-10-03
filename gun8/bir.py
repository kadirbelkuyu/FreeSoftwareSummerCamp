"""

class DataModel():

    def edit(self,veri):
        if type(veri) == str:
            return veri.upper()
        else:
            return veri

    def __setattr__(self, key, value):
        print(key,value)
        value = self.edit(value)
        return object.__setattr__(self, key,value)

    def __getattribute__(self, item):
        return object.__getattribute__(self,item)

class DtaTable(DataModel):
    pass

    # username = "Kadir"
    # password = "lemyamca"

data = DtaTable()
data.kadir = "Hello"
print(data.kadir)

"""

class Insan():
    ozellikler = {"gozu":"Gri"}
    def __setattr__(self, key, value):
        self.ozellikler.update({key:value})

    def __getattribute__(self, item):
        if item != "ozellikler":
            if item.endswith("_feet"):
                return self.ozellikler.get(item[:-5]) / 0.3048
            else:
                return self.ozellikler.get(item)

    def save(self):
        print(self.ozellikler)

kadir = Insan
kadir.gozu = "Ela"
kadir.boy = 1.83
print(kadir.boy_feet)
print(feet)
kadir.ogrenci = True
kadir.save()