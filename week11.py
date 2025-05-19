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

# 깊이 우선 탐색
def dfs(g, i, visited):
    visited[i] = 1 # 방문 처리
    print(chr(ord('A') + i), end = ' ') # ord fn: 아스키 코드 값 반환
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]: # 두 노드가 연결돼있고 한 번도 방문하지 않았으면.
            dfs(g, j, visited)

visited_dfs = [0 for _ in range(len(graph))] # 0이 8개인 리스트
dfs(graph, 0, visited_dfs)