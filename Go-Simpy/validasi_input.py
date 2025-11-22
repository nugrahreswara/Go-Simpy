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

