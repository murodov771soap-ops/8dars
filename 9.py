import csv

jami = 0
max_xarajat = 0
eng_katta = ""
soni = 0

with open("expenses.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        summa = float(row["summa"])
        jami += summa
        soni += 1
        if summa > max_xarajat:
            max_xarajat = summa
            eng_katta = row["nom"]

print("Barcha xarajatlar summasi:", jami)
print("Eng katta xarajat:", eng_katta)
print("Xarajatlar soni:", soni)