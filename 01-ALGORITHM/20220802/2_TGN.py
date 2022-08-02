# https://www.acmicpc.net/problem/5063
t = int(input())
for i in range(t):
    r, e, c = map(int, input().split())
    # 수익 = 매출 - 비용 
    if r < e - c:
        print('advertise')
    elif r == e - c:
        print('does not matter')
    else:
        print('do not advertise')