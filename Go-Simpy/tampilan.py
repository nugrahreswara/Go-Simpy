# Import Library
import os

# Import file
from akun import akun
from prettytable import PrettyTable
from autentikasi import (apakah_sudah_login, apa_akun_sekarang)
from manajemen_akun import dapatkan_data_akun

def bersihkan_layar():
	os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu_login():
	bersihkan_layar()
	print("Menu Login")
	print("1. Login")
	print("2. Registrasi")
	print("3. Keluar Program")

def tampilkan_menu_utama():
	bersihkan_layar()
	username = apa_akun_sekarang()
	data_akun = dapatkan_data_akun(username) 	
	print(f"Selamat datang, {data_akun['nama_lengkap']} ({username})")

	if data_akun["role"] == "admin":
		print("\n=== MENU ADMIN ===")
		print("1. Edit Profil")
		print("2. Tambah Akun Customer")
		print("3. Tambah Akun Driver")
		print("4. Hapus User")
		print("5. Lihat Daftar User")
		print("6. Logout")
		print("7. Keluar")
    
	elif data_akun["role"] == "customer":
		print("\n=== MENU CUSTOMER ===")
		print("1. Edit Profil")
		print("2. Pesan Gojek")
		print("3. Logout")
		print("4. Keluar")
	
	elif data_akun["role"] == "driver":
		print("\n=== MENU DRIVER ===")
		print("1. Edit Profil")
		print("2. Lihat pendapatan")
		print("3. Logout")
		print("4. Keluar")
