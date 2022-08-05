import sys

sys.stdin = open("_파리퇴치.txt")
t = int(input())
for x in range(1, t + 1):
    n, m = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(n)]
    # 죽은 파리의 개수 모든 경우의 수
    flies_list = []
    
    # i, j는 n * n 정사각형 내에서 찾을 수 있는 모든 m * m 정사각형의 시작점
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            # m * m 칸 내의 모든 파리의 개수 더해주기
            sum_flies = 0
            for k in range(m):
                for l in range(m):
                    sum_flies += flies[i + k][j + l]
            flies_list.append(sum_flies)
    print('#{}'.format(x), max(flies_list))