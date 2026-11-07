import json

with open("phone.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Telefon modeli:", data["model"])
yangi_narx = int(input("Yangi narxni kiriting: "))
data["narx"] = yangi_narx

with open("phone.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)