# https://www.acmicpc.net/problem/1926
import sys
from collections import deque

sys.stdin = open('3_그림.txt')
n, m = map(int, sys.stdin.readline().split())
pic = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def bfs(a, b, pic, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # (a, b)에서 시작하므로 시작 size = 1
    size = 1
    queue = deque([(a, b)])
    # 방문 처리
    visited[a][b] = True
    # (a, b)에서 연결된 모든 노드를 탐색
    while queue:
        x, y = queue.popleft()
        # 상 하 좌 우
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위 내에 있고, 그림이고, 방문 처리가 안되어있을시
            if 0 <= nx < n and 0 <= ny < m and pic[nx][ny] == 1 and not visited[nx][ny]:
                # 방문 처리를 하고
                visited[nx][ny] = True
                # 다음 노드에서 연결된 모든 그림을 탐색
                queue.append((nx, ny))
                # 연결된 그림으로 인정받았으므로 그림 크기 += 1
                size += 1
    return size

pic_size = []
# (0, 0)부터 시작해서 그림 탐색
for i in range(n):
    for j in range(m):
        if pic[i][j] == 1 and not visited[i][j]:
            size = bfs(i, j, pic, visited)
            pic_size.append(size)
# 그림이 하나도 없을 시 둘 다 0 출력
if len(pic_size) == 0:
    print(0)
    print(0)
else:
    print(len(pic_size))
    print(max(pic_size))
