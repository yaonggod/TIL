# https://www.acmicpc.net/problem/1436
n = int(input())
i = 0
x = 0
while True:
    if i == n:
        break
    x += 1
    if '666' in str(x):
        i += 1

print(x)



        
