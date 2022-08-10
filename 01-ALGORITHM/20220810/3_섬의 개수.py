# https://www.acmicpc.net/problem/4963
import sys

while True:
    # h가 행, w가 열
    w, h = map(int, sys.stdin.readline().split())
    # 입력값이 둘 다 0으로 들어오면 루프 빠져나옴
    if w == h == 0:
        break
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
        
    # 1 2 3
    # 8 X 4
    # 7 6 5
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    
    island = 0    
    while True:
        # 보드 내의 모든 섬을 탐색해서 보드에 0만 있을 때 탈출
        sum_board = 0
        for i in range(h):
            sum_board += sum(board[i])
        if sum_board == 0:
            break
        
        for i in range(h):
            for j in range(w):
                stack = []
                # 처음으로 1이 나온 곳부터 탐색 시작
                if board[i][j] == 1:
                    # 방문 처리
                    board[i][j] = 0
                    stack.append((i, j))
                    # 스택이 빌 때까지 돌면 섬 하나 탐색 완료
                    while stack:
                        x, y = stack.pop()
                        # 8방향 탐색
                        for d in range(8):
                            nx = x + dx[d]
                            ny = y + dy[d]
                            # 보드 안에 인덱스가 존재하고 새로운 좌표가 섬에 해당할 시
                            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 1:
                                # 방문 처리
                                board[nx][ny] = 0
                                # 스택에 넣어서 다음 이어진 공간을 탐색
                                stack.append((nx, ny))
                    # (i, j) 에서 시작한 섬을 탐색 완료했으므로 섬 하나 추가            
                    island += 1
                    
    print(island)
                    




