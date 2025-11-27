import sys
import os
import pandas as pd
from autentikasi import (login, logout, apakah_sudah_login, apa_akun_sekarang)
from manajemen_akun import (edit_profil, buat_akun, hapus_akun, dapatkan_data_akun, tampilkan_daftar_akun)
from tampilan import (tampilkan_menu_login, tampilkan_menu_utama)
from sistem_pemesanan import (pesan_ojek, lihat_pendapatan, lihat_histori, lihat_semua_pendapatan)

def pilihan_menu_admin():
	while True:
		tampilkan_menu_utama(role)
		pilihan = input("Pilih menu: ").strip()
		if pilihan == "1":
			edit_profil()

		elif pilihan == "2":
			buat_akun(pilihan)

		elif pilihan == "3":
			buat_akun(pilihan)

		elif pilihan == "4":
			hapus_akun()

		elif pilihan == "5":
			tampilkan_daftar_akun()
	
		elif pilihan == "6":
			lihat_semua_pendapatan()

		elif pilihan == "7":
			logout()
			break

		elif pilihan == "8":
			print("Terimakasih telah menggunakan program ini.")
			sys.exit()

		else:
			print("Pilihan tidak valid")
			input("Tekan Enter untuk kembali...")


def pilihan_menu_customer():
	while True:
		tampilkan_menu_utama(role)
		pilihan = input("Pilih menu: ").strip()

		if pilihan == "1":
			edit_profil()

		elif pilihan == "2":
			pesan_ojek()
		
		elif pilihan == "3":
			lihat_histori()

		elif pilihan == "4":
			logout()
			break

		elif pilihan == "5":
			print("Terimakasih telah menggunakan program ini.")
			sys.exit()

		else:
			print("Pilihan tidak valid")
			input("Tekan Enter untuk kembali")
	

def pilihan_menu_driver():
	while True:
		tampilkan_menu_utama(role)
		pilihan = input("Pilih menu: ").strip()

		if pilihan == "1":
			edit_profil()

		elif pilihan == "2":
			lihat_pendapatan()

		elif pilihan == "3":
			logout()
			break

		elif pilihan == "4":
			print("Terimakasih telah menggunakan program ini.")
			sys.exit()

		else:
			print("Pilihan tidak valid")
			input("Tekan Enter untuk kembali")
	

if __name__ == "__main__":
	file_path = "transaksi.csv"
	expected_header = "Waktu,Customer,Driver,Jarak,Harga"

	# Cek apakah file ada
	if not os.path.exists(file_path):
		# Buat file baru dengan header yang benar
		with open(file_path, "w", encoding="utf-8") as f:
			f.write(expected_header + "\n")
	else:
		with open(file_path, "r", encoding="utf-8") as f:
			lines = f.readlines()

		if not lines:
			# File kosong → tulis header saja
			with open(file_path, "w", encoding="utf-8") as f:
				f.write(expected_header + "\n")
		else:
			current_header = lines[0].strip()
			expected_header_stripped = expected_header.strip()

			# Bandingkan header (abaikan spasi tambahan)
			if current_header.replace(" ", "") != expected_header_stripped.replace(" ", ""):
				print("Kolom transaksi tidak valid")
				# Ganti hanya baris pertama, sisanya tetap
				with open(file_path, "w", encoding="utf-8") as f:
					f.write(expected_header + "\n")
					# Tulis semua baris data (dari baris ke-2 dst) tanpa ubah apa pun
					f.writelines(lines[1:])

	while True:
		if not apakah_sudah_login(): 
			tampilkan_menu_login()
			pilihan = input("Pilih menu: ")

			if pilihan == "1":
				login()
			
			elif pilihan == "2":
				buat_akun(pilihan)

			elif pilihan == "3":
				buat_akun(pilihan)
			
			elif pilihan == "4":
				print("Terimakasih telah menggunakan program ini.")
				sys.exit()
			
			else:
				print("Pilihan tidak valid")
				input("Tekan Enter untuk kembali")

		else:
			role = dapatkan_data_akun(apa_akun_sekarang())["role"]
			
			if role == "admin":
				pilihan_menu_admin()

			elif role == "customer":
				pilihan_menu_customer()

			elif role == "driver":
				pilihan_menu_driver()
