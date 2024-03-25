# Elektronik Kelas Induk

class Elektronik:
    def __init__(self, nama, merek):
        self.nama = nama
        self.merek = merek

    def info(self):
        return f"{self.nama} adalah produk merek {self.merek}."
