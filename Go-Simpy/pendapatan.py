import csv

CSV_FILE = "pendapatan.csv"

def baca_pendapatan(username_driver):
    data = []
    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username_driver:
                    data.append(row)
    except FileNotFoundError:
        open(CSV_FILE, "w").close()

    return data
