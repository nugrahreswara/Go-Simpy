import sys
from akun import akun

sudah_login = False
akun_sekarang = None

def login():
	from tampilan import bersihkan_layar
	global sudah_login, akun_sekarang
	maksimal_percobaan = 5
	percobaan = 0

	while percobaan < maksimal_percobaan:
		bersihkan_layar()
		print("=== LOGIN ===")
		username = input("Masukkan Username: ").strip()
		password = input("Masukkan Password: ").strip()
        
		if username in akun and akun[username]["password"] == password:
			sudah_login = True
			akun_sekarang = username
			bersihkan_layar()
			print("Login berhasil!")
			input("\nTekan Enter untuk melanjutkan...")
			return True
      
		else:
			percobaan += 1
			if percobaan < maksimal_percobaan:
				print(f"Username atau password salah. Percobaan ke-{percobaan} dari {maksimal_percobaan}")
				input("Tekan Enter untuk mencoba lagi...")
			else:
				print("Anda telah gagal login sebanyak 5 kali. Program akan dihentikan")
				sys.exit()
	return False
			
def logout():
	global sudah_login, akun_sekarang
	sudah_login = False
	akun_sekarang = None
	print(f"Troubleshoot: Sudah Login: {sudah_login}")
	print("Anda telah logout, silahkan login kembali")
	input("Tekan Enter untuk kembali...")	
	return

def apakah_sudah_login():
	global sudah_login
	return sudah_login

def apa_akun_sekarang():
	global akun_sekarang
	return akun_sekarang
