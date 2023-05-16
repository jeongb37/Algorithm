"""
# 미로 탈출 문제 = Connected Component
    - N×M크기의 배열로 표현되는 미로가 있음
    - 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타냄
    - 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성
    - 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있음

    - 입력 예시
    4 6
    101111
    101010
    101011
    111011
    - 출력 예시
    15

    - 해결 방법
    # BFS 활용 방법
    1) 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색
    2) 상, 하, 좌, 우로 연결된 모든 노드로의 거리가 1로 동일
    3) 따라서 (1,1)지점부터 BFS를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결
    4) 방문한 곳을 +1 하는 형식으로 마지막 값을 출력
"""

import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split())

graph = []
for i in range(n):
    graph.append(list(map(int, read().strip())))

def bfs(x,y):
    # 큐 구현
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >=n or ny<0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                # 갈 수 있는 노드만 큐에 담으면, 이 노드에 4가지 방향을 확인
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

# 이동할 네 가지 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs를 수행한 결과 출력
print(bfs(0,0))