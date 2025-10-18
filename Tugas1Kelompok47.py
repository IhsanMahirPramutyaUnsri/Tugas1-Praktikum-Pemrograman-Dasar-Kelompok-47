import os
from datetime import datetime

daftar_buku = []
id_counter = 1

def validasi_input(prompt, tipe_data='str'):
    while True:
        try:
            nilai = input(prompt)
            if tipe_data == 'int':
                return int(nilai)
            elif tipe_data == 'str':
                if nilai.strip() == '':
                    print("Input tidak boleh kosong!")
                    continue
                return nilai.strip()
        except ValueError:
            print(f"Input harus berupa {tipe_data}!")

def generate_id():
    global id_counter
    current_id = id_counter
    id_counter += 1
    return current_id

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_header():
    print("\n" + "="*50)
    print("   SISTEM PERPUSTAKAAN DIGITAL - Kelompok 47")
    print("="*50)

class Buku:
    def __init__(self, id_buku, judul, pengarang, tahun, stok):
        self.id_buku = id_buku
        self.judul = judul
        self.pengarang = pengarang
        self.tahun = tahun
        self.stok = stok
    
    def tampilkan_info(self):
        print(f"\nID Buku      : {self.id_buku}")
        print(f"Judul        : {self.judul}")
        print(f"Pengarang    : {self.pengarang}")
        print(f"Tahun Terbit : {self.tahun}")
        print(f"Stok         : {self.stok}")
        print("-" * 40)
    
    def cek_ketersediaan(self):
        return self.stok > 0
    
    def get_info_singkat(self):
        status = "Tersedia" if self.cek_ketersediaan() else "Habis"
        return f"[ID: {self.id_buku}] {self.judul} - {self.pengarang} ({status})"

def tambah_buku():
    clear_screen()
    tampilkan_header()
    print("\n>>> TAMBAH BUKU BARU <<<")
    
    id_buku = generate_id()
    judul = validasi_input("Masukkan judul buku: ", 'str')
    pengarang = validasi_input("Masukkan nama pengarang: ", 'str')
    tahun = validasi_input("Masukkan tahun terbit: ", 'int')
    stok = validasi_input("Masukkan jumlah stok: ", 'int')
    
    if tahun < 1000 or tahun > datetime.now().year:
        print("\n✗ Tahun tidak valid!")
        return
    
    if stok < 0:
        print("\n✗ Stok tidak boleh negatif!")
        return
    
    buku_baru = Buku(id_buku, judul, pengarang, tahun, stok)
    daftar_buku.append(buku_baru)
    
    print("\n" + "="*40)
    print("✓ BUKU BERHASIL DITAMBAHKAN!")
    print("="*40)
    buku_baru.tampilkan_info()

def tampilkan_semua_buku():
    clear_screen()
    tampilkan_header()
    print("\n>>> DAFTAR SEMUA BUKU <<<\n")
    
    if len(daftar_buku) == 0:
        print("Belum ada buku dalam perpustakaan.")
        return
    
    print("="*50)
    for i, buku in enumerate(daftar_buku, 1):
        print(f"{i}. {buku.get_info_singkat()}")
    
    print("="*50)
    print(f"Total buku: {len(daftar_buku)}")
    
    lihat_detail = validasi_input("\nLihat detail buku? (y/n): ", 'str').lower()
    
    if lihat_detail == 'y':
        print("\n>>> DETAIL SEMUA BUKU <<<")
        for buku in daftar_buku:
            buku.tampilkan_info()

def hapus_buku():
    clear_screen()
    tampilkan_header()
    print("\n>>> HAPUS BUKU <<<")

    if len(daftar_buku) == 0:
        print("Belum ada buku dalam perpustakaan.")
        return
    
    print("\nDaftar Buku:")
    print("-"*50)
    for i, buku in enumerate(daftar_buku, 1):
        print(f"{i}. {buku.get_info_singkat()}")
    print("-"*50)
    
    id_hapus = validasi_input("\nMasukkan ID buku yang akan dihapus: ", 'int')
    
    buku_ditemukan = None
    index_hapus = -1
    
    for i, buku in enumerate(daftar_buku):
        if buku.id_buku == id_hapus:
            buku_ditemukan = buku
            index_hapus = i
            break
    
    if buku_ditemukan is None:
        print("\n✗ Buku dengan ID tersebut tidak ditemukan!")
        return
    
    print("\nData buku yang akan dihapus:")
    buku_ditemukan.tampilkan_info()
    
    konfirmasi = validasi_input("Apakah Anda yakin ingin menghapus? (y/n): ", 'str').lower()
    
    if konfirmasi == 'y':
        daftar_buku.pop(index_hapus)
        print("\n" + "="*40)
        print("✓ BUKU BERHASIL DIHAPUS!")
        print("="*40)
    else:
        print("\n✗ Penghapusan dibatalkan.")

def menu_utama():
    """Function untuk menampilkan menu utama"""
    while True:
        clear_screen()
        tampilkan_header()
        print("\n>>> MENU UTAMA <<<")
        print("="*50)
        print("1. Tambah Buku Baru")
        print("2. Tampilkan Semua Buku")
        print("3. Hapus Buku")
        print("0. Keluar")
        print("="*50)
        
        pilihan = validasi_input("\nPilih menu: ", 'int')
        
        if pilihan == 1:
            tambah_buku()
        elif pilihan == 2:
            tampilkan_semua_buku()
        elif pilihan == 3:
            hapus_buku()
        elif pilihan == 0:
            clear_screen()
            print("\n" + "="*50)
            print("   TERIMA KASIH TELAH MENGGUNAKAN PROGRAM!")
            print("   Program dibuat oleh Kelompok 47")
            print("="*50 + "\n")
            break
        else:
            print("\n✗ Pilihan tidak valid!")
        
        input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("   SELAMAT DATANG DI PERPUSTAKAAN DIGITAL")
    print("   Dari Kelompok 47")
    print("="*50)
    input("\nTekan Enter untuk memulai...")
    
    menu_utama()