# - 1. 데이터를 준비합니다.
fields = ["title", "singer", "released date"]
rows = [
    ["Tho Box", "Roddy Ricch", "2019-12-19"],
    ["Don't Start Now", "Dua Lipa", "2019-11-01"],
    ["Life Is Good", "Future Featuring Drake", "2020-02-10"],
    ["Blinding", "The Weeknd", "2019-11-29"],
    ["Circles", "Post Malone", "2019-08-30"],
]

# - 2. 판다스를 이용해 데이터를 csv 파일로 저장합니다.
import pandas as pd

df = pd.DataFrame(rows, columns=fields)
df.to_csv("pandas.csv", index=False)

# CSV 파일 읽어서 DataFrame으로 저장
df = pd.read_csv("pandas.csv")
print(df.head())
