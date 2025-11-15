from prettytable import PrettyTable
from akun import akun
from validasi_input import validasi_input_email
from validasi_input import validasi_input_umur

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
	return

def tampilkan_daftar_akun():
	if not akun.items(): 
		print("Belum ada akun yang terdaftar.")
		input("Tekan Enter untuk kembali...")

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

	username = input("Masukkan username: ")
	if not username:
		print("Username tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	if len(username) < 3:
		print("Username terlalu pandek!, minimal 3 karakter")
		input("Tekan Enter untuk kembali...")
		return
	
	if len(username) > 15:
		print("Username terlalu panjang!, maksimal 15 karakter")
		input("Tekan Enter untuk kembali...")
		return

	if akun_ada(username):
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
	
	umur = input("Masukkan umur: ")
	if not umur:
		print("Umur tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	if not validasi_input_umur(umur):
		print("Umur tidak valid!")
		input("Tekan Enter untuk kembali...")
		return
		
	nomor_telepon = input("Masukkan nomor telepon: ")
	if not nomor_telepon:
		print("Nomor telepon tidak boleh kosong")
		return

	alamat_email = input("Masukkan alamat email: ")
	if not alamat_email:
		print("Alamat email tidak boleh kosong")
		return

	if not validasi_input_email(alamat_email):
		print("Format E-Mail tidak valid!\nContoh format yang benar: user@example.com")
		return

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
	username = input("Masukkan username: ")
	if not username:
		print("Username tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	if akun_ada(username):
		print("Username sudah ada")
		input("Tekan Enter untuk kembali...")
		return

	if len(username) < 3:
		print("Username terlalu pandek!, minimal 3 karakter")
		input("Tekan Enter untuk kembali...")
		return
	
	if len(username) > 15:
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
	
	umur = input("Masukkan umur: ")
	if not umur:
		print("Umur tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	if not validasi_input_umur(umur):
		print("Umur tidak valid!")
		input("Tekan Enter untuk kembali...")
		return

		
	nomor_telepon = input("Masukkan nomor telepon: ")
	if not nomor_telepon:
		print("Nomor telepon tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	alamat_email = input("Masukkan alamat email: ")
	if not alamat_email:
		print("Alamat email tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	if not validasi_input_email(alamat_email):
		print("Format E-Mail tidak valid!\nContoh format yang benar: user@example.com")
		input("Tekan Enter untuk kembali...")
		return

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

def akun_ada(username):
	return username in akun

def cek_saldo(username):
	data = akun.get(username)
	if data:
		print("\n=== CEK SALDO ===")
		print(f"Saldo Anda saat ini: Rp {data['saldo']}")
		input("Tekan Enter untuk melanjutkan...")
	else:
		print("Akun tidak ditemukan!")
		input("Tekan Enter untuk melanjutkan...")


