from collections import deque
from heapq import heappush, heappop, heapify

def solution(priorities, location):
    que = deque()
    heap = []
    for idx, p in enumerate(priorities):
        que.append((p, chr(ord('A') + idx)))
        heappush(heap, (-p, chr(ord('A') + idx)))
    answer=0
    while True:
        elem, ch = que.popleft()
        high_elem, high_ch = heappop(heap)
        if elem < -high_elem:
            que.append((elem, ch))
            heappush(heap, (high_elem, high_ch))
        else:
            answer +=1
            print(elem, ch)
            if ch == chr(ord("A") + location):
                break
    return answer