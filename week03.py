import array

arr = array.array('f', [11, 9, -77, 8]) # 튜플로 해도 동일
for i in range(len(arr)):
    print(f"{arr[i]:3}, {id(arr[i])}")
print(arr[2]) # 접근은 O(1)