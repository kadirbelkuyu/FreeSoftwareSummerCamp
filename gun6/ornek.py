class Canli():
    dogumu = ""
    kilosu = 0
    aclik = 0
    susuzluk = 0

    def __init__(self,dogumu,kilosu,aclik,susuzluk):
        self.dogumu = dogumu
        self.kilosu = kilosu
        self.aclik = aclik
        self.susuzluk = susuzluk

    def hareket(self,mesafe):
        self.enerji -= mesafe *2



