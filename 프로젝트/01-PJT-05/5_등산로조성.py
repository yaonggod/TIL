import sys
sys.stdin = open("_등산로조성.txt")
# 가장 높은 봉우리에서 시작
# 높은 곳에서 낮은 곳으로, 상하좌우만 연결
# 딱 한 곳을 최대 k만큼 높이를 줄일 수 있음, 높이가 1보다 작아지는 것도 가능

t = int(input())
for i in range(1, t + 1):
    n, k = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(n)]
    # 가장 높은 곳의 높이를 찾기
    max_height = 0
    for a in range(n):
        for b in range(n):
            if land[a][b] > max_height:
                max_height = land[a][b]
                
    # 가장 높은 곳의 좌표를 찾기, 가장 높은 곳의 좌표에서만 탐색할거
    max_height_list = []
    for a in range(n):
        for b in range(n):
            if land[a][b] == max_height:
                max_height_list.append([a, b])
                
    # (x, y) 좌표부터 백트래킹 하기
    def backtracking(x, y, a, b):
        max_length = 0
        # 상 하 좌 우
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 좌표가 땅 안에 존재한다
            if 0 <= nx < n and 0 <= ny < n:
                # 루트 안에 있는 방문했던 좌표는 안된다
                for i in range(len(route)):
                    if route[i][0] == nx and route[i][1] == ny:
                        break
                else:
                    # 내려가는 방향이다
                    if land[nx][ny] < route[-1][2]:
                        route.append([nx, ny, land[nx][ny], 0])
                        # 조건에 맞은 루트가 일단 완성되었으므로 루트 길이 정보에 저장
                        route_list.append(len(route))
                        # 백트래킹
                        backtracking(nx, ny, land[nx][ny], 0)
                        route.pop()
                    # 올라가거나 고도가 같은 방향이나 공사로 극복 가능하다
                    if land[nx][ny] >= route[-1][2] and land[nx][ny] - k < route[-1][2]:
                        construction = 0
                        for i in range(len(route)):
                            construction += route[i][3]
                        # 공사 경험이 없다
                        if construction == 0:
                            route.append([nx, ny, route[-1][2] - 1, 1])
                            # 조건에 맞은 루트가 일단 완성되었으므로 루트 길이 정보에 저장
                            route_list.append(len(route))
                            # 백트래킹
                            backtracking(nx, ny, route[-1][2] - 1, 1) 
                            route.pop()  
            # 다음 좌표가 될 수 없다
            else:
                continue
        
        return max(route_list)
        
    
    max_length_list = []
    for start in max_height_list:
        x = start[0]
        y = start[1]
        route_list = []
        route = [[x, y, land[x][y], 0]]
        max_length = backtracking(x, y, land[x][y], 0)
        max_length_list.append(max_length)
        
    print('#{}'.format(i), max(max_length_list))
    
    
            

    
   

                    
                        
        
        
    
    