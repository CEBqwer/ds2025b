groups = ['HOT', 'Seventeen', 'Black Pink', 'NJZ']
ratings = [1, 2, 4, 3]

# list 결합에 zip 함수 사용
# 결합하려는 list 원소의 수가 맞아야 제대로 동작
group_rating = list(zip(groups, ratings))
print(group_rating)