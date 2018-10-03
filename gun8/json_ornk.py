import string as stg
import random
import json


class Keepass():
    dosya_ismi = None
    parolalist = []

    def __init__(self, dosya_ismi):
        self.dosya_ismi = dosya_ismi
        while True:
            menu = self.input_error("""
            Lütfen İşlem seçiniz:
            1 - Yeni parola oluştur
            2 - Parolaları listele
            3 - Parola ara
            4 - Çıkış yap
            """,is_numeric=True)
            if menu == 4:
                return
            if menu == 1:
                self.register_new_pass()
            elif menu == 2:
                self.list()
            elif menu == 3:
                key = self.input_error("Arama Kriteri :")
                self.search(key)
            else:
                print('Hatalı Girdi')



    def input_error(self,text,is_numeric=False):
        input_errors = True
        while input_errors:
            input_data = input(text)
            if input_data.strip() != "":
                if is_numeric:
                    if input_data.isnumeric():
                        return int(input_data)
                    else:
                        print('Geçersiz girdi')
                else:
                    return input_data
            else:
                print('Geçersiz girdi')



    def register_new_pass(self):
        """
        Kullanıcıdan kullanıcı adı , açıklama ve parola ister
        eğer parola boş ise kendisi random bir parola oluşturur
        oluşturulacak parola uzunluğunu da kullanıcıdan isteyeceğiz
        """
        username = self.input_error("Lütfen Kullanıcı adı giriniz :")
        password = input("Lütfen parolanızı giriniz:")
        if password.strip() == "":
            password_length = self.input_error('Lütfen parola uzunluğu giriniz',is_numeric=True)
            password = self.generate_pass(password_length)
        aciklama = self.input_error("Lütfen açıklama giriniz :")



        self.parolalist.append({"username":username,"password":password,"description":aciklama})
        self.save()

    def edit(self):
        """
         verilen index'te olan veriyi değiştirir
        """

    def load(self):
        """
        verdiğimiz dosya isminine bakarak okuma yapacak
        """
        with open(self.dosya_ismi) as file:
            file_data = file.read().strip().split("\n")
            json.dump(self.dosya_ismi)
            for veriler in self.dosya_ismi:
                veri_yigini = veriler.split("@ayrac@")
                self.parolalist.append(
                    {"username": veri_yigini[0],
                     "password": veri_yigini[1],
                     "description": veri_yigini[2]})

    def list(self):
        """
        parolalarımızı listeleyecek

        """
        for passlist in self.parolalist:
            print(list(passlist.values()))

    def search(self,keyw):
        """
        vericeğimiz parametreye göre parolalar arasında arama yapacak
        """
        for passlist in self.parolalist:
            if keyw in list(passlist.values()):
                print(list(passlist.values()))

    def save(self):
        """
        dosyaya kayit yapacak
        """
        data = ""
        for i in self.parolalist:
            data += "{username}@ayrac@{passw}@ayrac@{desc}\n".format(username=i.get('username'),passw=i.get('password'),desc=i.get('description'))
        with open(self.dosya_ismi,"a") as file:
            file.write(data)
        json.dump(self.dosya_ismi)



    def generate_pass(self, length):
        string_data = stg.printable
        return ''.join([string_data[random.randint(0, len(string_data) - 1)] for i in range(0, length)])


kep = Keepass("deneme.txt")
print(kep.generate_pass(10))