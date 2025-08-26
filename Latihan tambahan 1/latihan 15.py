password_benar = "rahasia123"
maks_percobaan = 3

for percobaan in range(maks_percobaan):
    password = input("Masukkan password: ")
    if password == password_benar:
        print("Login berhasil!")
        break
    else:
        sisa = maks_percobaan - (percobaan + 1)
        if sisa > 0:
            print(f"Password salah. Sisa percobaan: {sisa}")
else:
    print("Akun Anda terkunci!")