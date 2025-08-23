# ================================
#  APLIKASI POLLING SEDERHANA
# ================================

# Struktur data survei
SURVEI = [
    {
        "pertanyaan": "Apa bahasa pemrograman favoritmu?",
        "opsi": ["Python", "JavaScript", "Java", "C++"]
    },
    {
        "pertanyaan": "Apa sistem operasi yang paling sering kamu gunakan?",
        "opsi": ["Windows", "macOS", "Linux"]
    },
    {
        "pertanyaan": "Tim mana yang akan menang di final piala dunia?",
        "opsi": ["Argentina", "Prancis", "Brasil", "Jerman"]
    }
]

# Inisialisasi hasil polling dengan 0 suara
hasil_polling = {}
for item_survei in SURVEI:
    for opsi in item_survei["opsi"]:
        hasil_polling[opsi] = 0

print("============================================")
print(" SELAMAT DATANG DI APLIKASI POLLING")
print("============================================")

# Loop utama untuk setiap pertanyaan
for idx, item_survei in enumerate(SURVEI, start=1):
    print(f"\nPertanyaan {idx}: {item_survei['pertanyaan']}")
    for opsi in item_survei["opsi"]:
        print(f" - {opsi}")

    # Validasi input
    while True:
        jawaban = input("Jawaban Anda: ")
        if jawaban in item_survei["opsi"]:
            print(f"> {jawaban}")
            print("--- Terima kasih! ---")
            hasil_polling[jawaban] += 1
            break
        else:
            print(f"> {jawaban}")
            print("Jawaban tidak valid. Silakan pilih dari opsi yang tersedia.")

# Menampilkan hasil akhir polling
print("\n============================================")
print(" HASIL POLLING")
print("============================================")

total_suara = sum(hasil_polling.values())

for opsi, jumlah in hasil_polling.items():
    if total_suara > 0:
        persentase = (jumlah / total_suara) * 100
    else:
        persentase = 0
    print(f"{opsi} : {jumlah} suara ({persentase:.2f}%)")

print("============================================")

# (Bonus) Simpan hasil polling ke file
with open("hasil_polling.txt", "w") as f:
    f.write("=== HASIL POLLING ===\n")
    for opsi, jumlah in hasil_polling.items():
        if total_suara > 0:
            persentase = (jumlah / total_suara) * 100
        else:
            persentase = 0
        f.write(f"{opsi} : {jumlah} suara ({persentase:.2f}%)\n")
