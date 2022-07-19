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

