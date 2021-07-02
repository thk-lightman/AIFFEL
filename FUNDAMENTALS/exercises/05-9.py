fields = ["title", "singer", "released date"]
rows = [
    ["Tho Box", "Roddy Ricch", "2019-12-19"],
    ["Don't Start Now", "Dua Lipa", "2019-11-01"],
    ["Life Is Good", "Future Featuring Drake", "2020-02-10"],
    ["Blinding", "The Weeknd", "2019-11-29"],
    ["Circles", "Post Malone", "2019-08-30"],
]

# - 3. 동일한 내용을 csv.writer를 이용해 수행해 봅니다.
import csv

filename = "test.csv"
with open(filename, "w+", newline="\n") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(fields)
    csv_writer.writerows(rows)
