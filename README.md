# Studi_Kasus_4_Naufa-Fauza-Eky
nama: Naufa Fauza Eky
nim: 2609116060
kelas: b

Penjelasan Singkat Kode Studi Kasus 4 
1. Mengisi data produk
   produk = {
    "produk skincare 1" : {
    "nama" : "sunscreen wardah",
    "harga" : "37000",
    "stok" : "10"
    },
   dst
   }
   membuat key produk yang berisi nama, harga, stok dan menggunakan nested dictionary agar bisa memuat banyak produk
   
3. Mengisi menu
   membuat menu (yang berisikan tampilkan data, tambahkan data, ubah data, hapus data, keluar) dengan opsi agar pengguna bisa memilih tindakan yang ingin dilakukan serta menggunakan while True pada menu agar menu bisa ditampilkan secara berulang-ulang sampai pengguna memilih untuk keluar (pilihan no 5)
   
5. Menu 1
   secara keseluruhan kode ini berfungsi untuk menampilkan semua data
   - for key, data in produk.items():
            print("\n[{}]".format(key))
     digunakan untuk memanggil kategori produk (seperti: "produk skincare 1")
   - for field, isi in data.items():
                print("{} : {}".format(field.capitalize(), isi))
     digunakan untuk menampilkam isi dari kategori produknya
     
6. Menu 2
   kode ini digunakan untuk menambahkan informasi baru yang fieldnya beserta value yang belum ada didalam kategori, serta memeriksa apakah field tersebut sudah ada atau belum ada. Cara kerjanya adalah pengguna memasukkan key kategori (contoh: produk skincare 2) lalu pengguna diminta untuk memasukkan nama field baru beserta value nya
   
8. Menu 3
   mengedit atau mengubah nilai dari informasi atau data yang sudah ada dalam database. Cara kerjanya adalah pengguna diminta produk skincare yang mana ingin di edit, lalu pengguna mengisi value yang mau digantikan
   
10. Menu 4
   kode tersebut digunakan untuk pengguna agar bisa menghapus salah satu data atau field yang sudah ada didalam database

12. Menu 5
   Kode ini menggunakan break, sehingga jika pengguna memilih menu bagian 5 maka program akan berhenti
