from collections import deque
computer = int(input())
edge_count = int(input())
# 인접 리스트
edges = [[] for _ in range(computer + 1)]
for _ in range(edge_count):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)
# 감염이 확인되었을 경우 True
virus = [False] * (computer + 1)
virus[1] = True

queue = deque([1])
while queue:
    # 감염되어서 큐에 들어가있는 원소
    n = queue.popleft()
    for i in range(len(edges[n])):
        # 감염되었으나 확인되지 않았을 경우 True로 바꿔줌
        if virus[edges[n][i]] == False:
            queue.append(edges[n][i])
            virus[edges[n][i]] = True

# 감염된 1번 컴퓨터를 제외하고 출력
print(virus.count(True) - 1)    
