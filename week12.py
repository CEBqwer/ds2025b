def is_connected(temp, v) -> bool:
    pass

v, e = map(int, input().split()) # 정점, 간선 개수 입력 (6 9)
edges = list()

# 춘천 0, 서울 1, 속초 2, 대전 3, 광주 4, 부산 5
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

print(edges)
edges.sort(reverse = True) # 내림차순
print(edges)

selected_edges = edges[:] # edges 복사본
total_cost = sum(cost for cost, a, b in edges)

for cost, a, b in enumerate(edges):
    # 간선을 제거해도 도시의 연결이 안 끊기는지 확인 -> 제거
    temp_edges = [(c, x, y) for c, x, y in selected_edges if not (c==cost and x==a and y==b)]
    if is_connected(temp_edges, v):
        selected_edges = temp_edges
        total_cost = total_cost - cost
        print(f"간선 ({a}------{b}, 가중치 : {cost}) 제거, 현 시점 총 가중치 : {total_cost}")
    else:
        print(f"간선 ({a}------{b}, 가중치 : {cost}) 유지(제거하면 연결 끊어짐)")

print(f"\n최소 신장 트리의 총 가중치 : {total_cost}")
for cost, a, b in sorted(selected_edges): # 간선이 v-1개 나오면 됨
    print(f"{a}------{b}, {cost}")