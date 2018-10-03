import subprocess
import time
# subprocess.run(["ls","-l"])
# subprocess.run(["df","-h"])

# oute = subprocess.run(["df","-h"],stdout=subprocess.PIPE)
# print(oute.stdout)
# print(oute.stdout.decode("utf-8"))

gecmis_islem =""
while True:
    p1 = subprocess.run(["dmesg"], stdout=subprocess.PIPE)
    p2 = subprocess.run(["grep","usb"], stdin=p1.stdout,stdout=subprocess.PIPE)
    p1.stdout.close()
    output = p2.communicate()[0]
    son_satir = output.decode("utf-8").split("\n")[-2]
    son_islem = son_satir.split("[")[1].split("]")[0]
    if gecmis_islem != son_islem:
        gecmis_islem = son_islem
        print(son_satir)
    time.sleep(2)
