# Dictionary harga buah
harga_buah = {
    "apel": 5000,
    "jeruk": 8500,
    "mangga": 7800,
    "pisang": 3000
}

total = 0

# Iterasi dengan .items()
for buah, harga in harga_buah.items():
    print(f"Harga 1 kg {buah} adalah Rp {harga}")
    total += harga

print("Total harga semua buah:", total)
