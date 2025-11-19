from akun import akun

def jumlah_saldo(username):
	return akun["saldo"]

def isi_saldo(jumlah):
	global saldo

	if jumlah > 0:
		saldo += jumlah
		print(f"Saldo berhasil ditambahkan. Saldo sekarang: {jumlah_saldo}")
	else:
		print("Jumlah isi saldo harus lebih dari 0.")

def cek_saldo():
	print(f"Saldo Anda saat ini adalah: {jumlah_saldo}")

def bayar_qris():
	print("Tes")
