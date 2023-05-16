"""
https://www.acmicpc.net/problem/2210

# 입력
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 2 1
1 1 1 1 1

# 출력
15

# 해결법: DFS
"""

import sys

read = sys.stdin.readline
graph = [list(map(int, read().split())) for _ in range(5)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, s):
    s += str(graph[x][y])
    if len(s) == 6:
        result.add(s)
        return ;
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0<= ny<5:
                dfs(nx, ny, s)

result = set()
for i in range(5):
    for j in range(5):
        s = ""
        dfs(i, j, s)

print(len(result))