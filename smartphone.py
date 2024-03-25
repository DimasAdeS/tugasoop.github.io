# smartphone Kelas Anak

from perangkat import Perangkat

class Smartphone(Perangkat):
    def __init__(self, nama, merek, sistem_operasi):
        super().__init__(nama, merek, 0)  # Harga default untuk smartphone
        self.sistem_operasi = sistem_operasi

    def info(self):
        return f"{self.nama} adalah smartphone merek {self.merek} dengan sistem operasi {self.sistem_operasi}."
