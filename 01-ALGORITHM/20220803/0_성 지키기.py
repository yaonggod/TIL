# https://www.acmicpc.net/problem/1236
n, m = map(int, input().split())
castle = [list(input()) for _ in range(n)] # 가로줄
castle2 = [[] for _ in range(m)] # 세로줄
for i in range(m):
    for j in range(n):
        castle2[i].append(castle[j][i])

count = 0   
for i in range(n):
    for j in range(m):
        if 'X' not in castle[i] and 'X' not in castle2[j]:
            castle[i][j] = 'X'
            castle2[j][i] = 'X'
            count += 1
# 가로줄 검증
for i in range(n):
    if 'X' not in castle[i]:
        count += 1
# 세로줄 검증
for j in range(m):
    if 'X' not in castle2[j]:
        count += 1
        
print(count)