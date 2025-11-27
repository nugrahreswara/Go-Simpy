from akun import akun

def validasi_input_umur(umur):
	try:
		umur = int(umur)
		return umur if 13 <= umur <= 100 else None

		""" Sama aja kayak gini:
		if 1 <= umur <= 150:
			return umur
		
		else:
			return None
		"""

	except (ValueError, TypeError):
		return None

def email_valid(email):
	return "@" in email and "." in email 

def nomor_terdaftar(nomor_telepon):
	for data in akun.values():
		if data.get("nomor_telepon") == nomor_telepon:
			return True
	return False

def email_terdaftar(alamat_email):
	for data in akun.values():
		if data.get("alamat_email") == alamat_email:
			return True
	return False	

def username_terdaftar(username):
	return username in akun

def validasi_input_jarak(jarak):
	try:
		jarak = float(jarak)
		jarak = round(jarak, 1)
		if jarak <= 0:
			print("Jarak harus lebih dari 0.0!")
			return None

	except ValueError:
		print("Mohon masukkan jarak yang valid (contoh 2.5, 10, 0.8)")
		input("Tekan Enter untuk kembali...")
		return None