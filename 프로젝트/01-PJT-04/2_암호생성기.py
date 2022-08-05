import sys
from collections import deque

sys.stdin = open("_암호생성기.txt")
for x in range(1, 11):
    n = int(input())
    # 암호 리스트를 큐로 만듬
    queue = deque(list(map(int, input().split())))
    # 감소하는 숫자는 1에서 시작
    minus = 1
    while True:
        # 큐의 맨 뒷자리 수가 0이면 종료
        if queue[-1] == 0:
            break
        # 감소하는 숫자가 앞 단계에서 1 더해져서 6이 되면 다시 1부터 시작
        if minus == 6:
            minus = 1
        # 맨 왼쪽의 숫자를 minus만큼 감소시킨 뒤 append함
        x = queue.popleft() - minus
        # x가 음수가 되면 0으로 맞춰줌
        if x < 0:
            x = 0
        queue.append(x)
        # 다음 단계를 위해 감소하는 숫자 1 증가
        minus += 1
        
    print('#{}'.format(n), end = ' ')
    for i in range(8):
        print(queue[i], end = ' ')
    print()