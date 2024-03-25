# laptop Kelas Anak

from perangkat import Perangkat

class Laptop(Perangkat):
    def __init__(self, nama, merek, processor):
        super().__init__(nama, merek, 0)  # Harga default untuk laptop
        self.processor = processor

    def info(self):
        return f"{self.nama} adalah laptop merek {self.merek} dengan prosesor {self.processor}."
