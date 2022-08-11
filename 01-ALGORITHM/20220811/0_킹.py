import sys 
sys.stdin = open('0_킹.txt')

move = {
    'R' : (0, 1),
    'L' : (0, -1),
    'B' : (1, 0),
    'T' : (-1, 0),
    'RT' : (-1, 1),
    'LT' : (-1, -1),
    'RB' : (1, 1),
    'LB' : (1, -1)  
}

row = ['8', '7', '6', '5', '4', '3', '2', '1']
column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

king, stone, n = map(str, sys.stdin.readline().split())
x_king, y_king = row.index(king[1]), column.index(king[0])
x_stone, y_stone = row.index(stone[1]), column.index(stone[0])

for i in range(int(n)):
    command = input()
    nx_king = x_king + move[command][0]
    ny_king = y_king + move[command][1]
    # 킹이 체스판 밖으로 안빠져나갈때 이동 처리
    if 0 <= nx_king <= 7 and 0 <= ny_king <= 7:
        x_king = nx_king
        y_king = ny_king
    # 킹이 돌과 겹쳤을 때 킹과 같은 방향으로 이동 처리
    if x_king == x_stone and y_king == y_stone:
        x_stone += move[command][0]
        y_stone += move[command][1]
    # 돌이 체스판 밖으로 빠져나갈 때 킹과 돌의 이동 취소
    if not 0 <= x_stone <= 7 or not 0 <= y_stone <= 7:
        x_king -= move[command][0]
        y_king -= move[command][1]
        x_stone -= move[command][0]
        y_stone -= move[command][1]

king = column[y_king] + row[x_king]
stone = column[y_stone] + row[x_stone]

print(king)
print(stone)    
    
    
       