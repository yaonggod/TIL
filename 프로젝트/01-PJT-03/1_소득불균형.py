import sys

sys.stdin = open("_소득불균형.txt")

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    income = list(map(int, input().split()))
    average_income = sum(income) / n
    
    # 평균 소득 이하인 사람들을 count변수로 세주기
    count = 0
    for j in range(n):
        if income[j] <= average_income:
            count += 1
    print("#{}".format(i), count)