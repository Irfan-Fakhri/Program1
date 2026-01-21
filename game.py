import random  # Import library random untuk memilih pilihan komputer secara acak

# ============================================================================
# FUNGSI UNTUK MENAMPILKAN BANNER WELCOME
# ============================================================================
def tampilkan_welcome():
    """Menampilkan ucapan selamat datang yang menarik"""
    print("\n" + "=" * 60)
    print("          🎮 SELAMAT DATANG DI GAME BATU GUNTING KERTAS 🎮")
    print("=" * 60)
    print("Aturan Permainan:")
    print("  • Batu mengalahkan Gunting")
    print("  • Gunting mengalahkan Kertas")
    print("  • Kertas mengalahkan Batu")
    print("=" * 60 + "\n")


# ============================================================================
# FUNGSI UNTUK MENGAMBIL INPUT PEMAIN DENGAN VALIDASI
# ============================================================================
def ambil_input_pemain():
    """
    Meminta input dari pemain dan melakukan validasi.
    Input tidak peduli huruf besar atau kecil (case-insensitive).
    
    Return:
        str: Pilihan pemain ('batu', 'gunting', atau 'kertas')
        atau None jika input tidak valid
    """
    pilihan_valid = ['batu', 'gunting', 'kertas']
    
    while True:
        # Meminta input dari pemain
        input_pemain = input("Pilih (Batu/Gunting/Kertas): ").strip().lower()
        
        # Validasi input
        if input_pemain in pilihan_valid:
            return input_pemain
        else:
            # Jika input tidak valid, tampilkan pesan error
            print("❌ Input tidak valid! Silakan pilih: Batu, Gunting, atau Kertas\n")


# ============================================================================
# FUNGSI UNTUK MEMILIH KOMPUTER SECARA ACAK
# ============================================================================
def pilihan_komputer():
    """
    Komputer memilih secara acak dari tiga pilihan.
    
    Return:
        str: Pilihan komputer ('batu', 'gunting', atau 'kertas')
    """
    pilihan_list = ['batu', 'gunting', 'kertas']
    return random.choice(pilihan_list)


# ============================================================================
# FUNGSI UNTUK MENENTUKAN PEMENANG
# ============================================================================
def tentukan_pemenang(pemain, komputer):
    """
    Menentukan siapa pemenang dalam satu ronde permainan.
    
    Args:
        pemain (str): Pilihan pemain
        komputer (str): Pilihan komputer
    
    Return:
        str: 'menang', 'kalah', atau 'seri'
    """
    # Jika kedua pilihan sama, maka seri
    if pemain == komputer:
        return 'seri'
    
    # Cek kondisi kemenangan pemain
    if (pemain == 'batu' and komputer == 'gunting') or \
       (pemain == 'gunting' and komputer == 'kertas') or \
       (pemain == 'kertas' and komputer == 'batu'):
        return 'menang'
    
    # Jika bukan kondisi di atas, maka pemain kalah
    return 'kalah'


# ============================================================================
# FUNGSI UNTUK MENAMPILKAN HASIL RONDE
# ============================================================================
def tampilkan_hasil_ronde(pemain, komputer, hasil):
    """
    Menampilkan hasil permainan dalam satu ronde dengan format yang rapi.
    
    Args:
        pemain (str): Pilihan pemain
        komputer (str): Pilihan komputer
        hasil (str): Hasil permainan ('menang', 'kalah', atau 'seri')
    """
    print("\n" + "-" * 60)
    print(f"Anda memilih: {pemain.upper()}")
    print(f"Komputer memilih: {komputer.upper()}")
    
    # Tampilkan hasil dengan emoji sesuai kondisi
    if hasil == 'menang':
        print("🎉 ANDA MENANG! 🎉")
    elif hasil == 'kalah':
        print("💀 ANDA KALAH!")
    else:
        print("🤝 SERI!")
    print("-" * 60 + "\n")


# ============================================================================
# FUNGSI UNTUK MENAMPILKAN SKOR SAAT INI
# ============================================================================
def tampilkan_skor(skor_menang, skor_kalah, skor_seri):
    """
    Menampilkan skor permainan saat ini.
    
    Args:
        skor_menang (int): Jumlah kemenangan
        skor_kalah (int): Jumlah kekalahan
        skor_seri (int): Jumlah seri
    """
    print("=" * 60)
    print(f"SKOR: Menang: {skor_menang} | Kalah: {skor_kalah} | Seri: {skor_seri}")
    print("=" * 60 + "\n")


# ============================================================================
# FUNGSI UNTUK MENANYAKAN LANJUT ATAU BERHENTI
# ============================================================================
def tanya_lanjut():
    """
    Menanyakan kepada pemain apakah ingin melanjutkan permainan.
    
    Return:
        bool: True jika ingin lanjut, False jika ingin berhenti
    """
    while True:
        # Meminta input apakah ingin lanjut
        pilihan = input("Ingin bermain lagi? (Ya/Tidak): ").strip().lower()
        
        # Validasi input
        if pilihan in ['ya', 'y', 'iya']:
            return True
        elif pilihan in ['tidak', 'n', 'no']:
            return False
        else:
            # Jika input tidak valid
            print("❌ Input tidak valid! Silakan ketik: Ya atau Tidak\n")


# ============================================================================
# FUNGSI UNTUK MENAMPILKAN SKOR AKHIR PERMAINAN
# ============================================================================
def tampilkan_skor_akhir(skor_menang, skor_kalah, skor_seri):
    """
    Menampilkan skor akhir permainan dengan format yang menarik.
    
    Args:
        skor_menang (int): Total kemenangan
        skor_kalah (int): Total kekalahan
        skor_seri (int): Total seri
    """
    total_ronde = skor_menang + skor_kalah + skor_seri
    
    print("\n" + "=" * 60)
    print("               📊 SKOR AKHIR PERMAINAN 📊")
    print("=" * 60)
    print(f"Total Ronde: {total_ronde}")
    print(f"  ✅ Kemenangan: {skor_menang}")
    print(f"  ❌ Kekalahan: {skor_kalah}")
    print(f"  🤝 Seri: {skor_seri}")
    
    # Hitung presentase kemenangan
    if total_ronde > 0:
        presentase = (skor_menang / total_ronde) * 100
        print(f"  📈 Presentase Menang: {presentase:.1f}%")
    
    print("=" * 60)
    print("     Terima kasih telah bermain! Sampai jumpa lagi! 👋")
    print("=" * 60 + "\n")


# ============================================================================
# FUNGSI UTAMA UNTUK MENJALANKAN PERMAINAN
# ============================================================================
def main():
    """
    Fungsi utama yang menjalankan seluruh permainan.
    Mengontrol alur permainan dari awal hingga akhir.
    """
    # Tampilkan welcome banner
    tampilkan_welcome()
    
    # Inisialisasi variabel skor
    skor_menang = 0
    skor_kalah = 0
    skor_seri = 0
    
    # Loop permainan utama
    while True:
        # Ambil input dari pemain
        pilihan_pemain = ambil_input_pemain()
        
        # Komputer memilih secara acak
        pilihan_komp = pilihan_komputer()
        
        # Tentukan pemenang ronde ini
        hasil = tentukan_pemenang(pilihan_pemain, pilihan_komp)
        
        # Tampilkan hasil ronde
        tampilkan_hasil_ronde(pilihan_pemain, pilihan_komp, hasil)
        
        # Update skor berdasarkan hasil
        if hasil == 'menang':
            skor_menang += 1
        elif hasil == 'kalah':
            skor_kalah += 1
        else:
            skor_seri += 1
        
        # Tampilkan skor saat ini
        tampilkan_skor(skor_menang, skor_kalah, skor_seri)
        
        # Tanya apakah ingin lanjut
        if not tanya_lanjut():
            # Jika pemain memilih tidak, tampilkan skor akhir dan keluar
            tampilkan_skor_akhir(skor_menang, skor_kalah, skor_seri)
            break


# ============================================================================
# ENTRY POINT PROGRAM
# ============================================================================
# Jalankan program jika file ini dieksekusi langsung
if __name__ == "__main__":
    main()
