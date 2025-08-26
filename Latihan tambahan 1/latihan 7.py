N = int(input("Masukkan sebuah angka N: "))
i = 1
jumlah = 0

while i <= N:
    jumlah += i ** 2
    i += 1

print(f"Jumlah kuadrat dari {N} bilangan pertama adalah: {jumlah}")
