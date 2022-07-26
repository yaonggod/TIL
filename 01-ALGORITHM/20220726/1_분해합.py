# https://www.acmicpc.net/problem/2231
a = int(input())

def digit(n):
    sum = 0
    for i in range(len(str(n))):
        sum += int(str(n)[i])
    return sum

n = 0
while n != a:
    if a == n + digit(n):
        print(n)
        break
    n += 1
if n == a:
    print(0)