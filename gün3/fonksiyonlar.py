"""
def toplama(a=0,b=0):
    return a + b
print(toplama(1,2))
"""

def fonk1(*args):
    print(args)
def fonk2(**kwargs):
    print(kwargs)

#fonk1(1,2,3,4,5,6)
#fonk2(deneme="Test",deneme2="Kadir")

def fonk3(*args, **kwargs):
    print(args)
    print(kwargs)

#fonk3([1,2,3,4,5,6],(7,8,9),test1="Hello",test2="World")


def yazdır(*args):
    bitirici = args[-1]
    ayirici = args[-2]
    yazilacak = args[:-2]
    # for kelime in yazilacak:
    #     print(kelime,end='' )

    print(*yazilacak,sep=ayirici,end=bitirici)


#yazdır("Kadir","ali","Deneme","bitiş")

def kwards_yazdir(*args, **kwargs):

    print(*args, sep=kwargs.get('ayirici'), end=kwargs.get('bitirici'))

kwards_yazdir("Kadir","Ahmet", "Ali",ayirici='!!!',bitirici='bitiş')



