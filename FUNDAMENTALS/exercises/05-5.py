f = open("hello.txt", "w")

for i in range(10):
    f.write("hello\n")

f.close()

with open("hello.txt", "r") as f:
    print(f.read())
