import sys

sys.stdin = open("_창용마을무리의개수.txt")
from collections import deque
t = int(input())
for x in range(1, t + 1):
    n, m = map(int, input().split())
    # 인간관계 그래프
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # 너비 우선 탐색해서 인간관계 연걸 파악
    queue = deque()
    group = 0
    for i in range(1, n + 1):
        # 새로운 그룹의 시작
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            # 큐를 한 바퀴 다 돌아야 인간관계 한 무리 완성
            while queue:
                v = queue.popleft()
                for adj in graph[v]:
                    if not visited[adj]:
                        visited[adj] = True
                        queue.append(adj)
            group += 1
    print('#{} {}'.format(x, group))