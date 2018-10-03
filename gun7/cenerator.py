# import pdb debuging
# durmasını istediğimiz yerde (pdb.set_trace() )

def metod():
    data = []
    for i in range(0,1000):
        data.append(i)
        return data

# for i in metod():
#     print(i)


def metod2():
    data = []
    for i in range(0,2):
        data.append(i)
        yield i

for i in metod2():
    print(i)
