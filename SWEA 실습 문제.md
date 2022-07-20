# SWEA 실습 문제

## 2029. 몫과 나머지 출력하기

> 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.

```python
t = int(input())
test_case = []
for i in range(t):
    test_case.append(list(map(int, input().split())))
    
for i in range(t):
    print("#{}".format(i + 1), test_case[i][0] // test_case[i][1], test_case[i][0] % test_case[i][1])
```

## 1545. 거꾸로 출력해 보아요

> 주어진 숫자부터 0까지 순서대로 찍어보세요

```python
n = int(input())
for i in range(n, -1, -1):
    print(i, end = " ")
```

## 2071. 평균값 구하기

> 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
>
> (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

```python
t = int(input())
test_case = []
for i in range(t):
    test_case.append(list(map(int, input().split())))
    
for i in range(t):
    print("#{}".format(i + 1), round(sum(test_case[i]) / len(test_case[i])))
```

## 2070. 큰 놈, 작은 놈, 같은 놈

> 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.

```python
t = int(input())
test_case = []
for i in range(t):
    test_case.append(list(map(int, input().split())))
    
for i in range(t):
    if test_case[i][0] < test_case[i][1]:
        print("#{}".format(i + 1), "<")
    elif test_case[i][0] > test_case[i][1]:
        print("#{}".format(i + 1), ">")
    else:
        print("#{}".format(i + 1), "=")
```

## 1933. 간단한 N 의 약수

> 입력으로 1개의 정수 N 이 주어진다.
>
> 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

```python
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end = " ")
```

## 2019. 더블더블

> 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
>
> 주어질 숫자는 30을 넘지 않는다.

```python
n = int(input())
for i in range(n + 1):
    print(2 ** i, end = " ")
```

## 2050. 알파벳을 숫자로 변환

> 알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.

```python
t = input()
for i in range(len(t)):
    print(ord(t[i]) - 64, end = " ")
```

## 1986. 지그재그 숫자

> 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

```python
t = int(input())
test_case = []
for i in range(t):
    test_case.append(int(input()))
def zigzag(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum -= i
        else:
            sum += i
    return sum
for i in range(t):
    print("#{}".format(i + 1), zigzag(test_case[i]))
```

## 1284. 수도 요금 경쟁

> 삼성전자에 입사한 종민이는 회사 근처로 이사를 하게 되었다.
>
> 그런데 집의 위치가 두 수도 회사 A, B 중간에 위치하기에 원하는 수도 회사를 선택할 수 있게 되었는데, 두 회사 중 더 적게 수도 요금을 부담해도 되는 회사를 고르려고 한다.
>  
> 종민이가 알아본 결과 두 회사의 수도 요금은 한 달 동안 사용한 수도의 양에 따라 다음과 같이 정해진다.
>  
> A사 : 1리터당 P원의 돈을 내야 한다.
>
> B사 : 기본 요금이 Q원이고, 월간 사용량이 R리터 이하인 경우 요금은 기본 요금만 청구된다. 하지만 R 리터보다 많은 양을 사용한 경우 초과량에 대해 1리터당 S원의 요금을 더 내야 한다.

```python
t = int(input())
test_case = []
for i in range(t):
    test_case.append(list(map(int, input().split())))
                     
def water(p, q, r, s, w):
    a_water = p * w
    if w < r:
        b_water = q
    else:
        b_water = q + (w - r) * s
    return min(a_water, b_water)
                     
for i in range(t):
	print("#{}".format(i + 1), water(test_case[i][0], test_case[i][1], test_case[i][2], test_case[i][3], test_case[i][4]))
```

