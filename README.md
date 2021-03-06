# 알고리즘 - 파이썬(Python) Rev08

# 1. 알고리즘 푸는데 필요한 개념

## * 1. 빠른 입력
 <details><summary>CLICK ME</summary>
 
 ```python
  import sys<br>
  sys.stdin.readline().strip() # strip을 사용하지 않으면 \n이 추가적으로 들어가게 된다.
 ```
 
 </details>
 
 <br>
 
### * 2) dictionary 타입<br>

   + 정렬 sorted(), value 기준 // 내림차순 reverse = True 추가
   
   <details><summary>CLICK ME</summary>
 
   ```python
   d = dict() # == d = {}
   sorted(d, key = lambda x : dict[x])
   ```

   ```python
   d = dict() # == d = {}
   sorted(d.items(), key = lambda x : x[1])
   ```
   </details> 

 
   <br>
   
  + 정렬 sorted(), 전체 정렬

   <details><summary>CLICK ME</summary>
 
   ```python
   d = dict() # == d = {}
   sorted(d.items())
   ```

   </details> 
  
   <br>
   
  + max / min key값 기준
   <details><summary>CLICK ME</summary>
 
   ```python
   d = dict() # == d = {}
   max(d, key = d.get)
   min(d, key = d.get)
   ```
   </details> 
   
   <br>
   
  + max / min value값 기준
   <details><summary>CLICK ME</summary>
 
   ```python
   d = dict() # == d = {}
   max(d.values())
   min(d.values())
   ```
   </details> 
   
<br><br>

### * 3) 순열 <sub>4</sub>P<sub>3</sub><br>

<details><summary>CLICK ME</summary>
 
```python
from itertools import permutations
v = [0, 1, 2, 3]
for i in permutations(v, 3): # v에서 4개를 뽑아서 나열
    print(i)
```
</details> 
   
<br><br>

### * 4) 조합 <sub>4</sub>C<sub>2</sub><br>

<details><summary>CLICK ME</summary>
 
```python
from itertools import combinations
v = [0, 1, 2, 3]
for i in combinations(v, 2): # v에서 4개를 뽑아서 나열
    print(i)
```
</details> 

<br><br>

## * 5) 스택(Stack)<br>

<details><summary>CLICK ME</summary>
 
```python
s = []
s.append('값1') # queue에 값을 추가 ['값1']
s.append('값2') # ['값1', '값2']
s.append('값3') # ['값1', '값2', '값3']
while len(s) > 0:
    print(s[-1])
    print(s.pop(-1)) # == print(s.pop()) 제일 뒤에 값이 순차적으로 빠진다. 따라서 ['값1', '값2'] -> ['값1'] ->[]이 된다.
```
</details> 

<br><br>

## * 6) 큐(Queue)<br>
 
<details><summary>CLICK ME</summary>
 
```python
from collections import deque
q = deque
q.append('값1') # queue에 값을 추가 ['값1']
q.append('값2') # ['값1', '값2']
q.appendleft('값3') # ['값3', '값1', '값2']
print(q.pop()) # 제일 뒤에 값('값2')이 빠진다. 따라서 ['값3', '값1']이 된다.
print(q.popleft()) # 제일 앞에 값('값3')이 빠진다. 따라서 ['값1']이 된다.
```
</details> 

<br><br>

## * 7) 힙(Heap) = 우선 순위 큐(Priority Queue) - 기본 min-heap<br>
 
<details><summary>CLICK ME</summary>
 
```python
import heapq as hq
pq = []
hq.heappush(pq, 6)
hq.heappush(pq, 12)
hq.heappush(pq, 0)
hq.heappush(pq, -5)
hq.heappush(pq, 8) # pq = [-5, 0, 6, 8, 12]

while pq:
    print(pq[0])
    hq.heappop(pq) # -5제거 -> 0제거 -> 6제거 -> 8제거 -> 12제거
```
</details> 

<br><br>

## * 8) 탐욕법 : 매 순간마다 최선의 경우만 골라서 가는 방법 따라서 어떤 경우가 최선인지 찾아야 한다.<br>
#### - 조건의 각각이 연관관계를 가지고 있을 때 사용할 수 있다. eg) 배수
#### - eg) 가장 큰 값부터 아래로 차근차근 채워나갈 수 있을 때 사용

<br><br>

## * 9) 재귀함수 : 점화식을 코드로 변형할 수 있지만 제한 조건을 반드시 주어야 한다.<br>
 
<details><summary>CLICK ME</summary>
 
```python
 # 재귀함수 예제
 def recursive_function(i):
     # 100을 호출했을 때 종료
     if i == 100:
         return
     print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
     recursive_function(i+1)
     print(i, '번째 재귀함수를 종료합니다.')
 
 recursive_function(1)
 
 ```
</details> 

<details><summary>CLICK ME</summary>
 
```python
 # eg) 최대공약수 구하는 방법 - 유클리드 호제법
 def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
 
 print(gcd(192, 162))
```
</details> 

<br><br>

## * 10) DFS(Depth first search) 깊이 우선 탐색<br>
#### - 앞으로 찾아 가야할 노드와 이미 방문한 노드를 기준으로 데이터를 탐색
#### - 스택(LIFO)으로 구현할 수 있다.
 
<details><summary>CLICK ME</summary>
 
```python
 # DFS 메소드 정의
# v는 시작 노드, visited는 각 노드가 방문된 정보를 표현하는 리스트
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 2차원 리스트로 표현
graph = [ [], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7] ]

# 각 노드가 방문된 정보를 1차원 리스트로 표현
visited = [False] * 9

dfs(graph, 1, visited)
```
</details> 

<br><br>

## * 11) BFS(Breadth first search) 너비 우선 탐색<br>
 
<details><summary>CLICK ME</summary>
 
```python
 # BFS 메소드 정의
from collections import deque
def bfs(graph, start, visited):
    # 큐(Queue)를 구현하기 위해 deque 라이브러리 사용
    queue = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 존재하지 않을 때까지 반복
    while queue:
        # 큐에서 원소 하나를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')

        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 2차원 리스트로 표현
graph = [ [], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7] ]

# 각 노드가 방문된 정보를 1차원 리스트로 표현
visited = [False] * 9

bfs(graph, 1, visited)
```
</details> 

<br><br>

## * 12) 이진 탐색<br>
#### - 순서가 정렬되어 있는 상태에서 절반씩 나눠 탐색하는 방법
#### - 탐색을 여러번 하는 경우에 유리(NlogN)
 
<details><summary>CLICK ME</summary>
 
```python
#이진 탐색
from bisect import bisect_left, bisect_right

v = (0, 1, 3, 3, 6, 6, 6, 7, 8, 8, 9)
three = bisect_right(v, 3) - bisect_left(v, 3)
four = bisect_right(v, 4) - bisect_left(v, 4)
six = bisect_right(v, 6) - bisect_left(v, 6)

print(f'number of 3 : {three}')
print(f'number of 4 : {four}')
print(f'number of 6 : {six}') 
 
```
</details> 

<br><br>

## * 13) 파라메트릭 서치<br>
#### - 최적화 문제를 결정 문제로 바꿔서 이진탐색으로 푸는 방법
#### - 가능한 해의 영역이 연속적이어야 한다.
#### - 최적화 문제 : 문제 상황을 만족하는 변수의 최솟값, 최댃값을 구하는 문제
#### - 결정 문제 : Yes/No(True/False) 문제
 
<br><br>

## * 14) 동적할당(Dynamic Programming)<br>
#### - 1. Top-down 방식 : 큰 문제를 우선으로 아래로 내려가며 계산하는 방식
##### - 메모이제이션(Memoization)
##### - 직관적이라 코드 가독성이 좋다.
##### - 재귀함수 호출을 많이 해서 느릴 수 있다.
##### - 초깃값 설정을 해줘야 한다.

<details><summary>CLICK ME</summary>
 
```python
import sys
# 반복 횟수 제어
sys.setrecursionlimit(10**7)

# 제한 횟수 설정
MOD = 10007
# N과 K로 각각 숫자를 받아 저장한다.
N, K = map(int, input().split())

# 케시 설정 : 범위가 0 ~ 1000이므로 값 저장할 메모리 설정.
cache = [[0] * 1001 for _ in range(1001)]


def bino(n, k):
    # cache[n][k]가 이미 존재하면 cache[n][k]를 리턴값으로 받는다.
    if cache[n][k]:
        return cache[n][k]

    # k가 0이거나 k가 n이랑 같을 경우에 cache에 1을 넣는다.
    if k == 0 or k == n:
        cache[n][k] = 1
    # cache[n][k] = cache[n-1][k-1] + cache[n-1][k] 점화식 활용.
    # 10007을 넘으면 나머지를 반환하도록 설정.
    else:
        cache[n][k] = bino(n-1, k-1) + bino(n-1, k)
        cache[n][k] = cache[n][k] % MOD
    return cache[n][k]


print(bino(N, K)) 
```
</details> 

<br>

#### - 2. bottom-up 방식 : 작은 문제들로부터 올라가면서 계산하는 방식
##### - 타뷸레이션(Tabulation)
##### - 시간과 메모리를 좀더 아낄 수 있다.
##### - DP 테이블을 채워 나가는 순서를 알아야 한다.
##### - 초깃값 설정을 해줘야 한다.
 
<details><summary>CLICK ME</summary>
 
```python
MOD = 10007
N, K = map(int, input().split())

cache = [[0] * 1001 for _ in range(1001)]

for i in range(1001):
    cache[i][0] = cache[i][i] = 1
    for j in range(1, i):
        cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
        cache[i][j] %= MOD

print(cache[N][K])
```
</details> 

<br><br>


<hr><br>

# 2. 느낀점 
  * 1) if문을 사용하고 예외가 발생할 경우에 break를 반드시 사용한다.
  * 2) 값을 갱신해서 사용하는 경우에 정답과 값 비교 시 갱신 값이 들어가는지 확인한다.
  * 3) 테스트할 때 극단적인 값도 테스트 해본다.(최소값, 최대값 등등...)
  * 4) 논리적으로 접근하여 수학적으로 즉, 함수 형식으로 풀 수 있는지 확인해본다.
  * 5) 수학적으로 점화식을 만들 수 있는지 확인하고 정답이 아니라면 점화식이 아닐 가능성을 확인한다!
  * 6) 함수를 만들어서 풀도록 해보자!
  * 7) 경우의 수를 너무 세분화하지 말고 큰 단위로 나눠서 if문을 작성하자! => 너무 세분화하니 시간복잡도가 커져, 시간 초과 발생...
