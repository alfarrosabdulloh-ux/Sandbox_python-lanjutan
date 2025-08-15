# Dictionary kosong
kontak = {}

# Tambah tiga kontak
kontak["Ibu"] = "08123456789"
kontak["Ayah"] = "08234567890"
kontak["Teman"] = "08345678901"

# Ubah nomor telepon Ibu
kontak["Ibu"] = "08111111111"

# Hapus Teman
kontak.pop("Teman")

# Cetak kontak akhir
print(kontak)
