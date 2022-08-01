from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = [] # 전체 책의 순서를 이중 리스트 없이 그냥 리스트에 넣기, 이중 리스트 쓰면 시간초과
k_i = [] # 더미별 책의 개수
for i in range(m):
    k = int(input())
    k_i.append(k)
    lst += list(map(int, input().split()))
    
result = [] # result에 0이 있으면 불가능한 경우
queue = deque(lst)
for i in range(m):
    for j in range(k_i[i] - 1):
        # 모든 더미 내부에서 책이 내림차순으로 있으면 가능함
        if queue[j] < queue[j + 1]:
            result.append(0)
    # 검사 후 검사한 더미의 책들은 pop해서 다음 더미 검사
    for _ in range(k_i[i]):
        queue.popleft() 

if 0 in result:
    print('No')
else:
    print('Yes')