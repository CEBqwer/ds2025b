# 실행: alt + shift + F10

import random

num = random.randint(1, 101)
for i in range(1, 8):
    answer = int(input("정답을 입력하세요 : "))
    if num > answer:
        print(f"{answer}보다 큰 수입니다.")
    elif num < answer:
        print(f"{answer}보다 작은 수입니다.")
    elif num > 100 or num < 0:
        print("1에서 100까지의 정수를 입력하세요.")
    else:
        print("정답입니다!")
        break


