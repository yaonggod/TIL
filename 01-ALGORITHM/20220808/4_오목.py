# https://www.acmicpc.net/problem/2615
omok = [list(map(int, input().split())) for _ in range(19)]

# 가로 세로 우하향 우상향
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]
win = 0
x_win, y_win = -1, -1
for x in range(19):
    for y in range(19):
        # 오목의 값이 1이거나 2일때
        if omok[x][y]:
            # 4가지 방향 탐사
            for a in range(4):
                # omok[x][y] = 1 or 2므로 count에 미리 1을 더해줌
                count = 1
                # 인덱스가 오목판 안에 있고 새 인덱스가 omok[x][y]랑 같을 시 count += 1 해줌
                for i in range(1, 5):
                    nx = x + i * dx[a]
                    ny = y + i * dy[a]
                    if 0 <= nx < 19 and 0 <= ny < 19 and omok[nx][ny] == omok[x][y]:
                        count += 1
                        
                if count == 5:
                    # 육목일 경우 거름, 왼쪽에 같은 수가 있거나 오른쪽에 같은 수가 있을 때
                    if (0 <= x - dx[a] < 19 and 0 <= y - dy[a] < 19 and omok[x - dx[a]][y - dy[a]] == omok[x][y]) or (0 <= x + 5 * dx[a] < 19 and 0 <= y + 5 * dy[a] < 19 and omok[x + 5 * dx[a]][y + 5 * dy[a]] == omok[x][y]):
                        pass
                    else:
                        win = omok[x][y]
                        x_win = x + 1
                        y_win = y + 1
                         
if win == 1 or win == 2:
    print(win)
    print(x_win, y_win)
else:
    print(win)                    
                        
                        
                    
            

