# https://www.acmicpc.net/problem/1292

a, b = map(int, input().split())

# (1), (2 ~ 3), (4 ~ 6), (7 ~ 10), ... ((n - 1)n // 2 ~ n(n + 1) // 2)

# n이 몇 번째 구간에 속해있는지 돌려주는 함수
def position(n):
    i = 1
    while True:
        if n <= (i * (i + 1)) // 2:
            break
        i += 1
    return i

total = 0
for i in range(a, b + 1):
    total += position(i)
    
print(total)
