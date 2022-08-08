# https://www.acmicpc.net/problem/2309
height = [int(input()) for _ in range(9)]
height.sort()
sum_height = sum(height)

fake_1 = 0
fake_2 = 0
for i in range(8):
    for j in range(i + 1, 9):
        # 가짜들의 키를 빼면 키의 합이 100
        if height[i] + height[j] == sum(height) - 100:
            fake_1, fake_2 = i, j
            break

for i in range(9):
    if i != fake_1 and i != fake_2:
        print(height[i])