jumlah_prima = 0
angka = 2

while jumlah_prima < 5:
    prima = True
    for i in range(2, angka):
        if angka % i == 0:
            prima = False
            break
    if prima:
        print(angka)
        jumlah_prima += 1
    angka += 1