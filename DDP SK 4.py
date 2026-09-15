produk = {
    "produk skincare 1" : {
    "nama" : "sunscreen wardah",
    "harga" : "37000",
    "stok" : "10"
    },
    "produk skincare 2" : {
    "nama" : "toner hadalabo",
    "harga" : "40000",
    "stok" : "5"
    },
    "produk skincare 3" : {
    "nama" : "face wash emina",
    "harga" : "25000",
    "stok" : "4"
    },
    "produk skincare 4" : {
    "nama" : "micellar water g2g",
    "harga" : "30000",
    "stok" : "7"
    }
}

print("===== TOKO VELOUVERA SKIN =====")
print("Pilih keluar untuk mengakhiri pengecekan")

while True:
    print("\nMenu:")
    print("1. Tampilkan data")
    print("2. Tambahkan data kategori")
    print("3. Ubah data")
    print("4. Hapus data")
    print("5. keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        for key, data in produk.items():
            print("\n[{}]".format(key))
            for field, isi in data.items():
                print("{} : {}".format(field.capitalize(), isi))

    elif pilihan == "2":
        key_produk = input("masukkan key kategori yang sudah ada: ")
        if key_produk in produk:
            field_baru = input("Masukkan field baru: ")

            if field_baru in produk[key_produk]:
                print(f"Data ini sudah ada")
            else: 
                isi_baru = input("Isi value {} data tersebut: ".format(field_baru))
                produk[key_produk][field_baru] = isi_baru
                print("Data berhasil ditambahkan")
        else: 
            print("key produk tidak ditemukan!")

    elif pilihan =="3":
        key_produk = input("Masukkan key produk: ")
        if key_produk in produk:
            field_ubah = input("Masukkan data yang mau diubah: ")
            if field_ubah in produk[key_produk]:
                isi_baru = input("Nilai baru untuk {} (sekarang: {}): ".format(field_ubah, produk[key_produk][field_ubah]))
                produk[key_produk][field_ubah] = isi_baru
                print("Data berhasil diubah")
            else: 
                print("Produk ini tidak punya data")
        else:
            print("Key produk tidak ditemukan")

    elif pilihan =="4":
        key_produk = input("masukkan key produk yang datanya ingin dihapus: ")
        if key_produk in produk:
            field_hapus = input("masukkan nama data yang ingin dihapus: ")
            if field_hapus in produk[key_produk]:
                del produk[key_produk][field_hapus]
                print("Data '{}' berhasil dihapus!".format(field_hapus))
            else:
                print("Produk ini tidak punya data '{}'!".format(field_hapus))
        else:
            print("key produk tidak ditemukan")

    elif pilihan == "5":
        print("Terimakasih!")
        break