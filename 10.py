import csv

with open("sportchilar.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    max_ball = -1
    eng_yuqori = ""
    print("Barcha sportchilar:")
    for row in reader:
        print(row["ism"])
        ball = int(row["ball"])
        if ball > 80:
            print(f"80 balldan yuqori: {row['ism']} ({ball} ball)")
        if ball > max_ball:
            max_ball = ball
            eng_yuqori = row["ism"]

print("Eng yuqori ball olgan sportchi:", eng_yuqori)