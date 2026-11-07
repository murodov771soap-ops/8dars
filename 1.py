import json

with open("user.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Ism va yoshi:", data["ism"], data["yosh"])
print("Shahar:", data["shahar"])