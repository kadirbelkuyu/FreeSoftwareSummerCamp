from functools import reduce


def birlestir(birinci, ikinci):
    return birinci + " " + ikinci


kisiler = ["kadir", "Ali", "mehmet", "deneme"]
print(reduce(birlestir, kisiler))


def ucus(rakam1, rakam2):
    return rakam1 * rakam2


rakamlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(reduce(ucus, rakamlar))
