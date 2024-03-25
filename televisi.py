# televisi Kelas Anak

from perangkat import Perangkat

class Televisi(Perangkat):
    def __init__(self, nama, merek, ukuran):
        super().__init__(nama, merek, 0)  # Harga default untuk televisi
        self.ukuran = ukuran

    def info(self):
        return f"{self.nama} adalah televisi merek {self.merek} dengan ukuran {self.ukuran} inch."
