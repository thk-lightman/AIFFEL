import os

# 파일 이름을 리스트 형태로 저장
photo = os.listdir("/Users/t1won/Documents/blog thumbnail")

# png로 끝나는 파일들만 png 리스트에 저장
png = [png for png in photo if png.endswith(".png")]

print(photo)
