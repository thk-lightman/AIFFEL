import csv

header = ["title", "singer", "released date"]

with open("billboardchart.csv", "r") as inputfile:
    with open("billboardchart_out.csv", "w", newline="\n") as outputfile:
        fi = csv.reader(
            inputfile, delimiter=","
        )  # 지정된 csvfile의 줄을 이터레이트 하는 판독기(reader) 객체를 반환

        fo = csv.writer(
            outputfile, delimiter=","
        )  # 지정된 파일류 객체에 분리된 문자열로 사용자의 데이터를 변환하는 기록기(writer) 객체를 반환

        fo.writerow(header)  # 헤더 파일 작성

        for row in fi:
            fo.writerow(row)
