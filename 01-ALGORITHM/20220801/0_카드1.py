from collections import deque
n = int(input())
queue = deque(range(1, n + 1))

i = 0
while True:
    if queue == deque([]):
        break
    if i % 2 == 0:
        # 2n - 1번째 카드는 버리기
        a = queue.popleft()
        print(a, end = ' ')
    else:
        # 2n번째 카드는 제일 뒤로 옮기기
        b = queue.popleft()
        queue.append(b)
    i += 1
    