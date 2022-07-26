# https://www.acmicpc.net/problem/2609

# 유클리드 호제법
def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    
def lcm(a, b):
    return a * b // gcd(a, b)   

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))

# 내장함수 사용
import math
a, b = map(int, input().split())
print(math.gcd(a, b))
print(math.lcm(a, b))

# 실제로 숫자를 반복문으로 돌면서 최대공약수 찾기
a, b = map(int, input().split())
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        gcd = i
        print(gcd)
        break
lcm = a * b // i
print(lcm)