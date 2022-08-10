# https://www.acmicpc.net/problem/11724
# python3은 시간 초과, pypy3은 통과
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
  
visited = [False] * (n + 1)

cc_count = 0
stack = []
# 0을 제외한 모든 정점을 다 돌았을 때 while문이 끝남
while visited.count(False) != 1:
    # 1부터 n까지의 정점 중 방문하지 않은 정점부터 시작해서 DFS
    for i in range(1, n + 1):
        if not visited[i]:
            # 방문 처리
            stack.append(i)
            visited[i] = True
            # 시작 노드로부터 연결된 모든 노드를 탐색하면 연결 요소가 한 개 완성됨
            while stack:
                v = stack.pop()
                for adj in graph[v]:
                    if not visited[adj]:
                        visited[adj] = True
                        stack.append(adj)
            # 다음 번 연결 요소 탐색을 위해 1 더해줌
            cc_count += 1

print(cc_count)