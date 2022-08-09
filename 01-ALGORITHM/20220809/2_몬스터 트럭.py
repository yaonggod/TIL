# https://www.acmicpc.net/problem/2897
r, c = map(int, input().split())
parking = [list(input()) for _ in range(r)]

count = [0] * 5
for i in range(r - 1):
    for j in range(c - 1):
        lst = []
        for m in range(2):
            for n in range(2):
                lst.append(parking[i + m][j + n])
        if '#' not in lst:
            count[lst.count('X')] += 1

for i in range(5):
    print(count[i])

