total = 0
count = 0
numbers = input("Enter a number :  (<Enter Key> to quit)")

while numbers != "":  # while 문에 아무것도 입력이 안될 때까지 합 구한다
    try:
        x = float(numbers)
        count += 1
        total = total + x
    except ValueError:
        print("NOT a number! Ignored..")
    numbers = input("Enter a number :  (<Enter Key> to quit)")
avg = total / count
print("\n average is", avg)
