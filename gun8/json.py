import json

bir_sozluk = {"meyvalar":{"yazmeyveleri":["karpuz","kavun","şeftali"],
                          "kismeyveleri":["portakal","elma","nar"]
                          }}

print((type(bir_sozluk)))
str_sozluk = json.dumps(bir_sozluk)
print(type(str_sozluk),str_sozluk)

