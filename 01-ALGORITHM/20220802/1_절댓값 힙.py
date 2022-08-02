# https://www.acmicpc.net/problem/11286
import heapq
import sys

heap = []
n = int(sys.stdin.readline())
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap == []:
            print(0)
        else:
            # 최소 힙이므로 가장 작은 값을 pop함
            y = heapq.heappop(heap)
            print(y[0] * y[1])
    else:
        # (x, y)로 push 받았을 시 x가 같은 값이면 y를 정렬함
        # (1, -1), (1, 1) 순으로 정렬
        # x는 입력값의 절댓값, y는 입력값의 부호를 나타냄
        heapq.heappush(heap, (x if x > 0 else -x, 1 if x > 0 else -1))