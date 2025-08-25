# proyek_pembersih.py

def pembersih_data():
git add .
    try:
        # buka file input
        with open("transaksi_kotor.txt", "r", encoding="utf-8") as file_input:
            # buka file output
            with open("laporan_bersih.txt", "w", encoding="utf-8") as file_output:
                # tulis header
                file_output.write("LAPORAN TRANSAKSI BERSIH\n")
                file_output.write("=========================\n")

                grand_total = 0  # untuk bonus akumulasi total semua transaksi

                # loop setiap baris
                for baris in file_input:
                    baris = baris.strip()  # hapus spasi dan newline
                    if not baris:  # jika baris kosong -> skip
                        continue

                    # pecah data berdasarkan koma
                    data_potongan = baris.split(",")
                    if len(data_potongan) < 4:
                        continue  # jika format aneh, lewati saja

                    # bersihkan masing-masing bagian
                    id_bersih = data_potongan[0].strip().upper()
                    nama_bersih = data_potongan[1].strip().title()
                    jumlah = int(data_potongan[2].strip())
                    harga_satuan = float(data_potongan[3].strip())

                    # hitung total harga
                    total_harga = jumlah * harga_satuan
                    grand_total += total_harga

                    # format string output
                    string_output = (
                        f"ID: {id_bersih} | Produk: {nama_bersih} "
                        f"| Jumlah: {jumlah} | Total Harga: Rp {total_harga}\n"
                    )

                    # tulis ke file output
                    file_output.write(string_output)

                # footer
                file_output.write("--- ANALISIS SELESAI ---\n")
                file_output.write(f"Grand Total Seluruh Transaksi: Rp {grand_total}\n")

        print("Proses pembersihan data selesai. Laporan disimpan di laporan_bersih.txt")

    except FileNotFoundError:
        print("File transaksi_kotor.txt tidak ditemukan. Pastikan file tersedia.")


if __name__ == "__main__":
    pembersih_data()
