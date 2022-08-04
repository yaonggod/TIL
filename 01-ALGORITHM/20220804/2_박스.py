# https://www.acmicpc.net/problem/9455
t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]
    
    # 검은 박스를 한 칸씩 내려주는 과정
    # 검은 박스가 맨 위에 있고 나머지 칸은 모두 흰색일 때
    # 검은 박스가 끝까지 내려가기 위해서는 전체 grid에 대해서 m - 1번의 수행이 필요
    count = 0
    for _ in range(m - 1):
        for i in range(m - 2, -1, -1):
            for j in range(n):
                if grid[i + 1][j] == 0 and grid[i][j] == 1:
                    grid[i + 1][j], grid[i][j] = 1, 0
                    count += 1
    print(count)
    
    