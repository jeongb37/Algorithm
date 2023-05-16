import sys

"""
python sys.stdin의 경우, 사용자의 입력을 Buffer에 저장한 후에 요청이 올 때마다 읽기 때문에 input()보다 빠르게 동작함
"""

### N개의 정수를 한 줄로 입력받아 List에 저장할 경우
read = sys.stdin.readline
data = list(map(int, read().split()))

### 정수의 개수인 N과, N개의 정수를 한 줄로 입력받아 List에 저장하는 경우
read = sys.stdin.readline
N = int(read())
data = list(map(int, read().split()))

### N개의 정수를 여러 줄에 걸쳐 입력 받아 List에 저장할 경우
read = sys.stdin.readline
N = int(read())
data = [int(read()) for _ in range(N)]

### N개의 문자열을 여러 줄에 걸쳐 입력 받아 List에 저장할 경우, strip을 이용하여 '\n'을 없애기

N = int(read())
data = [read().strip() for _ in range(N)]

### N개의 정수를 여러 줄에 걸쳐 입력 받아 이차원 배열에 저장할 경우
read = sys.stdin.readline
N = int(read())
data = [list(map(int, read().split())) for _ in range(N)]

print(N)
print(data)