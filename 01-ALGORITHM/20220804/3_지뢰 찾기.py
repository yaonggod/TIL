# https://www.acmicpc.net/problem/4396
n = int(input())
# 지뢰
trap = [list(input()) for _ in range(n)]
# 오픈된 칸
open = [list(input()) for _ in range(n)]
# 해답 칸
answer = [['.'] * n for _ in range(n)]
# 지뢰를 밟아서 졌을 때
lose = False
# 방향 8가지
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

# 0 1 2
# 7 X 3
# 6 5 4

for i in range(n):
    for j in range(n):
        if open[i][j] == 'x': 
            # 지뢰를 밟았을 때
            if trap[i][j] == '*':
                lose = True
            # 8방향 지뢰 탐색해서 count에 더해주기
            count = 0
            for a in range(8):
                if i + dx[a] >= 0 and i + dx[a] <= n - 1 and j + dy[a] >= 0 and j + dy[a] <= n - 1:
                    if trap[i + dx[a]][j + dy[a]] == '*':
                        count += 1
            answer[i][j] = count
# 졌을 때 모든 지뢰를 노출시켜주기            
if lose:
    for i in range(n):
        for j in range(n):
            if trap[i][j] == '*':
                answer[i][j] = '*'

for i in range(n):
    for j in range(n):
        print(answer[i][j], end = '')
    print()
                        
