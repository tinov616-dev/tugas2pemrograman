class Produk:
    batas_diskon = 5000
    persen_diskon = 0.05

    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        print("Nama : ", self.nama)
        print("Harga : Rp", self.harga)

    def hitung_total(self, jumlah):
        return self.harga * jumlah

    def hitung_diskon(self, total):
        if total > self.batas_diskon:
            return total * self.persen_diskon
        return 0

    def hitung_total_akhir(self, jumlah):
        total = self.hitung_total(jumlah)
        return total - self.hitung_diskon(total)