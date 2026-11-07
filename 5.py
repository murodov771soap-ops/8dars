import csv

with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("Barcha o'quvchilar:")
    for row in reader:
        print(row["ism"])
        if int(row["yosh"]) > 20:
            print(f"20 yoshdan katta: {row['ism']}")