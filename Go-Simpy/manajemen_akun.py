from prettytable import PrettyTable
from akun import akun

data_akun = []
    
def hapus_akun(username):
    for akun in data_akun:
        if akun["username"] == username:
            data_akun.remove(akun)
            print(f"Akun '{username}' berhasil dihapus.")
            return
    print(f"Akun dengan username {username} tidak ditemukan.")

def edit_profil(username, password, nama_lengkap=None, umur=None, no_telepon=None, alamat_email=None):
    for akun in data_akun:
        if akun["username"] == username and akun["password"] == password:
            if nama_lengkap:
                akun["nama_lengkap"] = nama_lengkap
            if umur:
                akun["umur"] = umur
            if no_telepon:
                akun["nomor_telepon"] = no_telepon
            if alamat_email:
                akun["alamat_email"] = alamat_email

            print(f"Profil akun {username} berhasil diperbarui.")
            return
    print("Username atau password salah. Profil tidak dapat diperbarui.")

def buat_akun():
    print("=== Buat Akun Baru ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    nama_lengkap = input("Masukkan nama lengkap: ")
    umur = input("Masukkan umur: ")
    nomor_telepon = input("Masukkan nomor telepon: ")
    alamat_email = input("Masukkan alamat email: ")

    for a in data_akun:
        if a["username"] == username:
            print("Username sudah digunakan. Gunakan username lain.")
            return

    akun_baru = {
        "username": username,
        "password": password,
        "nama_lengkap": nama_lengkap,
        "umur": umur,
        "nomor_telepon": nomor_telepon,
        "alamat_email": alamat_email
    }

    data_akun.append(akun_baru)
    print(f"Akun '{username}' berhasil dibuat!")

def lihat_daftar_akun():
    print("=== Daftar Akun ===")
    
    if not data_akun: 
        print("Belum ada akun yang terdaftar.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["Username", "Nama Lengkap", "Umur", "Nomor Telepon", "Alamat Email"]

    for akun in data_akun:
        tabel.add_row([
            akun["username"],
            akun["nama_lengkap"],
            akun["umur"],
            akun["nomor_telepon"],
            akun["alamat_email"]
        ])

    print(tabel)

def registrasi_customer():
    print("=== Registrasi Customer ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    nama_lengkap = input("Masukkan nama lengkap: ")
    umur = input("Masukkan umur: ")
    nomor_telepon = input("Masukkan nomor telepon: ")
    alamat_email = input("Masukkan alamat email: ")

    for a in data_akun:
        if a["username"] == username:
            print("Username sudah digunakan. Gunakan username lain.")
            return

    akun_customer = {
        "username": username,
        "password": password,
        "nama_lengkap": nama_lengkap,
        "umur": umur,
        "nomor_telepon": nomor_telepon,
        "alamat_email": alamat_email
    }

    data_akun.append(akun_customer)
    print(f"Akun customer {username} berhasil dibuat!")


def registrasi_driver():
    print("=== Registrasi Driver ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    nama_lengkap = input("Masukkan nama lengkap: ")
    umur = input("Masukkan umur: ")
    nomor_telepon = input("Masukkan nomor telepon: ")
    alamat_email = input("Masukkan alamat email: ")

    for a in data_akun:
        if a["username"] == username:
            print("Username sudah digunakan. Gunakan username lain.")
            return

    akun_driver = {
        "username": username,
        "password": password,
        "nama_lengkap": nama_lengkap,
        "umur": umur,
        "nomor_telepon": nomor_telepon,
        "alamat_email": alamat_email
    }

    data_akun.append(akun_driver)
    print(f"Akun driver {username} berhasil dibuat!")