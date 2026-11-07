import json

with open("product.json", "r", encoding="utf-8") as f:
    data = json.load(f)

umumiy_qiymat = data["narx"] * data["miqdor"]
print("Mahsulotning umumiy qiymati:", umumiy_qiymat)