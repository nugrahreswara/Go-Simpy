import os
import random
import pandas as pd
from datetime import datetime
from akun import akun
from autentikasi import apa_akun_sekarang
from validasi_input import validasi_input_jarak
from prettytable import PrettyTable

# def cek_file_csv():
#     kolom_valid = ["Waktu", "Customer", "Driver", "Jarak", "Harga"]
#     try:
#         df = pd.read_csv("transaksi.csv")

#     except (FileNotFoundError, pd.errors.EmptyDataError):
#         df = pd.DataFrame(columns=kolom_valid)
#         df.to_csv(file_path, index=False)

#         kolom_transaksi = list(df.columns)

#         if kolom_transaksi == kolom_valid:
#             return

#         else:
#             kolom_baru = pd.DataFrame(columns=kolom_valid)
#             for col in kolom_valid:
#                 if col in kolom_transaksi:
#                     kolom_baru[col] = df[col]
#                 else:
#                     kolom_baru[col] = pd.NA
#             kolom_baru.to_csv("transaksi.csv", index=False)

def daftar_driver():
    global akun
    daftar_driver = []
    for username, data in akun.items():
        if data["role"] == "driver":
            daftar_driver.append(username)
    return daftar_driver

def pesan_ojek():
    username = apa_akun_sekarang()
    if not daftar_driver():
        print("Tidak ada driver tersedia.")
        input("Tekan Enter untuk kembali...")
        return
    
    jarak = input("Masukkan berapa km jarak yang ingin anda tuju: ")
    if not jarak:
        print("Jarak tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")

    try:
        jarak = float(jarak)
        jarak = round(jarak, 1)
        if jarak <= 0:
            print("Jarak harus lebih dari 1 km!")
            input("Tekan Enter untuk kembali...")
            return

    except ValueError:
        print("Mohon masukkan angka yang valid (contoh 2.5, 10, 0.8)")
        input("Tekan Enter untuk kembali...")
        return
    
    driver_terpilih = random.choice(daftar_driver())
    harga = jarak * 7000
    waktu = datetime.now().strftime("Tanggal: %d-%m-%Y Jam: %H:%M:%S")

    transaksi = pd.read_csv("transaksi.csv")
    transaksi = pd.concat([
                    transaksi, pd.DataFrame([{
                        "Customer" : username,
                        "Driver" : driver_terpilih,
                        "Jarak" : jarak,
                        "Harga" : harga,
                        "Waktu" : waktu
                    }])
                ], ignore_index=True)
    transaksi.to_csv("transaksi.csv", index=False)

    print("Pesanan berhasil!")
    print(f"Jarak: {jarak} km")
    print(f"Harga: Rp{harga:,.0f}")
    print(f"Driver: {driver_terpilih}")
    print("Pesan Ojek Online selesai... selamat menikmati perjalananmu!")
    print()
    input("Tekan Enter untuk kembali...")

def lihat_pendapatan():
    username = apa_akun_sekarang()
    pendapatan_driver = pd.read_csv("transaksi.csv")
    pendapatan_driver = pendapatan_driver[pendapatan_driver["Driver"] == username]

    if pendapatan_driver.empty:
        print(f"Belum ada pendapatan untuk {username}.")
        input("Tekan Enter untuk kembali...")
        return

    total = pendapatan_driver["Harga"].sum()

    tabel_pendapatan = PrettyTable()
    tabel_pendapatan.field_names = ["Waktu", "Customer", "Jarak (km)", "Pendapatan (Rp)"]

    for index, data in pendapatan_driver.iterrows():
        waktu = data["Waktu"]
        customer = data["Customer"]
        jarak = f"{data['Jarak']:,.1f}"
        pendapatan = f"{data['Harga']:.0f}"
        tabel_pendapatan.add_row([waktu, customer, jarak, pendapatan])

    print(f"\nRiwayat Pendapatan untuk {username}:")
    print(tabel_pendapatan)
    print(f"\nTotal Pendapatan: Rp{total:,.0f}")
    input("Tekan Enter untuk kembali...")

def lihat_histori():
    histori = pd.read_csv("transaksi.csv")
    histori = histori[histori["Customer"] == apa_akun_sekarang()]

    if histori.empty:
        print(f"belum ada histori pemesanan untuk {apa_akun_sekarang()}.")
        input("Tekan Enter untuk kembali...")
        return

    tabel_histori = PrettyTable()
    tabel_histori.field_names = ["Waktu", "Driver", "Jarak (km)", "Harga (Rp)"]

    for index, data in histori.iterrows():
        waktu = data["Waktu"]
        driver = data["Driver"]
        jarak = f"{data['Jarak']:,.1f}"
        harga = f"{data['Harga']:.0f}"
        tabel_histori.add_row([waktu, driver, jarak, harga])

    print(f"\nHistori Pemesanan untuk {apa_akun_sekarang()}:")
    print(tabel_histori)
    input("Tekan Enter untuk kembali...")


def lihat_semua_pendapatan():
    transaksi = pd.read_csv("transaksi.csv")
    
    tabel_transaksi = PrettyTable()
    tabel_transaksi.field_names = ["Waktu", "Customer", "Driver", "Jarak (km)", "Harga (Rp)"]

    for index, data in transaksi.iterrows():
        waktu = data["Waktu"]
        customer = data["Customer"]
        driver = data["Driver"]
        jarak = f"{data['Jarak']:,.1f}"
        harga = f"{data['Harga']:.0f}"
        tabel_transaksi.add_row([waktu, customer, driver, jarak, harga])

    print(f"\nSemua transaksi Go-Simpy")
    print(tabel_transaksi)
    input("Tekan Enter untuk kembali...")