password = "katasandi123"
karakter_terlarang = "$%&"

for char in password:
    if char in karakter_terlarang:
        print("Password mengandung karakter terlarang!")
        break
else:
    print("Password aman.")
