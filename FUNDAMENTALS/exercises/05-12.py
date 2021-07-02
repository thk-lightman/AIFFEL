import json

person = {
    "first name": "Yuna",
    "last name": "Jung",
    "age": 33,
    "nationality": "South Korea",
    "education": [
        {
            "degree": "B.S degree",
            "university": "Daehan university",
            "major": "mechanical engineering",
            "graduated year": 2010,
        }
    ],
}

# json 파일로 저장하기
with open("person.json", "w") as f:
    json.dump(person, f)

# json 파일의 내용을 파이썬 dict 객체로 읽어오기
# encoding => utf-8
with open("person.json", "r", encoding="utf-8") as f:
    contents = json.load(f)  # json load
    print(contents["first name"])
    print(contents["education"])
