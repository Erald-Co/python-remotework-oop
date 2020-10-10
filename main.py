from geometri.persegi_panjang import PersegiPanjang
from geometri.segitiga import SegiTiga

print("Menggunakan OOP")
p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.luas())

st1 = SegiTiga(2,1)
print(st1.info())
print(st1.luas())