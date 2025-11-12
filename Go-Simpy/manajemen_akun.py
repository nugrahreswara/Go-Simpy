from prettytable import PrettyTable
from akun import akun

data_akun = []

def tambah_akun_customer():
	return

def tambah_akun_driver():
	return

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

def tampilkan_daftar_akun():
	table = PrettyTable()
	table.field_names = ["Username", "Nama Lengkap", "Umur", "No. Telp", "Email", "Role"]
	for username, data in akun.items():
		table.add_row([
			username,
			data["nama_lengkap"],
			data["umur"],
			data["nomor_telepon"],
			data["alamat_email"],
			data["role"]
		])
	print("===DAFTAR AKUN GO-SIMPY===")
	print(table)
	input("Tekan Enter untuk kembali...")

def dapatkan_data_akun(username):
	return akun.get(username)
