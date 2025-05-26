from collections import deque

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

# 깊이 우선 탐색, 재귀 함수
def dfs(g, i, visited):
    visited[i] = 1 # 방문 처리
    print(chr(ord('A') + i), end = ' ') # ord fn: 아스키 코드 값 반환
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]: # 두 노드가 연결돼있고 한 번도 방문하지 않았으면.
            dfs(g, j, visited)


# 너비 우선 탐색, deque(양방향 큐, append, popleft)
def bfs(g, i, visited):
    queue = deque([i])
    visited[i] = True
    while queue: # queue에 원소가 남아있으면 방문해야 할 게 남았다는 뜻
        # print(visited)
        i = queue.popleft() # == dequeue
        print(chr(ord('A') + i), end=' ')
        for j in range(len(g)):
            if g[i][j] == 1 and not visited[j]:
                queue.append(j)
                visited[j] = True


visited_dfs = [0 for _ in range(len(graph))] # 0이 8개인 리스트
# visited_bfs = [0 for _ in range(len(graph))] # 0이 8개인 리스트
visited_bfs = [False for _ in range(len(graph))] # 0이 8개인 리스트
dfs(graph, 0, visited_dfs)
print()
bfs(graph, 6, visited_bfs)