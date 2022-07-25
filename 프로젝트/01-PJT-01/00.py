with open("00.txt", 'w', encoding="utf-8") as f:
    f.write("3회차 이주용\n")
    f.write("Hello, Python!\n")
    for i in range(5):
        f.write("{}일차 파이썬 공부 중\n".format(i + 1))