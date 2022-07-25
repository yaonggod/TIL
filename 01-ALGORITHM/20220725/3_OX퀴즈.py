# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

def score(ox : str):
    n = 0 # 연속되는 O의 점수를 계산
    total = 0 # 총점을 계산
    # 첫 번째 항에 점수 부여
    if ox[0] == "O":
        n = 1
        total += n
    else: 
        n = 0
        total += n 
    for i in range(1, len(ox)):
        # O가 나타날 시 기존의 n에 1을 추가해 연속으로 점수 부여
        if ox[i] == "O":
            n += 1
            total += n
        # X가 나타날 시 n을 0으로 초기화
        else:
            n = 0
            total += n
    return total

T = int(input())
for i in range(T):
    ox = input() 
    print(score(ox))
    
