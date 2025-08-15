# Membaca file dan menghitung frekuensi hari
fname = "mbox-short.txt"
hari_count = {}

with open(fname) as f:
    for line in f:
        if line.startswith("From "):
            kata = line.split()
            hari = kata[2]  # Hari ada di posisi index 2
            hari_count[hari] = hari_count.get(hari, 0) + 1

print(hari_count)
