# Utama (mengimpor kelas-kelas tsb)

from televisi import Televisi
from laptop import Laptop
from smartphone import Smartphone

tv1 = Televisi("Smart TV", "Samsung", 55)
laptop1 = Laptop("Notebook", "Lenovo", "Intel Core i7")
phone1 = Smartphone("Galaxy S21", "Samsung", "Android")

print(tv1.info())
print(laptop1.info())
print(phone1.info())
