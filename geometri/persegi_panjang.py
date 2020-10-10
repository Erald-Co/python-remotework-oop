from geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):
    """ Objek persegi panjang """
    def __init__(self, p, l):
        self.p = p
        self.l = l
        # fungsi yang dipanggil pertama kali

    def info(self):
        ''' Memuat informasi mengenai objek persegi panjang'''
        return f'Modul menghitung rumus-rumus tentang persegi panjang dengan panjang {self.p} dan lebar {self.l}'

    def luas(self):
        """ Menghitung luas dari persegi panjang"""
        return self.p * self.l

