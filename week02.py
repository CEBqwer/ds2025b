# 실행: alt + shift + F10

n = int(input("정수 입력 : "))
result = 0
for i in range(1, n+1):
   result = result + i
# 시간 복잡도 O(n) <= 선형 시간
print(result)
