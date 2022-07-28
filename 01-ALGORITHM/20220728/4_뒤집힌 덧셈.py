# https://www.acmicpc.net/problem/1357

def rev(n):
    return int(str(n)[::-1])

x, y = map(int, input().split())
print(rev(rev(x) + rev(y)))