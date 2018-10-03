
import string

fonk = lambda a,b: a+b
print(fonk(4,5))

harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
harfler2 = string.ascii_lowercase
cevirim = {i:harfler2.index(i) for i in harfler2}
isimler = ["kadir","ahmet",
           "ali","veli"
           "mehmez","zehra"
           ]
print(sorted(isimler,key=lambda x: cevirim.get(x[0])))


