# Nested dictionary produk
produk = {
    "PROD001": {"nama": "Laptop", "harga": 7500000, "stok": 5},
    "PROD002": {"nama": "Mouse", "harga": 150000, "stok": 20}
}

# Cetak nama dan harga dari PROD002
print("Nama:", produk["PROD002"]["nama"])
print("Harga:", produk["PROD002"]["harga"])
