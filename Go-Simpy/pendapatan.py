import csv
from prettytable import PrettyTable

def lihat_pendapatan(file_csv="Data.csv"):
    data = []
    with open(file_csv, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    table = PrettyTable()
    table.field_names = ["Waktu Pesan", "Nama Pelanggan", "Biaya Didapat"]

    total_biaya = 0
    for row in data:
        biaya = int(row["biaya_didapat"])
        total_biaya += biaya
        table.add_row([row["waktu_pesan"], row["nama_pelanggan"], biaya])

    print(table)
    print("Total pendapatan semua pelanggan: Rp {:,}".format(total_biaya).replace(",", "."))
    input("\nTekan Enter untuk kembali ke menu...")
