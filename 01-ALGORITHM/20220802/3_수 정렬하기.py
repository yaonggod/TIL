# https://www.acmicpc.net/problem/2750
import heapq
n = int(input())
heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))

for i in range(n):
    # 최소 힙이므로 오름차순 정렬
    print(heapq.heappop(heap))