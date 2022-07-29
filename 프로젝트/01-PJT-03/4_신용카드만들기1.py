import sys

sys.stdin = open("_신용카드만들기1.txt")

t = int(input())
for i in range(1, t + 1):
    # 룬 공식 계산을 위해 int형으로 카드 번호를 받음
    card = list(map(int, input().split()))
    sum_card = 0
    for j in range(len(card)):
        if j % 2 == 0:
            sum_card += card[j] * 2
        else:
            sum_card += card[j]
    # sum_card + n 이 10의 배수가 될 때까지 n을 1씩 증가시키며 확인 
    n = 0
    while True:
        if (sum_card + n) % 10 == 0:
            break
        n += 1
    print("#{}".format(i), n)
