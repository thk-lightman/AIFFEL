billboardchart = {
    1: ["Tho Box", "Roddy Ricch", "2019-12-19"],
    2: ["Don't Start Now", "Dua Lipa", "2019-11-01"],
    3: ["Life Is Good", "Future Featuring Drake", "2020-02-10"],
    4: ["Blinding", "The Weeknd", "2019-11-29"],
    5: ["Circles", "Post Malone", "2019-08-30"],
}

# 딕셔너리의 value들을 csv 파일로 저장
with open("billboardchart.csv", "w") as f:
    for i in billboardchart.values():  # 딕셔너리의 value만 불러온다
        data = ",".join(i)  # ,로 분리
        f.write(data + "\n")  # 개행
