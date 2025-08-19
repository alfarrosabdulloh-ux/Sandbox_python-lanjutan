# Latihan 2: Class RekeningBank
class RekeningBank:
    def __init__(self, nomor_rekening, nama_pemilik):
        self.nomor_rekening = nomor_rekening
        self.nama_pemilik = nama_pemilik
        self.saldo = 0

    def lihat_saldo(self):
        print(f"Saldo saat ini: Rp{self.saldo}")

    def setor(self, jumlah):
        self.saldo += jumlah
        print(f"Berhasil setor Rp{jumlah}. Saldo sekarang: Rp{self.saldo}")

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi")
        else:
            self.saldo -= jumlah
            print(f"Berhasil tarik Rp{jumlah}. Saldo sekarang: Rp{self.saldo}")


# Membuat object rekening
rekening_budi = RekeningBank("1234567890", "Budi")

# Menggunakan method
rekening_budi.lihat_saldo()
rekening_budi.setor(500000)
rekening_budi.setor(250000)
rekening_budi.tarik(200000)
rekening_budi.tarik(700000)  # ini harus gagal karena saldo kurang
rekening_budi.lihat_saldo()
