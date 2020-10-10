from geometri.bangun_ruang import BangunRuang


class SegiTiga(BangunRuang):
    """Objek segitiga"""
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return f'Berikut merupakan class untuk segitiga dengan alas {self.alas} dan tinggi {self.tinggi}'

    def luas(self):
        return self.alas * self.tinggi / 2