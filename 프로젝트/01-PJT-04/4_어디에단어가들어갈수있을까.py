import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

t = int(input())
for x in range(1, t + 1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    # 세로줄 검증을 위해 행과 열이 뒤바뀐 새로운 행렬을 만듬
    puzzle_90 = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            puzzle_90[i].append(puzzle[j][i])
    
    count = 0
    # 가로줄 검증
    for i in range(n):
        for j in range(n - k + 1):
            # 가장 왼쪽 칸에서는 k개의 흰 칸이 나오고 바로 0이 나와야 함
            if j == 0:
                if puzzle[i][:k] == [1] * k and puzzle[i][k] == 0:
                    count += 1
            # 가장 오른쪽 칸에서는 0 이후에 k개의 흰 칸이 나와야 함
            elif j == n - k:
                if puzzle[i][n - k:] == [1] * k  and puzzle[i][n - k - 1] == 0:
                    count += 1
            # 가운데에 흰 칸이 k개 있는 경우 양 옆에 겸은 칸이 나와야 함
            else:
                if puzzle[i][j:j + k] == [1] * k and puzzle[i][j - 1] == puzzle[i][j + k] == 0:
                    count += 1
    # 세로줄 검증
    for i in range(n):
        for j in range(n - k + 1):
            if j == 0:
                if puzzle_90[i][:k] == [1] * k and puzzle_90[i][k] == 0:
                    count += 1
            elif j == n - k:
                if puzzle_90[i][n - k:] == [1] * k  and puzzle_90[i][n - k - 1] == 0:
                    count += 1
            else:
                if puzzle_90[i][j:j + k] == [1] * k and puzzle_90[i][j - 1] == puzzle_90[i][j + k] == 0:
                    count += 1    
    print('#{}'.format(x), count)   
