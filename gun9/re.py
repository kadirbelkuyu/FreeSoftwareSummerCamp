import re
import pprint
x = """
sdjngliengeiiwri3ljğ4uk<mfdinkdl<fnni
lkbugrhgoığjownfmkhisknh
skjıou849uç<dömfwwlieıoru983333*92lind<vknf


"""
print(re.search("\D(\d\d\d)\D",x).group(1))


"""
\d = sayı
\D = sayı olmayan
\w = harf
\W = Harf olmayan
"""

with open("dosya.fastq") as f:
    dosya_icerigi = f.read()
sonuc = re.findall("^@chr(\d+):(\d+):\w+:-?\d+\/d+$",dosya_icerigi,flags=re.IGNORECASE|re.MULTILINE)
my_list = []

for chrom,pos,drection in sonuc:
    ham_posision = int(pos)
    if drection == "R":
        ham_posision = ham_posision * -1
    my_list.append(int(chrom), ham_posision)

pprint.pprint(sorted(my_list))