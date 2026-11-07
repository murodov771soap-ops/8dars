import csv

with open("products.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("Barcha mahsulotlar:")
    max_narx = 0
    eng_qimmat = ""
    for row in reader:
        print(row["nom"])
        umumiy = float(row["narx"]) * int(row["miqdor"])
        print(f"Umumiy qiymati: {umumiy}")
        if float(row["narx"]) > max_narx:
            max_narx = float(row["narx"])
            eng_qimmat = row["nom"]

print("Eng qimmat mahsulot:", eng_qimmat)