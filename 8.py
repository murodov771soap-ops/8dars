import csv

ism = input("Ismni kiriting: ")
yosh = input("Yoshni kiriting: ")
kurs = input("Kursni kiriting: ")

with open("students.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([ism, yosh, kurs])

with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print("Fayldagi barcha ma'lumotlar:")
    for row in reader:
        print(row)