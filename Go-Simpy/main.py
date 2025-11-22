import sys

from autentikasi import (login, logout, apakah_sudah_login, apa_akun_sekarang)
from manajemen_akun import (edit_profil, buat_akun_customer, buat_akun_driver, hapus_akun, dapatkan_data_akun, tampilkan_daftar_akun)
from tampilan import (tampilkan_menu_login, tampilkan_menu_utama)
<<<<<<< HEAD
from ewallet import (cek_saldo, isi_saldo, bayar_qris)
=======
>>>>>>> fd4a6082e9c24f965bda0cc311df0c9aab452e57

def pilihan_menu_admin():
	while True:
		tampilkan_menu_utama()
		pilihan = input("Pilih menu: ").strip()
		if pilihan == "1":
			edit_profil()

		elif pilihan == "2":
			buat_akun_customer()

		elif pilihan == "3":
			buat_akun_driver()

		elif pilihan == "4":
			hapus_akun()

		elif pilihan == "5":
			tampilkan_daftar_akun()
	
		elif pilihan == "6":
			logout()
			break

		elif pilihan == "7":
			print("Terimakasih telah menggunakan program ini.")
			sys.exit()

		else:
			print("Pilihan tidak valid")
			input("Tekan Enter untuk kembali")


def pilihan_menu_customer():
	while True:
		tampilkan_menu_utama()
		pilihan = input("Pilih menu: ").strip()

		if pilihan == "1":
			edit_profil()

		elif pilihan == "2":
			cek_saldo(username)

		elif pilihan == "3":
			try:
				jumlah = int(input("Masukkan jumlah isi saldo: "))
			except ValueError:
				print("Nominal harus berupa angka.")
				input("Tekan Enter untuk kembali")
				continue
			isi_saldo(username, jumlah)

		elif pilihan == "4":
			try:
				jumlah = int(input("Masukkan nominal QRIS: "))
			except ValueError:
				print("Nominal harus berupa angka.")
				input("Tekan Enter untuk kembali")
				continue
			bayar_qris(username, jumlah)

		elif pilihan == "5":
			logout()
			break

		elif pilihan == "6":
			print("Terimakasih telah menggunakan program ini.")
			sys.exit()

		else:
			print("Pilihan tidak valid")
			input("Tekan Enter untuk kembali")
	

def pilihan_menu_driver():
	while True:
		tampilkan_menu_utama()
		pilihan = input("Pilih menu: ").strip()

		if pilihan == "1":
			edit_profil()

		elif pilihan == "2":
			cek_saldo()

		elif pilihan == "3":
			lihat_pendapatan()

		elif pilihan == "4":
			logout()
			break

		elif pilihan == "5":
			print("Terimakasih telah menggunakan program ini.")
			sys.exit()

		else:
			print("Pilihan tidak valid")
			input("Tekan Enter untuk kembali")
	

if __name__ == "__main__":
	while True:
		if not apakah_sudah_login(): 
			tampilkan_menu_login()
			pilihan = input("Pilih menu: ")

			if pilihan == "1":
				login()
			
			elif pilihan == "2":
				buat_akun_customer()

			elif pilihan == "3":
				buat_akun_driver()
			
			elif pilihan == "4":
				print("Terimakasih telah menggunakan program ini.")
				sys.exit()
			
			else:
				print("Pilihan tidak valid")
				input("Tekan Enter untuk kembali")

		else:
			# username = apa_akun_sekarang()
			role = dapatkan_data_akun(apa_akun_sekarang())["role"]
			
			if role == "admin":
				pilihan_menu_admin()

			elif role == "customer":
				pilihan_menu_customer()

			elif role == "driver":
				pilihan_menu_driver()
