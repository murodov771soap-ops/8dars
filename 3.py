import json

with open("student.json", "r", encoding="utf-8") as f:
    data = json.load(f)

data["ball"] = 95

with open("student.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)