from pprint import pprint
n, m = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    # 인접 행렬
    matrix[u][v] = 1
    # 인접 리스트
    graph[u].append(v)

pprint(matrix)
print(graph)


