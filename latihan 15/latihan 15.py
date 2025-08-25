# =========================
# Latihan 1: Membuat dan Mengakses
# =========================
biodata = {
    "nama": "Abdulloh Al-Farros",
    "umur": 17,
    "hobi": ["Ngoding", "Membaca", "Gaming"],
    "sudah_menikah": False
}

# Cetak seluruh dictionary
print("Seluruh biodata:", biodata)

# Cetak hanya value dari key "nama"
print("Nama:", biodata["nama"])

# Cetak hobi pertama
print("Hobi pertama:", biodata["hobi"][0])


# =========================
# Latihan 2: Modifikasi Dictionary
# =========================
# Tambahkan key-value baru "kota"
biodata["kota"] = "Jakarta"

# Ubah umur menjadi umur tahun depan
biodata["umur"] = biodata["umur"] + 1

# Cetak dictionary yang sudah diperbarui
print("Biodata diperbarui:", biodata)


# =========================
# Latihan 3: Penggunaan .get()
# =========================
# Coba akses key "pekerjaan" dengan bracket notation
# print(biodata["pekerjaan"])  # <-- Ini akan error karena key tidak ada

# Akses dengan .get()
print("Pekerjaan (tanpa default):", biodata.get("pekerjaan"))

# Akses dengan .get() + default
print("Pekerjaan (dengan default):", biodata.get("pekerjaan", "Pelajar"))


# =========================
# Latihan 4: Histogram Kata
# =========================
kalimat = input("Masukkan sebuah kalimat: ").lower()

# Ubah kalimat menjadi list kata
kata_list = kalimat.split()

# Buat dictionary histogram
histogram = {}
for kata in kata_list:
    histogram[kata] = histogram.get(kata, 0) + 1

# Cetak histogram
print("Histogram kata:", histogram)
