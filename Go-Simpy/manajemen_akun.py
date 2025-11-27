from prettytable import PrettyTable
from akun import akun
from validasi_input import (email_valid, validasi_input_umur, email_terdaftar, nomor_terdaftar, username_terdaftar)
from autentikasi import apa_akun_sekarang

def hapus_akun():
	tampilkan_daftar_akun()
	print()
	username = input("Masukkan username akun yang akan dihapus: ")

	if username in akun:
		if akun[username]["role"] == "admin":
			print("Tidak dapat menghapus akun dengan role admin!")
			input("Tekan Enter untuk kembali...")
			return

		else:
			print(f"\nAnda akan menghapus akun: {username}")
			print(f"Nama lengkap: {akun[username]['nama_lengkap']}")
			print(f"Role: {akun[username]['role']}")
			print(f"Nomor Telepon: {akun[username]['nomor_telepon']}")
			print(f"Alamat E-Mail: {akun[username]['alamat_email']}\n")

			konfirmasi = input("Apakah anda yakin ingin menghapus akun: {username}? (y/t): ").strip().lower()

			if konfirmasi == "y":
				print(f"\nAkun {username} berhasil dihapus!")
				input("Tekan Enter untuk melanjutkan...")
				del akun[username]

			else:
				print("Penghapusan akun dibatalkan")
				input("Tekan Enter untuk kembali...")
				return

	else:
		print("Username tidak ditemukan!")
		input("Tekan Enter untuk melanjutkan...")

	return
	
def edit_profil():
	print("===Edit Profil===")
	print("===Kosongkan jika tidak ingin mengubah!===")
	from akun import akun
	data_akun = akun[apa_akun_sekarang()]

	# Username
	username = input(f"Masukkan username baru ({apa_akun_sekarang()}): ").strip() or None
	if username is not None:
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
		
		elif not username[0].isalpha():
			print("Username harus diawali dengan huruf!")
			input("Tekan Enter untuk kembali...")
			return
			
		elif not username.replace('_','').replace('-','').isalnum():
			print("Username hanya boleh berisi huruf, angka, underscore(_), atau tanda hubung (-)!")
			input("Tekan Enter untuk kembali...")
			return

		else:
			data_akun["username"] = username
	
	# Password
	password = input("Masukkan password baru: ") or None
	if password is not None:
		data_akun["password"] = password	

	# Nama Lengkap
	nama_lengkap = input(f"Masukkan nama lengkap baru ({data_akun['nama_lengkap']}): ") or None
	if nama_lengkap is not None:	
		if not nama_lengkap.isalpha():
			print("Nama lengkap hanya boleh diisi dengan huruf!")
			input("Tekan Enter untuk kembali...")
			return

		else:
			data_akun["nama_lengkap"] = nama_lengkap

	# Umur
	umur = input(f"Masukkan umur ({data_akun['umur']}): ") or None
	if umur is not None:
		if not validasi_input_umur(umur):
			print("Umur tidak valid!")
			input("Tekan Enter untuk kembali...")
			return

		else:
			data_akun["umur"] = umur
		
	# Nomor Telepon
	nomor_telepon = input(f"Masukkan nomor telepon baru ({data_akun['nomor_telepon']}): ").strip() or None
	if nomor_telepon is not None:
		if not nomor_telepon.isdigit() and not len(nomor_telepon) >= 10:
			print("Nomor telepon tidak valid! Harus berisi angka dan minimal 10 digit.")
			input("Tekan Enter untuk kembali...")
			return

		elif nomor_terdaftar(nomor_telepon):
			print("Nomor telepon sudah terdaftar di akun lain")
			input("Tekan Enter untuk kembali...")
			return
			
		else:
			data_akun["nomor_telepon"] = nomor_telepon

	# Alamat E-Mail
	alamat_email = input(f"Masukkan alamat email baru ({data_akun['alamat_email']}): ").strip() or None
	if alamat_email is not None:
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
			input("Tekan Enter untuk kembali...")
			return

		bagian_user, bagian_domain = alamat_email.split("@")
		
		if not bagian_user:
			print("Format E-Mail tidak valid! Nama pengguna sebelum '@' tidak boleh kosong.")
			input("Tekan Enter untuk kembali...")
			return

		elif '.' in bagian_user:
			print("Format E-Mail tidak valid! Nama pengguna tidak boleh berisi titik (.).")
			input("Tekan Enter untuk kembali...")
			return

		elif bagian_user.startswith('.') or bagian_user.endswith('.'):
			print("Format E-Mail tidak valid! Nama pengguna tidak boleh diawali atau diakhiri dengan titik.")
			input("Tekan Enter untuk kembali...")
			return

		elif '..' in bagian_domain:
			print("Format E-Mail tidak valid! Nama pengguna tidak boleh mengandung titik berurutan (..).")
			input("Tekan Enter untuk kembali...")
			return
		
		elif not bagian_domain:
			print("Format E-Mail tidak valid! Nama domain setelah '@' tidak boleh kosong.")
			return

		elif '.' not in bagian_domain:
			print("Format E-Mail tidak valid! Domain harus berisi titik (.) seperti 'domain.com'.")
			input("Tekan Enter untuk kembali...")
			return

		elif bagian_domain.startswith('.') or bagian_domain.endswith('.'):
			print("Format E-Mail tidak valid! Domain tidak boleh diawali atau diakhiri dengan titik.")
			input("Tekan Enter untuk kembali...")
			return

		elif '..' in bagian_domain:
			print("Format E-Mail tidak valid! Domain tidak boleh mengandung titik berurutan (..).")
			input("Tekan Enter untuk kembali...")
			return

		else:
			data_akun["alamat_email"] = alamat_email

	print("Profil akun berhasil diubah!")
	input("Tekan Enter untuk kembali...")
	
def tampilkan_daftar_akun():
	global akun
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

def buat_akun(pilihan):
	print("=== Proses pembuatan akun ===")

	# Username
	username = input("Masukkan username: ").strip()

	if not username:
		print("Username tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

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
		
	elif not username[0].isalpha():
		print("Username harus diawali dengan huruf!")
		input("Tekan Enter untuk kembali...")
		return
			
	elif not username.replace('_','').replace('-','').isalnum():
		print("Username hanya boleh berisi huruf, angka, underscore(_), atau tanda hubung (-)!")
		input("Tekan Enter untuk kembali...")
		return

	# Password
	password = input("Masukkan password: ")
	if not password:
		print("Password tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	# Nama Lengkap
	nama_lengkap = input("Masukkan nama lengkap: ")
	if not nama_lengkap:
		print("Nama lengkap tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	if not all(kata.isalpha() for kata in nama_lengkap.split()):
		print("Nama hanya boleh berisi huruf dan spasi. Input tidak valid.")
		input("Tekan Enter untuk kembali...")
		return

	nama_lengkap = nama_lengkap.title()
	
	# Umur
	umur = input("Masukkan umur: ").strip()
	if not umur:
		print("Umur tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	elif not validasi_input_umur(umur):
		print("Umur tidak valid!")
		input("Tekan Enter untuk kembali...")
		return
		
	# Nomor Telepon
	nomor_telepon = input("Masukkan nomor telepon: ").strip()
	if not nomor_telepon:
		print("Nomor telepon tidak boleh kosong")
		input("Tekan Enter untuk kembali...")
		return

	elif nomor_terdaftar(nomor_telepon):
		print("Nomor telepon sudah terdaftar di akun lain")
		input("Tekan Enter untuk kembali...")
		return

	elif not nomor_telepon.isdigit() or not len(nomor_telepon) >= 10:
		print("Nomor telepon tidak valid! Harus berisi angka dan minimal 10 digit.")
		input("Tekan Enter untuk kembali...")
		return

	# Alamat E-Mail
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
		input("Tekan Enter untuk kembali...")
		return

	bagian_user, bagian_domain = alamat_email.split('@')
	
	if not bagian_user:
		print("Format E-Mail tidak valid! Nama pengguna sebelum '@' tidak boleh kosong.")
		input("Tekan Enter untuk kembali...")
		return

	elif '.' in bagian_user:
		print("Format E-Mail tidak valid! Nama pengguna tidak boleh berisi titik (.).")
		input("Tekan Enter untuk kembali...")
		return

	elif bagian_user.startswith('.') or bagian_user.endswith('.'):
		print("Format E-Mail tidak valid! Nama pengguna tidak boleh diawali atau diakhiri dengan titik.")
		input("Tekan Enter untuk kembali...")
		return

	elif '..' in bagian_user:
		print("Format E-Mail tidak valid! Nama pengguna tidak boleh mengandung titik berurutan (..).")
		input("Tekan Enter untuk kembali...")
		return
	
	elif not bagian_domain:
		print("Format E-Mail tidak valid! Nama domain setelah '@' tidak boleh kosong.")
		input("Tekan Enter untuk kembali...")
		return

	elif '.' not in bagian_domain:
		print("Format E-Mail tidak valid! Domain harus berisi titik (.) seperti 'domain.com'.")
		input("Tekan Enter untuk kembali...")
		return

	elif bagian_domain.startswith('.') or bagian_domain.endswith('.'):
		print("Format E-Mail tidak valid! Domain tidak boleh diawali atau diakhiri dengan titik.")
		input("Tekan Enter untuk kembali...")
		return

	elif '..' in bagian_domain:
		print("Format E-Mail tidak valid! Domain tidak boleh mengandung titik berurutan (..).")
		input("Tekan Enter untuk kembali...")
		return


	if pilihan == "2":	
		akun[username] = {
			"password" : password,
			"nama_lengkap" : nama_lengkap,
			"umur" : umur,
			"nomor_telepon" : nomor_telepon,
			"alamat_email" : alamat_email,
			"role" : "customer"
		}

		print(f"Akun customer berhasil dibuat!, Silahkan login")

		
	if pilihan == "3":	
		akun[username] = {
			"password" : password,
			"nama_lengkap" : nama_lengkap,
			"umur" : umur,
			"nomor_telepon" : nomor_telepon,
			"alamat_email" : alamat_email,
			"role" : "driver"
		}	
		
		print(f"Akun driver berhasil dibuat!, Silahkan login")

	
	input("Tekan Enter untuk melanjutkan")
	return

def dapatkan_data_akun(username):
	return akun.get(username)
