# Daftar awal buku
daftar_buku = [
    ["Novel", 75000, "Putih", 10],
    ["Pendidikan", 50000, "Putih", 15],
    ["Biografi", 35000, "Kuning", 20]
]

def tampilkan_daftar():
    print("\nDaftar Buku:")
    for i, buku in enumerate(daftar_buku, start=1):
        print(f"{i}. Jenis: {buku[0]}, Harga: {buku[1]}, Warna: {buku[2]}, Stok: {buku[3]}")

def tambah_buku():
    jenis = input("Jenis buku: ")
    harga = int(input("Harga: "))
    warna = input("Warna sampul: ")
    stok = int(input("Stok: "))
    daftar_buku.append([jenis, harga, warna, stok])
    print("Buku ditambahkan.")

def hapus_buku():
    tampilkan_daftar()
    index = int(input("Nomor buku yang akan dihapus: ")) - 1
    if 0 <= index < len(daftar_buku):
        daftar_buku.pop(index)
        print("Buku dihapus.")
    else:
        print("Nomor tidak valid.")

def cari_buku():
    kata_kunci = input("Cari berdasarkan jenis atau warna: ").lower()
    print("\nHasil pencarian:")
    for buku in daftar_buku:
        if kata_kunci in buku[0].lower() or kata_kunci in buku[2].lower():
            print(f"Jenis: {buku[0]}, Harga: {buku[1]}, Warna: {buku[2]}, Stok: {buku[3]}")

# Menu utama
while True:
    print("\n--- Menu ---")
    print("1. Tampilkan daftar buku")
    print("2. Tambah buku")
    print("3. Hapus buku")
    print("4. Cari buku")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tampilkan_daftar()
    elif pilihan == "2":
        tambah_buku()
    elif pilihan == "3":
        hapus_buku()
    elif pilihan == "4":
        cari_buku()
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
