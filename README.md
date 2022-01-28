# 알고리즘 - 파이썬(Python) rev02

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


<hr><br>

# 2. 느낀점 
  * 1) if문을 사용하고 예외가 발생할 경우에 break를 반드시 사용한다.
