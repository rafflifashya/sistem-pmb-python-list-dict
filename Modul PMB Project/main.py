class SistemPMB:
    def __init__(self):
        # List of dictionaries untuk menyimpan data
        self.pendaftar = []
        self.counter_id = 1

    def tambah_pendaftar(self, nama, jalur):
        pendaftar_baru = {
            "id": self.counter_id,
            "nama": nama,
            "jalur": jalur,
            "status": "Pending"
        }
        self.pendaftar.append(pendaftar_baru)
        self.counter_id += 1
        print(f"Pendaftar {nama} berhasil ditambahkan!")

    def lihat_semua(self):
        print("\n--- Daftar Seluruh Pendaftar ---")
        for p in self.pendaftar:
            print(f"ID: {p['id']} | Nama: {p['nama']} | Jalur: {p['jalur']} | Status: {p['status']}")

    def update_status(self, id_pendaftar, status_baru):
        for p in self.pendaftar:
            if p['id'] == id_pendaftar:
                p['status'] = status_baru
                print(f"Status ID {id_pendaftar} diperbarui menjadi {status_baru}")
                return
        print("ID tidak ditemukan.")

    def filter_lulus(self):
        print("\n--- Daftar Mahasiswa Lulus ---")
        lulus = [p for p in self.pendaftar if p['status'].lower() == "lulus"]
        if not lulus:
            print("Belum ada pendaftar yang lulus.")
        else:
            for p in lulus:
                print(f"Selamat! {p['nama']} ({p['jalur']})")

# --- Contoh Penggunaan ---
pmb = SistemPMB()
pmb.tambah_pendaftar("Andi", "Prestasi")
pmb.tambah_pendaftar("Budi", "Ujian Tulis")
pmb.lihat_semua()

pmb.update_status(1, "Lulus")
pmb.filter_lulus()