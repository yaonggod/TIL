# https://www.acmicpc.net/problem/2167
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
new_arr = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        new_arr[i][j] = arr[i - 1][j - 1] + new_arr[i - 1][j] + new_arr[i][j - 1] - new_arr[i - 1][j - 1]

for x in range(k):
    i, j, x, y = map(int, input().split())
    print(new_arr[x][y] - new_arr[x][j - 1] - new_arr[i - 1][y] + new_arr[i - 1][j - 1])       
    
    
## pypy 통과
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for x in range(k):
    i, j, x, y = map(int, input().split())
    sum_arr = 0
    for a in range(i - 1, x):
        for b in range(j - 1, y):
            sum_arr += arr[a][b]
    print(sum_arr)