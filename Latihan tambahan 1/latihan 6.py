while True:
    try:
        umur = int(input("Masukkan umur Anda: "))
        if umur < 0 or umur > 100:
            print("Umur tidak wajar. Harap masukkan umur antara 0 dan 100.")
        else:
            print(f"Terima kasih. Umur Anda adalah {umur}.")
            break
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
