# 🚀 Go-Simpy – Sistem Pemesanan Ojek Online Sederhana

> Simulasi sistem manajemen akun transportasi berbasis Python dengan autentikasi, validasi input, dan antarmuka terminal interaktif.

---

## 🔍 Ringkasan
Go-Simpy adalah program pemesanan ojek online yang mengimplementasikan **multi user dengan 3 peran: admin, customer & driver**. Sistem ini menampilkan menu berbeda sesuai peran akun, menjamin keamanan autentikasi, dan menjaga integritas data melalui validasi input.

---

## ✨ Fitur Utama

- **🔐 Autentikasi**: Login dengan proteksi percobaan gagal (max 5x), registrasi, dan logout.
- **👥 Manajemen Akun (CRUD)**:
  - Buat/Registrasi, edit, hapus, dan tampilkan akun.
  - Validasi inputan: umur (13–100), email (format dasar), dan nomor telepon.
- **👥 Menerapkan Multiuser**:
  - Bisa membuat akun melalui akun admin atau registrasi di menu login
  - Bisa logout dan login sebagai akun lain
- **🛡️ Akses fitur berdasarkan role**:
  - **Admin**: Kelola akun & lihat semua transaksi.
  - **Customer**: Pesan ojek & lihat histori pemesanan.
  - **Driver**: Lihat histori pendapatan.
- **🎨 Visualisasi Data**:
  - Tampilan cantik dan bersih dengan menggunakan `PrettyTable`.
- **📁 Modular**: Kode terstruktur dalam beberapa modul untuk kemudahan debugging.

---

## 📦 Akun & Password bawaan:
- **Akun dengan role Admin**
  - Username: admin
  - Password: admin

- **Akun dengan role Customer**
  - Username: customer-01
  - Password: customer-01

- **Akun dengan role driver**
  - Username: driver-01
  - Password: driver-01
  
---
