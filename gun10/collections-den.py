from collections import Counter

data = ["Ahmet","Mehmet","Ahmet","Cihan","İhsan","Ziya","Ziya","Ziya"]

data = Counter(data)

print(data.most_common(2))
z = Counter(a=1,b=2,ihsan=9)
print(list(z.elements()))
data3 = Counter("Kadir")
print(data3.most_common(2))
print(list(z))