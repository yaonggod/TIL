# https://www.acmicpc.net/problem/13567
import sys
sys.stdin = open('2_로봇.txt')
m, n = map(int, sys.stdin.readline().split())
# 시작 좌표
x = y = 0
# x, y 중 어느 좌표를 어느 방향으로 움직이는지 정보
# 왼쪽으로 90도씩 돌 때, 오른쪽은 -1씩 하면 됨
move = [['x', 1], ['y', 1], ['x', -1], ['y', -1]]
# 시작 방향
i = 0
# 도중에 break되면 -1 출력하고 else문이 실행되지 않음
for _ in range(n):
    command, num = map(str, sys.stdin.readline().split())
    # MOVE : 지정된 좌표를 방향대로 num만큼 움직여줌
    if command == 'MOVE':
        if move[i][0] == 'x':
            x += move[i][1] * int(num)
        else:
            y += move[i][1] * int(num)
    # TURN : 방향 바꿔줌
    else:
        # 왼쪽으로 돌 때
        if num == '0':
            i = (i + 1) % 4
        # 오른쪽으로 돌 때
        else:
            i = (i - 1) % 4

    if not 0 <= x <= m or not 0 <= y <= m:
        print(-1)
        break
else:
    print(x, y)