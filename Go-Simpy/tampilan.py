
import os

LINE = "────────────────────────────────────────────"
DOUBLE_LINE = "============================================"
BULLET = "›"

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')


def banner(text):
    print(DOUBLE_LINE)
    print(text.center(44))
    print(DOUBLE_LINE)


def tampilkan_menu_login():
    bersihkan_layar()
    banner("MENU LOGIN")

    print(f"{BULLET} 1. Login")
    print(f"{BULLET} 2. Registrasi Customer")
    print(f"{BULLET} 3. Registrasi Driver")
    print(f"{BULLET} 4. Keluar")
    print(LINE)

def tampilkan_menu_utama(role):
    bersihkan_layar()
    banner(f"Selamat Datang")

    if role == "admin":
        print(" MENU ADMIN")
        print(LINE)
        print(f"{BULLET} 1. Edit Profil")
        print(f"{BULLET} 2. Tambah Akun Customer")
        print(f"{BULLET} 3. Tambah Akun Driver")
        print(f"{BULLET} 4. Hapus User")
        print(f"{BULLET} 5. Lihat Semua Akun")
        print(f"{BULLET} 6. Lihat Semua Pendapatan")
        print(f"{BULLET} 7. Logout")
        print(f"{BULLET} 8. Keluar")
        print(LINE)

    elif role == "customer":
        print(" 	MENU CUSTOMER")
        print(LINE)
        print(f"{BULLET} 1. Edit Profil")
        print(f"{BULLET} 2. Cek Saldo")
        print(f"{BULLET} 3. Pesan Ojek")
        print(f"{BULLET} 4. Logout")
        print(f"{BULLET} 5. Keluar")
        print(LINE)

    elif role == "driver":
        print("   MENU DRIVER")
        print(LINE)
        print(f"{BULLET} 1. Edit Profil")
        print(f"{BULLET} 2. Cek Saldo")
        print(f"{BULLET} 3. Tarik Pendapatan")
        print(f"{BULLET} 4. Lihat Pendapatan")
        print(f"{BULLET} 5. Logout")
        print(f"{BULLET} 6. Keluar")
        print(LINE)
