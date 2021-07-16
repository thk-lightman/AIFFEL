from random import randrange


class FunnyDice:
    def __init__(self, n=6):  # 기본 6면체
        self.n = int(n)  # n면체 주사위
        self.numbers = list(range(1, n + 1))  # 주사 번호들
        self.index = randrange(0, self.n)  # numbers 변수의 인덱스
        self.val = self.numbers[self.index]  # 주사위의 눈

    # 랜덤으로 주사위 눈이 나오게 한다
    def throw(self):
        self.index = randrange(0, self.n)
        self.val = self.numbers[self.index]

    # 주사위 눈의 값을 얻는다
    def getval(self):
        return self.val

    # 사용자가 주사위 눈을 세팅할 수 있게 한다
    def setval(self, val):
        if val <= self.val:
            self.val = val
        else:
            msg = f"주사위에 없는 숫자입니다. 주사위는 1 ~ {self.n}까지 있습니다."
            raise ValueError(msg)


def get_inputs():
    n = int(input("주사위 면의 개수를 입력하세요: "))
    return n


def main():
    n = get_inputs()  # 주사위 면 수 입력 받는다
    mydice = FunnyDice(n)
    mydice.throw()
    mydice.getval()
    print(f"행운의 숫자는 {mydice.getval()}")
    # mydice.setval(7)


main()
