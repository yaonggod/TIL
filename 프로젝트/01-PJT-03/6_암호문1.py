import sys

sys.stdin = open("_암호문1.txt")

for i in range(1, 11):
    n = int(input())
    code = list(map(str, input().split()))
    m = int(input())
    # I를 기준으로 commands를 나눔
    # 이 떄 맨 앞의 항이 ''이 나오므로 슬라이싱을 통해 command의 개수랑 일치시켜야함
    commands = list(map(str, input().split('I')))[1:]
    
    # command를 알아볼 수 있게 다듬는 과정이 필요
    # 각 command마다 문자열로 묶여있으므로 리스트로 만들기
    # command 안의 모든 요소는 문자열이므로 추후에 int형 변환 활용 필요
    commands_revised = []
    for command in commands:
        command = command.strip()
        commands_revised.append(list(map(str, command.split())))

    for command in commands_revised:
        # command[1]이 숫자를 삽입하는 개수이므로 command[1]만큼 반복
        for j in range(int(command[1])):
            # command[0]이 숫자를 삽입하는 처음 위치이므로 삽입을 하나 할 때마다 삽입하는 위치도 1씩 증가함
            # 삽입할 숫자는 command[2]부터 command 리스트 끝까지
            code.insert(int(command[0]) + j, command[2 + j])
            
    print('#{}'.format(i), end = ' ')
    # code의 앞에 10개만 출력
    for k in range(10):
        print(code[k], end = ' ')  
    print()
