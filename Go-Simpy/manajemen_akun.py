from prettytable import PrettyTable
from akun import akun
from validasi_input import (email_valid, validasi_input_umur, email_terdaftar, nomor_terdaftar, username_terdaftar)

def hapus_akun():
	username = input("Masukkan username akun yang akan dihapus: ")

	if username in akun:
		print(f"Akun {username} berhasil dihapus!")
		input("Tekan Enter untuk melanjutkan...")
		del akun[username] 

	else:
		print("Username tidak ditemukan!")
		input("Tekan Enter untuk melanjutkan...")

	return
	
def edit_profil():
	username = input("Masukkan username: ").strip
	if len(username) < 3:
		print("Username terlalu pandek!, minimal 3 karakter")
		input("Tekan Enter untuk kembali...")
		return
	
	elif len(username) > 15:
		print("Username terlalu panjang!, maksimal 15 karakter")
		input("Tekan Enter untuk kembali...")
		return

	elif username_terdaftar(username):
		print("Username sudah ada")
		input("Tekan Enter untuk kembali...")
		return
	
	password = input("Masukkan password: ")
	
	nama_lengkap = input("Masukkan nama lengkap: ")
		
	umur = input("Masukkan umur: ")
	if not validasi_input_umur(umur):
		print("Umur tidak valid!")
		input("Tekan Enter untuk kembali...")
		return
		
	nomor_telepon = int(input("Masukkan nomor telepon: ")).strip()
	if not nomor_telepon.isdigit() and not len(nomor_telepon) >= 10:
		print("Nomor telepon tidak valid! Harus berisi angka dan minimal 10 digit.")
		input("Tekan Enter untuk kembali...")
		return

	elif nomor_terdaftar(nomor_telepon):
		print("Nomor telepon sudah terdaftar di akun lain")
		input("Tekan Enter untuk kembali...")
		return

	alamat_email = input("Masukkan alamat email: ").strip()
	bagian_user, bagian_domain = alamat_email.split("@")

	if not email_valid(alamat_email):
		print("Format E-Mail tidak valid!\nContoh format yang benar: user@example.com")
		input("Tekan Enter untuk kembali...")
		return

	elif email_terdaftar(alamat_email):
		print("Alamat email sudah terdaftar di akun lain")
		input("Tekan Enter untuk kembali...")
		return

	elif email.count('@' != 1):
		print("Format E-Mail tidak valid! Harus berisi satu tanda '@'.")
		return
	
	elif not bagian_user:
		print("Format E-Mail tidak valid! Nama pengguna sebelum '@' tidak boleh kosong.")
		return

	elif '.' in bagian_user:
		print("Format E-Mail tidak valid! Nama pengguna tidak boleh berisi titik (.).")
		return

	elif bagian_user.startswith('.') or bagian_user.endswith('.'):
		print("Format E-Mail tidak valid! Nama pengguna tidak boleh diawali atau diakhiri dengan titik.")
		return

	elif '..' in bagian_domain:
		print("Format E-Mail tidak valid! Nama pengguna tidak boleh mengandung titik berurutan (..).")
	
	elif not bagian_domain:
		print("Format E-Mail tidak valid! Nama domain setelah '@' tidak boleh kosong.")
		return

	elif '.' not in bagian_domain:
		print("Format E-Mail tidak valid! Domain harus berisi titik (.) seperti 'domain.com'.")
		return

	elif bagian_domain.startswith('.') or bagian_domain.endswith('.'):
		print("Format E-Mail tidak valid! Domain tidak boleh diawali atau diakhiri dengan titik.")
		return

	elif '..' in bagian_domain:
		print("Format E-Mail tidak valid! Domain tidak boleh mengandung titik berurutan (..).")
	
def tampilkan_daftar_akun():
	if not akun.items(): 
		print("Belum ada akun yang terdaftar.")
		input("Tekan Enter untuk kembali...")
		return

	table = PrettyTable()
	table.field_names = ["Username", "Nama Lengkap", "Umur", "Nomor Telepon", "Alamat Email", "Role"]

	for uname, data_akun in akun.items():
		table.add_row([
			uname,
			data_akun["nama_lengkap"],
			data_akun["umur"],
			data_akun["nomor_telepon"],
			data_akun["alamat_email"],
			data_akun["role"]
		])

	print("\n=== DAFTAR AKUN ===")
	print(table)
	input("Tekan Enter untuk melanjutkan...")
	return

def buat_akun_customer():
	print("=== Registrasi Customer ===")

	username = input("Masukkan username: ").strip()
	if not username:
		print("Username tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	elif len(username) < 3:
		print("Username terlalu pandek!, minimal 3 karakter")
		input("Tekan Enter untuk kembali...")
		return
	
	elif len(username) > 15:
		print("Username terlalu panjang!, maksimal 15 karakter")
		input("Tekan Enter untuk kembali...")
		return

	elif username_terdaftar(username):
		print("Username sudah ada")
		input("Tekan Enter untuk kembali...")
		return
	
	password = input("Masukkan password: ")
	if not password:
		print("Password tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	nama_lengkap = input("Masukkan nama lengkap: ")
	if not nama_lengkap:
		print("Nama lengkap tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return
	
	umur = input("Masukkan umur: ").strip()
	if not umur:
		print("Umur tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	elif not validasi_input_umur(umur):
		print("Umur tidak valid!")
		input("Tekan Enter untuk kembali...")
		return
		
	nomor_telepon = input("Masukkan nomor telepon: ").strip()
	if not nomor_telepon:
		print("Nomor telepon tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	elif not nomor_telepon.isdigit() and not len(nomor_telepon) >= 10:
		print("Nomor telepon tidak valid! Harus berisi angka dan minimal 10 digit.")
		input("Tekan Enter untuk kembali...")
		return

	elif nomor_terdaftar(nomor_telepon):
		print("Nomor telepon sudah terdaftar di akun lain")
		input("Tekan Enter untuk kembali...")
		return

	alamat_email = input("Masukkan alamat email: ").strip()

	if not email_valid(alamat_email):
		print("Format E-Mail tidak valid!\nContoh format yang benar: user@example.com")
		input("Tekan Enter untuk kembali...")
		return

	elif email_terdaftar(alamat_email):
		print("Alamat email sudah terdaftar di akun lain")
		input("Tekan Enter untuk kembali...")
		return

	elif alamat_email.count('@') != 1:
		print("Format E-Mail tidak valid! Harus berisi satu tanda '@'.")
		return

	bagian_user, bagian_domain = alamat_email.split('@')
	
	if not bagian_user:
		print("Format E-Mail tidak valid! Nama pengguna sebelum '@' tidak boleh kosong.")
		return

	elif '.' in bagian_user:
		print("Format E-Mail tidak valid! Nama pengguna tidak boleh berisi titik (.).")
		return

	elif bagian_user.startswith('.') or bagian_user.endswith('.'):
		print("Format E-Mail tidak valid! Nama pengguna tidak boleh diawali atau diakhiri dengan titik.")
		return

	elif '..' in bagian_domain:
		print("Format E-Mail tidak valid! Nama pengguna tidak boleh mengandung titik berurutan (..).")
	
	elif not bagian_domain:
		print("Format E-Mail tidak valid! Nama domain setelah '@' tidak boleh kosong.")
		return

	elif '.' not in bagian_domain:
		print("Format E-Mail tidak valid! Domain harus berisi titik (.) seperti 'domain.com'.")
		return

	elif bagian_domain.startswith('.') or bagian_domain.endswith('.'):
		print("Format E-Mail tidak valid! Domain tidak boleh diawali atau diakhiri dengan titik.")
		return

	elif '..' in bagian_domain:
		print("Format E-Mail tidak valid! Domain tidak boleh mengandung titik berurutan (..).")

	akun[username] = {
		"password" : password,
		"nama_lengkap" : nama_lengkap,
		"umur" : umur,
		"nomor_telepon" : nomor_telepon,
		"alamat_email" : alamat_email,
		"role" : "customer"
	}
	
	print(f"Akun customer berhasil dibuat!, Silahkan login")
	input("Tekan Enter untuk melanjutkan")
	return

def buat_akun_driver():
	print("=== Registrasi Driver ===")
	username = input("Masukkan username: ").strip()
	if not username:
		print("Username tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	elif username_terdaftar(username):
		print("Username sudah ada")
		input("Tekan Enter untuk kembali...")
		return

	elif len(username) < 3:
		print("Username terlalu pandek!, minimal 3 karakter")
		input("Tekan Enter untuk kembali...")
		return
	
	elif len(username) > 15:
		print("Username terlalu panjang!, maksimal 15 karakter")
		input("Tekan Enter untuk kembali...")
		return
	
	password = input("Masukkan password: ")
	if not password:
		print("Password tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	nama_lengkap = input("Masukkan nama lengkap: ")
	if not nama_lengkap:
		print("Nama lengkap tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return
	
	umur = input("Masukkan umur: ").strip()
	if not umur:
		print("Umur tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	elif not validasi_input_umur(umur):
		print("Umur tidak valid!")
		input("Tekan Enter untuk kembali...")
		return

	nomor_telepon = input("Masukkan nomor telepon: ").strip()
	if not nomor_telepon:
		print("Nomor telepon tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	elif not type(nomor_telepon):
		print("Nomor telepon hanya dapat diisi dengan angka")
		input("Tekan Enter untuk kembali...")
		return

	elif nomor_terdaftar(nomor_telepon):
		print("Nomor telepon sudah terdaftar di akun lain")
		input("Tekan Enter untuk kembali...")
		return

	alamat_email = input("Masukkan alamat email: ").strip()

	if not email_valid(alamat_email):
		print("Format E-Mail tidak valid!\nContoh format yang benar: user@example.com")
		input("Tekan Enter untuk kembali...")
		return

	elif email_terdaftar(alamat_email):
		print("Alamat email sudah terdaftar di akun lain")
		input("Tekan Enter untuk kembali...")
		return

	elif alamat_email.count('@') != 1:
		print("Format E-Mail tidak valid! Harus berisi satu tanda '@'.")
		return

	bagian_user, bagian_domain = alamat_email.split('@')
	
	if not bagian_user:
		print("Format E-Mail tidak valid! Nama pengguna sebelum '@' tidak boleh kosong.")
		return

	elif '.' in bagian_user:
		print("Format E-Mail tidak valid! Nama pengguna tidak boleh berisi titik (.).")
		return

	elif bagian_user.startswith('.') or bagian_user.endswith('.'):
		print("Format E-Mail tidak valid! Nama pengguna tidak boleh diawali atau diakhiri dengan titik.")
		return

	elif '..' in bagian_domain:
		print("Format E-Mail tidak valid! Nama pengguna tidak boleh mengandung titik berurutan (..).")
	
	elif not bagian_domain:
		print("Format E-Mail tidak valid! Nama domain setelah '@' tidak boleh kosong.")
		return

	elif '.' not in bagian_domain:
		print("Format E-Mail tidak valid! Domain harus berisi titik (.) seperti 'domain.com'.")
		return

	elif bagian_domain.startswith('.') or bagian_domain.endswith('.'):
		print("Format E-Mail tidak valid! Domain tidak boleh diawali atau diakhiri dengan titik.")
		return

	elif '..' in bagian_domain:
		print("Format E-Mail tidak valid! Domain tidak boleh mengandung titik berurutan (..).")

	akun[username] = {
		"password" : password,
		"nama_lengkap" : nama_lengkap,
		"umur" : umur,
		"nomor_telepon" : nomor_telepon,
		"alamat_email" : alamat_email,
		"role" : "driver",
		"saldo": "0"
	}
	
	print(f"Akun customer berhasil dibuat! Silahkan login")
	input("Tekan Enter untuk kembali...")
	return

def dapatkan_data_akun(username):
	return akun.get(username)

def cek_saldo(username):
	data = akun.get(username)
	if data:
		print("\n=== CEK SALDO ===")
		print(f"Saldo Anda saat ini: Rp {data['saldo']}")
		input("Tekan Enter untuk melanjutkan...")
	else:
		print("Akun tidak ditemukan!")
		input("Tekan Enter untuk melanjutkan...")


