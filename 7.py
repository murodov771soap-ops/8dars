import json

talaba = {
    "ism": "Sardor",
    "yosh": 20,
    "kurs": 2
}

json_str = json.dumps(talaba, ensure_ascii=False)
print("JSON matn:", json_str)

qayta_dict = json.loads(json_str)
print("Talabaning ismi:", qayta_dict["ism"])