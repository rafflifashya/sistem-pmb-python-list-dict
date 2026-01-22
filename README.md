# Modul PMB (Penerimaan Mahasiswa Baru) - Python

Sistem sederhana untuk mengelola pendaftaran mahasiswa baru menggunakan Python. Proyek ini mendemonstrasikan penggunaan struktur data `list` dan `dictionary` untuk manajemen data tanpa database eksternal.

## 🌟 Fitur
- **Input Data Pendaftar**: Nama lengkap dan Jalur Seleksi.
- **Manajemen Status**: Default status adalah "Proses", yang kemudian dapat diubah oleh admin menjadi "Lulus" atau "Tidak Lulus".
- **Monitoring**: Menampilkan seluruh data pendaftar dalam bentuk list yang rapi.

## 🛠️ Teknologi
- **Python 3.x**
- **Mermaid.js** (untuk dokumentasi Class Diagram)

## 📊 Class Diagram
Berikut adalah struktur kelas dari modul ini:

```mermaid
classDiagram
    class CalonMahasiswa {
        +String nama
        +String jalur
        +String status
    }
    class ModulPMB {
        +List data_pendaftar
        +tambah_pendaftar()
        +lihat_semua()
        +update_status()
    }
    ModulPMB "1" -- "*" CalonMahasiswa : mengelola
