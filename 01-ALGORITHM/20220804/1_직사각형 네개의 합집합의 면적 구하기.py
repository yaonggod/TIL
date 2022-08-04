# https://www.acmicpc.net/problem/2669
# 직사각형들의 정보 입력
nemo_list = []
for i in range(4):
    nemo_list.append(list(map(int, input().split())))

# 직사각형을 모두 수용할 수 있는 max_x와 max_y를 구함
max_x = nemo_list[0][2]
for i in range(1, 4):
    if nemo_list[i][2] > max_x:
        max_x = nemo_list[i][2]
        
max_y = nemo_list[0][3]
for i in range(1, 4):
    if nemo_list[i][3] > max_y:
        max_y = nemo_list[i][3]

# 새로운 board에 직사각형이 있으면 그 영역을 1로 칠함        
board = [[0] * (max_y) for _ in range(max_x)]

for i in range(4):
    for j in range(nemo_list[i][0], nemo_list[i][2]):
        for k in range(nemo_list[i][1], nemo_list[i][3]):
            board[j][k] = 1

count = 0
for i in range(max_x):
    for j in range(max_y):
        count += board[i][j]
print(count)
