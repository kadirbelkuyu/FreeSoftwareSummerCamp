
liste1 = ["string",1,2,3,1.2,{"z":"x"},[[2,3]]]

print(liste1)
liste1.append("deneme")
print(liste1)
print(liste1.pop(0))
liste1.remove(1.2)
print(liste1)
print(liste1.count(1))
print(liste1.index(1))
liste2 = [1,2,3,4,5,6,78,-3]
liste2.sort()
print(liste2)
liste2.sort(reverse=True)
print(liste2)
liste2.insert(1,99)
print(liste2)
liste2.extend([12,13,14,15])
print(liste2)
copyden = liste2.copy()
print("Kopyaladığım list",copyden)
print(liste2[3:])
print(liste2[1:3])
print(liste2[:3])
print(liste2[1:5:2])
print(liste2[:-1])
print(len(liste2))

