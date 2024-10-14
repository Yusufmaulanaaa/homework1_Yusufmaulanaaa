class RuangKelas:
    def __init__(self):
        self.jadwal = {}

    def cek_ketersediaan(self, ruang, waktu_mulai, waktu_selesai):
        for waktu, ruang_terpakai in self.jadwal.items():
            if ruang_terpakai == ruang:
                if (waktu_mulai < waktu and waktu_selesai > waktu) or \
                   (waktu < waktu_selesai and ruang_terpakai == ruang):
                    return False
        return True

    def tambah_jadwal(self, ruang, waktu_mulai, waktu_selesai):
        if self.cek_ketersediaan(ruang, waktu_mulai, waktu_selesai):
            self.jadwal[waktu_mulai] = ruang
            print(f"Jadwal berhasil ditambahkan: {ruang} dari {waktu_mulai} hingga {waktu_selesai}.")
        else:
            print("Ruang tidak tersedia pada waktu tersebut.")

    def tampilkan_jadwal(self):
        print("Jadwal Ruang Kelas:")
        for waktu, ruang in self.jadwal.items():
            print(f"Waktu: {waktu}, Ruang: {ruang}")


def main():
    manajemen_ruang = RuangKelas()
    
    while True:
        ruang = input("Masukkan nama ruang kelas (atau 'exit' untuk keluar): ")
        if ruang.lower() == 'exit':
            break
        waktu_mulai = input("Masukkan waktu mulai (format HH:MM): ")
        waktu_selesai = input("Masukkan waktu selesai (format HH:MM): ")
        
        manajemen_ruang.tambah_jadwal(ruang, waktu_mulai, waktu_selesai)
        manajemen_ruang.tampilkan_jadwal()


if __name__ == "__main__":
    main()
