import sys
import os
import pandas as pd
from autentikasi import (login, logout, apakah_sudah_login, apa_akun_sekarang)
from manajemen_akun import (edit_profil, buat_akun, hapus_akun, dapatkan_data_akun, tampilkan_daftar_akun)
from tampilan import (tampilkan_menu_login, tampilkan_menu_utama)
<<<<<<< HEAD
from pendapatan import lihat_pendapatan 
import time
import random
from tampilan import DOUBLE_LINE

def pesan_ojek():
    DOUBLE_LINE("PESAN OJEK")
    print()
    lokasi = input("Lokasi penjemputan : ")
    tujuan = input("Tujuan perjalanan  : ")

    print("\nDetail Pesanan")
    print("-" * 30)
    print(f"- Lokasi Jemput : {lokasi}")
    print(f"- Tujuan        : {tujuan}")
    print("-" * 30)

    confirm = input("Pesan ojek? (y/n): ").strip().lower()

    if confirm == "y":
        drivers = ["Agung", "Budi", "Rama", "Tono", "Fajar"]
        motor = ["Vario 125", "Beat Street", "NMax", "Scoopy", "Aerox"]
        selected_driver = random.choice(drivers)
        selected_motor = random.choice(motor)
        biaya = random.randint(10000, 20000)

        print("\nMencari driver", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)

        print(f"\n\nDriver ditemukan!")
        print(f"- Nama Driver : {selected_driver}")
        print(f"- Motor       : {selected_motor}")
        print(f"- Harga       : Rp {biaya:,}")
        print("\nDriver sedang menuju lokasi Anda!")
    else:
        print("\nPesanan dibatalkan.")

    input("\nTekan Enter untuk kembali ke menu...")
=======
from sistem_pemesanan import (pesan_ojek, lihat_pendapatan, lihat_histori, lihat_semua_pendapatan)
>>>>>>> 19c8c5a1f06eb936e03b05e82fa54cdb4cd8911b

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
