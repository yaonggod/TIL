# https://www.acmicpc.net/problem/2644
import sys
n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

# [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]] 

# 촌수가 확인이 안되면 방문하지 않고 -1로 둠
# 촌수가 확인이 되면 이전 노드의 촌수에서 1을 더해줌
visited = [[False, -1]] * (n + 1)
stack = [a]
# 기준이 되는 사람의 방문 처리, 촌수는 0
visited[a] = [True, 0]
while stack:
    v = stack.pop()
    # 연결이 되어있는 사람들 중 = 친척들 중
    for adj in graph[v]:
        # 촌수 확인이 안되어있으면
        if visited[adj][0] == False:
            stack.append(adj)
            # 방문 처리하고 촌수를 1 늘려줌
            visited[adj] = [True, visited[v][1] + 1]
            
print(visited[b][1])




