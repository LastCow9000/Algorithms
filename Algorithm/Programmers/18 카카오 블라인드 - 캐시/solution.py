# Programmers 2018 KAKAO BLIND RECRUITMENT - [1차]캐시 Lv2
# https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    dq = deque(cities)
    cache = deque()
    time = 0
    
    while dq:
        city = dq.popleft().lower()
        
        if city in set(cache):
            time += 1
            cache.remove(city) # LRU 최근에 사용된 것을 가장 뒤로 옮겨쥼
            cache.append(city)
            continue
            
        if len(cache) < cacheSize:
            cache.append(city)
            time += 5
        else:
            cache.popleft()
            cache.append(city)
            time += 5
            
    return time