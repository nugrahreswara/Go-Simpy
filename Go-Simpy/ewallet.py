saldo = 0

def isi_saldo(jumlah):
    global saldo
    if jumlah > 0:
        saldo += jumlah
        print(f"Saldo berhasil ditambahkan. Saldo sekarang: {saldo}")
    else:
        print("Jumlah isi saldo harus lebih dari 0.")

def cek_saldo():
    print(f"Saldo Anda saat ini adalah: {saldo}")