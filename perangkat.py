# perangkat Kelas Induk

from elektronik import Elektronik

class Perangkat(Elektronik):
    def __init__(self, nama, merek, harga):
        super().__init__(nama, merek)
        self.harga = harga

    def info(self):
        return f"{self.nama} adalah perangkat merek {self.merek} dengan harga {self.harga} USD."
