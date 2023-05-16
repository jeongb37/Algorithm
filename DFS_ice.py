"""
# 음료수 얼려먹기 문제 = Connected Component
    - 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어짐 (1<=N, M<=1000)
    - 두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어짐
    - 이때 구멍이 뚫려있는 부분은 0, 그렇지않은 부분은 1
    - 결과: 한 번에 만들 수 있는 아이스크림의 개수 출력

    - 입력 예시
    4 5
    00110
    00011
    11111
    00000
    - 출력 예시
    3

    - 해결 방법
    각 영역을 노드로 생각하고, 노드와 연결된 곳을 방문했다고 표현
    # DFS 활용 방법
    1) 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문
    2) 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 진행하는 과정을 반복하면, 연결된 모든 지점을 방문할 수 있음
    3) 모든 노드에 대하여 1~2번의 과정을 반복하면서, 방문하지 않는 지점의 수를 카운트하여 출력
"""
import sys

read = sys.stdin.readline

n, m = map(int, read().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, read().strip())))

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1

print(graph)
print(result)

