import sys

from autentikasi import (login, logout, apakah_sudah_login, apa_akun_sekarang)
from manajemen_akun import (edit_profil, tambah_akun_customer, tambah_akun_driver, hapus_akun, dapatkan_data_akun)
from tampilan import (tampilkan_menu_login, tampilkan_menu_utama)

def menu_admin():
	while True:
		tampilkan_menu_utama()
		pilihan = input("Pilih menu: ").strip()

		if pilihan == "1":
			edit_profil()

		elif pilihan == "2":
			tambah_akun_customer()

		elif pilihan == "3":
			tambah_akun_driver()

		elif pilihan == "4":
			hapus_akun()

		elif pilian == "5":
			tampilkan_daftar_akun()
	
		elif pilihan == "6":
			logout()

		elif pilihan == "7":
			print("Terimakasih telah menggunakan program ini.")
			sys.exit()

		else:
			print("Pilihan tidak valid")
			input("Tekan Enter untuk kembali")
	
if __name__ == "__main__":
	while True:
		if apakah_sudah_login() == False: 
			tampilkan_menu_login()
			pilihan = input("Pilih menu: ")

			if pilihan == "1":
				login()
			
			elif pilihan == "2":
				registrasi()
			
			elif pilihan == "3":
				print("Terimakasih telah menggunakan program ini.")
				sys.exit()
			
			else:
				print("Pilihan tidak valid")
				input("Tekan Enter untuk kembali")

		else:
			username = apa_akun_sekarang()
			role = dapatkan_data_akun(username)["role"]

			if role == "admin":
				menu_admin()

			elif role == "manager":
				menu_manager()

			elif role == "pelanggan":
				menu_customer()

			elif role == "driver":
				menu_driver()
