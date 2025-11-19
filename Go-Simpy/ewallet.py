from manajemen_akun import dapatkan_data_akun
from pendapatan import baca_pendapatan

def cek_saldo(username):
    data = dapatkan_data_akun(username)
    print(f"Saldo Anda saat ini: Rp {data['saldo']}")
    input("Tekan Enter...")

def isi_saldo(username, jumlah):
    data = dapatkan_data_akun(username)
    if jumlah > 0:
        data["saldo"] += jumlah
        print(f"Isi saldo berhasil! Saldo sekarang: Rp {data['saldo']}")
    else:
        print("Jumlah harus lebih dari 0.")
    input("Tekan Enter...")

def bayar_qris(username, jumlah):
    data = dapatkan_data_akun(username)
    if jumlah > data["saldo"]:
        print("Saldo tidak cukup!")
    else:
        data["saldo"] -= jumlah
        print(f"Pembayaran QRIS berhasil! Sisa saldo: Rp {data['saldo']}")
    input("Tekan Enter...")
    

def hitung_total_pendapatan(username):
    data = baca_pendapatan(username)
    total = sum(int(row[1]) for row in data)
    return total

def tarik_pendapatan(username):
    data = dapatkan_data_akun(username)
    total = hitung_total_pendapatan(username)

    print("\n=== TARIK PENDAPATAN ===")
    print(f"Total pendapatan Anda: Rp {total}")

    if total == 0:
        print("Tidak ada pendapatan untuk ditarik.")
        input("Enter...")
        return

    konfirmasi = input("Tarik seluruh pendapatan? (y/n): ").lower()
    if konfirmasi != "y":
        print("Dibatalkan.")
        input("Enter...")
        return

    data["saldo"] += total
    print(f"Berhasil! Saldo driver bertambah: Rp {total}")
    print(f"Saldo baru: Rp {data['saldo']}")
    input("Enter...")
